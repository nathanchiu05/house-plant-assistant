from fastai.vision.all import *
from datetime import datetime
import pandas as pd

from season_database import season_from_month, time_of_day, season_db

import board
import busio
import adafruit_tsl2561
import time

# Load model
learn = load_learner('/home/fryrize/projects/house_plant_project/resnet18-houseplants.pkl')

#load lux dataset
df = pd.read_excel('/home/fryrize/projects/house_plant_project/lux_dataset.xlsx')

#Setup light sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2561.TSL2561(i2c)
sensor.enabled = True
sensor.gain = 0
sensor.integration_time = 1
time.sleep(1)  #allow sensor to stabilize

#Test Sensor: sudo i2cdetect -y 1
#PIN Mapping
#VCC (pin 1)
#GND (pin 6)
#SCL (pin 5)
#SDA (pin 3)
#Test Connection in terminal: i2cdetect -y 1

def is_night(tod):
    if tod == "Night":
        return True
    return False

def classify_plant(image_path: str):
    is_plant, _, probs = learn.predict(image_path)
    return str(is_plant), max(probs).item()

def get_lux():
    return sensor.lux

def get_bounds(plant_name, df=df):
    row = df[df['Plant Species'] == plant_name]
    min_lux = row['lower_lux'].values[0]
    max_lux = row['upper_lux'].values[0]
    return min_lux, max_lux

def get_rating(min_lux, max_lux, plant_name, adjusted_lux):
    row = df[df['Plant Species'] == plant_name]
    min_lux = row['lower_lux'].values[0]
    max_lux = row['upper_lux'].values[0]

    if adjusted_lux < min_lux:
        return (f"Recommended lux for {plant_name} is between {min_lux} and {max_lux}. The peak light level of this spot is {adjusted_lux} lux, which is too low.")

    elif adjusted_lux > max_lux:
        return (f"Recommended lux for {plant_name} is between {min_lux} and {max_lux}. The peak light level of this spot is {adjusted_lux} lux, which is too high.")
    else:
        return (f"Recommended lux for {plant_name} is between {min_lux} and {max_lux}. The peak light level of this spot is {adjusted_lux} lux, which is optimal.")
 
#run ML model, get current light level, time of day, season. Gets called in plant_app.py
def evaluate_plant(image_path: str, direction: str):

    plant, confidence = classify_plant(image_path)
    lux = get_lux()
    curr = datetime.now()
    month = curr.month
    hour = curr.hour
    season = season_from_month(month)
    tod = time_of_day(season, hour)

    if tod == "Night":
        return {
            "plant": plant,
            "confidence": round(confidence, 3),
            "lux": None,
            "season": season,
            "time_of_day": tod,
            "peak_lux": None,
            "direction": direction,
            "rating": "Hello Night"
        }

    exposure_factor = season_db [season][tod][direction] #exposure_factor gives fraction of max light for that season, time of day, and direction
    adjusted_lux = round(lux / exposure_factor,2)
    
    get_bounds(plant)
    min_lux, max_lux = get_bounds(plant)
    rating = get_rating(min_lux, max_lux, plant, adjusted_lux)

    return {
        "plant": plant,
        "confidence": round(confidence, 3),
        "lux": round(lux, 2) if lux else None,
        "season": season,
        "time_of_day": tod,
        "peak_lux": adjusted_lux,
        "direction": direction,
        "rating": rating,
        "min_lux": min_lux,
        "max_lux": max_lux
    }