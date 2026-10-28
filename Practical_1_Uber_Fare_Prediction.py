# Practical 1: Uber Fare Prediction
# Dataset required: uber.csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from math import radians, cos, sin, asin, sqrt

# 1. Load dataset
df = pd.read_csv("uber.csv")
print("Initial Data Shape:", df.shape)
print(df.head())

# 2. Preprocess data
df.dropna(inplace=True)
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"], errors="coerce")
df.dropna(subset=["pickup_datetime"], inplace=True)

df["hour"] = df["pickup_datetime"].dt.hour
df["day"] = df["pickup_datetime"].dt.day
df["month"] = df["pickup_datetime"].dt.month
df["year"] = df["pickup_datetime"].dt.year
df["day_of_week"] = df["pickup_datetime"].dt.dayofweek
df.drop(["pickup_datetime", "key", "Unnamed: 0"], axis=1, inplace=True, errors="ignore")

# 3. Remove outliers
df = df[(df["fare_amount"] > 0) & (df["fare_amount"] < 100)]
for col in ["pickup_latitude", "dropoff_latitude"]:
    df = df[df[col].between(-90, 90)]
for col in ["pickup_longitude", "dropoff_longitude"]:
    df = df[df[col].between(-180, 180)]

# 4. Calculate pickup-to-dropoff distance using Haversine formula
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    return 6371 * 2 * asin(sqrt(a))

df["distance_km"] = df.apply(
    lambda row: haversine(
        row["pickup_latitude"], row["pickup_longitude"],
        row["dropoff_latitude"], row["dropoff_longitude"]
    ), axis=1
)
df = df[df["distance_km"] > 0]

# 5. Correlation analysis
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.show()

# 6. Train and test models
X = df.drop("fare_amount", axis=1)
y = df["fare_amount"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
}

for name, model in models.items():
    print(f"\n--- {name} ---")
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    print("MAE:", mean_absolute_error(y_test, predictions))
    print("RMSE:", rmse)
    print("R2 Score:", r2_score(y_test, predictions))
