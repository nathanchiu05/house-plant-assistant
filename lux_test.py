import board
import busio
import adafruit_tsl2561
import time

#setup I2C
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2561.TSL2561(i2c)
sensor.enabled = True
sensor.gain = 0 
sensor.integration_time = 1 

time.sleep(1)

print(f"Measured Lux: {sensor.lux:.2f} lx")