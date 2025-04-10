from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model/car_price_model.pkl', 'rb'))

# Home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/light')
def light():
    return render_template('light.html')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        brand = request.form['brand']
        year = int(request.form['year'])
        km_driven = int(request.form['km_driven'])
        fuel = request.form['fuel']

        # Simple feature engineering (example)
        fuel_map = {'Petrol': 0, 'Diesel': 1, 'LPG': 2}
        brand_map = {'Maruti': 0, 'Hyundai': 1, 'Honda': 2, 'Toyota': 3}

        fuel_type = fuel_map.get(fuel, 0)
        brand_encoded = brand_map.get(brand, 0)

        features = np.array([[brand_encoded, year, km_driven, fuel_type]])

        prediction = model.predict(features)[0]
        predicted_price = round(prediction, 2)

        return jsonify({'price': predicted_price})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
