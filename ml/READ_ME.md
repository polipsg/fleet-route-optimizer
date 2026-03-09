# ML-Based Route Optimization

This project demonstrates a simple Machine Learning pipeline for route optimization using synthetic delivery data.

The goal is to simulate historical delivery routes, train a machine learning model to predict delivery time, and evaluate multiple route options to select the most efficient one.

---

## Project Overview

Traditional routing algorithms often rely on static rules. This project explores how Machine Learning can help estimate delivery times based on historical patterns such as:

* route distance
* number of stops
* traffic level
* time of day
* origin and destination

The trained model can then be used to evaluate multiple possible routes and choose the best one based on predicted delivery time.

---

## Project Structure

```
project/

generate_dataset.py
train_route_model.py
predict_route.py

synthetic_routes_dataset.csv
route_prediction_model.pkl

README.md
```

---

## Workflow

The project follows a simple Machine Learning pipeline:

1. Generate synthetic historical route data
2. Train a machine learning model
3. Predict delivery time for multiple routes
4. Select the best route based on predicted time

Pipeline overview:

```
Dataset → Model Training → Route Prediction → Best Route Selection
```

---

## Dataset

The synthetic dataset simulates delivery routes with the following features:

| Column                | Description              |
| --------------------- | ------------------------ |
| origin                | starting city            |
| destination           | destination city         |
| distance_km           | route distance           |
| num_stops             | number of delivery stops |
| traffic_level         | simulated traffic level  |
| hour_day              | hour of the day          |
| delivery_time_minutes | simulated delivery time  |

The dataset is generated using Python libraries such as **pandas** and **numpy**.

---

## Model

The model is trained using a **Random Forest Regressor** to predict delivery time.

Steps included in the pipeline:

* preprocessing categorical variables (origin and destination)
* encoding categorical features
* training a regression model
* evaluating model performance

The target variable is:

```
delivery_time_minutes
```

Model performance is evaluated using **Mean Absolute Error (MAE)**.

---

## How to Run

### 1. Generate the dataset

Run the dataset generator:

```
python generate_dataset.py
```

This will create:

```
synthetic_routes_dataset.csv
```

---

### 2. Train the model

Run the training script:

```
python train_route_model.py
```

This will train the model and save it as:

```
route_prediction_model.pkl
```

---

### 3. Predict the best route

Run the route prediction script:

```
python predict_route.py
```

The script generates multiple candidate routes, predicts delivery time for each route, and selects the best one.

---

## Example Output

Example result from the route prediction script:

```
Top 5 best routes:

origin destination distance_km num_stops traffic_level hour_day predicted_delivery_time

B D 7.3 1 1 11 22.1
A C 8.5 2 1 10 25.4
D E 9.1 1 2 13 27.6
```

Best route selected:

```
distance_km: 7.3
num_stops: 1
traffic_level: 1
predicted_delivery_time: 22.1
```

---

## Technologies Used

This project uses the Python data science ecosystem:

* pandas
* numpy
* scikit-learn
* joblib

---

## Future Improvements

Possible future improvements include:

* integrating the model with a route optimization solver
* adding geographic coordinates to simulate real maps
* implementing a full Vehicle Routing Problem solver
* exposing the model through an API for backend integration

---

## Purpose

This project serves as a demonstration of how Machine Learning can be applied to delivery route prediction and optimization using simulated data.
