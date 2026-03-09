"""
Synthetic route dataset generator.

Generates simulated delivery routes including:
- origin
- destination
- distance
- number of stops
- traffic level
- hour of day
- simulated delivery time
"""

# Import libraries
import pandas as pd
import numpy as np

# Setting the number of samples
NUM_SAMPLES = 10000
CITIES = ["A","B","C","D","E"]

np.random.seed(42)

def generate_dataset(n_samples=NUM_SAMPLES):

    data = {
        "origin": np.random.choice(CITIES, n_samples),
        "destination": np.random.choice(CITIES, n_samples),
        "distance_km": np.random.uniform(1,30, n_samples),
        "num_stops": np.random.randint(1, 8, n_samples),
        "traffic_level": np.random.randint(1, 5, n_samples),
        "hour_day": np.random.randint(0, 24, n_samples)
    }

    df = pd.DataFrame(data)

    # Formula simulating delivery time
    df["delivery_time_minutes"] = (
        df["distance_km"] * 2.5 +
        df["num_stops"] * 4 +
        df["traffic_level"] * 6 +
        np.where((df["hour_day"] >= 7) & (df["hour_day"] <= 9), 10, 0) +
        np.where((df["hour_day"] >= 17) & (df["hour_day"] <= 19), 12, 0) +
        np.random.normal(0, 3, len(df))
    )

    return df


def save_dataset():
    df = generate_dataset()
    df.to_csv("synthetic_routes_dataset.csv", index=False)

    print("Dataset generated successfully!")
    print(df.head())


if __name__ == "__main__":
    save_dataset()