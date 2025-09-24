# house-plant-assistant
I built this project because I'm terrible at taking care of my plants. I realized they might not be getting enough sunlight, so I made a plant assistant using a Raspberry Pi that tells me if a plant is in an ideal spot in my home.

# How it works
The user places the Raspberry Pi, which is connected to a Lux sensor (TSL2561), right next to their plant in its growing location. A photo of the plant is taken with the user's phone and uploaded to the system, where the CNN model classifies the plant species. The user then points their phone towards the window closest to the plant, allowing the compass to record the direction of incoming sunlight. At the same time, the Pi measures the current lux level in that exact spot and records the time of day and current season. Peak sunlight in that spot is calculated, providing an estimate of the maximum light the plant could receive at that location to determine if conditions are ideal for its growth.

# Peak Sunlight
The assistant estimates peak sunlight starting with the sensor’s lux reading at the plant’s spot. It adjusts this value using three factors:
- Time of day – the amount of lux received by the sun varies throughout the day. 
- Season – more light in summer, less in winter.
- Window direction – south-facing gets the most light, north-facing the least.

By combining these adjustments, the assistant predicts the maximum amount of sunlight the plant receives in that location and compares it to the plant’s ideal range.

# Plant-Classifier-using-ResNet-18.ipynb
Fine-tuning a pre-trained CNN (ResNet-18) on a dataset containing 47 common house plant species to identify the user's plant. Link to the dataset: https://www.kaggle.com/datasets/kacpergregorowicz/house-plant-species 

# Flask Server
To prototype this project, I deployed the website on a Raspberry Pi Flask server running on the Raspberry Pi. 
