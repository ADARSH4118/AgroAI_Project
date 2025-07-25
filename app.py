from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os
from dotenv import load_dotenv
import requests

app = Flask(__name__)
load_dotenv()

model_type = pickle.load(open('model/fertilizer_type_model.pkl', 'rb'))
model_quantity = pickle.load(open('model/fertilizer_quantity_model.pkl', 'rb'))
model_timing = pickle.load(open('model/fertilizer_timing_model.pkl', 'rb'))

soil_encoder = pickle.load(open('model/soil_encoder.pkl', 'rb'))
crop_encoder = pickle.load(open('model/crop_encoder.pkl', 'rb'))
fertilizer_decoder = pickle.load(open('model/fertilizer_encoder.pkl', 'rb'))
timing_decoder = pickle.load(open('model/timing_encoder.pkl', 'rb'))

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather_data(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            return None, None, None
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        rainfall = data.get('rain', {}).get('3h', 0)
        return temp, humidity, rainfall
    except Exception as e:
        print("Weather API error:", e)
        return None, None, None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        soil = request.form['soil']
        crop = request.form['crop']
        pH = float(request.form['ph'])
        city = request.form['city']

        temp, humidity, rainfall = get_weather_data(city)
        if temp is None:
            return jsonify({'error': 'Invalid city or weather API error.'}), 400

        try:
            soil_encoded = soil_encoder.transform([soil])[0]
            crop_encoded = crop_encoder.transform([crop])[0]
        except Exception:
            return jsonify({'error': 'Unrecognized soil or crop type.'}), 400

        features = np.array([[soil_encoded, pH, crop_encoded, temp, humidity, rainfall]])

        fert_type_pred = model_type.predict(features)[0]
        fert_qty_pred = model_quantity.predict(features)[0]
        fert_timing_pred = model_timing.predict(features)[0]

        fert_type_label = fertilizer_decoder.inverse_transform([fert_type_pred])[0]
        fert_timing_label = timing_decoder.inverse_transform([fert_timing_pred])[0]

        return jsonify({
            'prediction': True,
            'city': city,
            'temp': round(temp, 1),
            'humidity': humidity,
            'rainfall': rainfall,
            'fert_type': fert_type_label,
            'fert_qty': int(fert_qty_pred),
            'fert_time': fert_timing_label
        })
    except Exception as e:
        print("Server error:", e)
        return jsonify({'error': 'An internal server error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
