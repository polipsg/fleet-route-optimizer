import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("route_prediction_model.pkl")

# Possible cities
CITIES = ["A", "B", "C", "D", "E"]

# Number of routes to test
NUM_ROUTES = 50

np.random.seed(42)

# Generate possible routes
routes = pd.DataFrame({
    "origin": np.random.choice(CITIES, NUM_ROUTES),
    "destination": np.random.choice(CITIES, NUM_ROUTES),
    "distance_km": np.random.uniform(1, 30, NUM_ROUTES),
    "num_stops": np.random.randint(1, 8, NUM_ROUTES),
    "traffic_level": np.random.randint(1, 5, NUM_ROUTES),
    "hour_day": np.random.randint(0, 24, NUM_ROUTES)
})

# Predict delivery time
routes["predicted_delivery_time"] = model.predict(routes)

# Sort routes by best predicted time
routes = routes.sort_values("predicted_delivery_time")

print("\nTop 5 best routes:\n")
print(routes.head())

# Best route
best_route = routes.iloc[0]

print("\nBest route found:\n")
print(best_route)