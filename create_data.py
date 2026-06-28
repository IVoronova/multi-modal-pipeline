import pandas as pd
import numpy as np
import json
import os

# Create a CSV of fake sensor readings
data = {
    "id": [1, 2, 3, 4, 5],
    "heart_rate": [72, 75, 70, 68, 74],
    "temperature": [98.6, 99.1, 98.4, 98.7, 99.0],

}

pd.DataFrame(data).to_csv("sensor_readings.csv", index=False)

# Create a JSON of fake sensor readings
metadata = {
    "1": {"name": "Alice", "status": "healthy"},
    "2": {"name": "Bob", "status": "fever"},
    "3": {"name": "Charlie", "status": "healthy"},
    "4": {"name": "Dave", "status": "critical"},
    "5": {"name": "Eve", "status": "healthy"},
}

with open("sensor_metadata.json", "w") as f:
    json.dump(metadata, f)


# Create a folder of fake images
os.makedirs("images", exist_ok=True)
print("Data created successfully!")