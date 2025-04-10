import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load and clean column names
df = pd.read_csv("quikr_car.csv")
df.columns = df.columns.str.strip().str.lower()  # Normalize column names

print("Columns:", df.columns.tolist())  # 🔍 DEBUG: See actual column names

# Clean data
if 'price' not in df.columns:
    raise ValueError("❌ 'price' column not found. Check CSV column headers.")

df = df[df['price'].str.contains('ask for price', case=False) == False]
df['price'] = df['price'].str.replace(',', '', regex=True).astype(int)

# Clean other columns
df['year'] = pd.to_numeric(df['year'], errors='coerce')

df['kms_driven'] = df['kms_driven'].str.replace(' kms', '', regex=False).str.replace(',', '', regex=False)
df['kms_driven'] = pd.to_numeric(df['kms_driven'], errors='coerce')

df = df[df['fuel_type'].notnull()]
df = df[df['name'].notnull()]

# Extract brand
df['brand'] = df['name'].str.split().str[0]

# Final selection
df = df[['brand', 'year', 'kms_driven', 'fuel_type', 'price']]

# Encode categorical
brand_map = {b: i for i, b in enumerate(df['brand'].unique())}
fuel_map = {'Petrol': 0, 'Diesel': 1, 'LPG': 2}

df['brand'] = df['brand'].map(brand_map)
df['fuel_type'] = df['fuel_type'].map(fuel_map)

df.dropna(inplace=True)

# Train model
X = df[['brand', 'year', 'kms_driven', 'fuel_type']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
os.makedirs("model", exist_ok=True)
pickle.dump(model, open("model/car_price_model.pkl", "wb"))

print("✅ Model trained and saved successfully!")
