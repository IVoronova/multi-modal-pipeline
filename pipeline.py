import pandas as pd
import numpy as np
import json
from PIL import Image
import os

# Load the cvs
sensor_data = pd.read_csv("sensor_readings.csv")
print("Sensor Data:")
print(sensor_data)

# Load the json
with open("sensor_metadata.json", "r") as f:
    metadata = json.load(f)

print("\nSensor Metadata:")
print(metadata)

# Convert JSON to a DataFrame
metadata_df = pd.DataFrame.from_dict(metadata, orient='index')
metadata_df.index = metadata_df.index.astype(int)  # Convert index to integer for merging   
metadata_df.index.name = "id"  # Set the index name to 'id'
metadata_df = metadata_df.reset_index()  # Reset index to make 'id' a column

# Merge the sensor data with the metadata
merged = pd.merge(sensor_data, metadata_df, on='id', how='left')
print("\nMerged Data:")
print(merged)

# Load images and attach them to merged DataFrame
image_paths = []
for i in range(1, 6):
    path = f"images/patient_{i}_scan.png"
    image_paths.append(path)

merged['image_path'] = image_paths
print("\n Final Pipeline Output:")
print(merged)