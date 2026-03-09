'''
Notebook ML 
'''
# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
df = pd.read_csv("synthetic_routes_dataset.csv")

# Features and target
X = df.drop("delivery_time_minutes", axis=1)
y = df["delivery_time_minutes"]
# Categorical and numerical columns
categorical_features = [ "origin", "destination"]
numerical_features = ["distance_km", "num_stops", "traffic_level", "hour_day"]
# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", "passthrough", numerical_features)
    ]
)

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
pipeline.fit(X_train, y_train)

# Predictions
predictions = pipeline.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)

print("Model trained successfully!")
print("Mean Absolute Error:", mae)

# Save model
joblib.dump(pipeline, "route_prediction_model.pkl")

print("Model saved as route_prediction_model.pkl")