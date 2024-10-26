from flask import jsonify
import requests
from app.models import WeatherSummary
from app import app, db

API_KEY = os.getenv('OPENWEATHER_API_KEY')
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

@app.route('/weather', methods=['GET'])
def get_weather_data():
    weather_data = []
    for city in CITIES:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        weather_data.append({
            'city': city,
            'temperature': kelvin_to_celsius(data['main']['temp']),
            'feels_like': kelvin_to_celsius(data['main']['feels_like']),
            'main': data['weather'][0]['main'],
            'timestamp': data['dt']
        })
    return jsonify(weather_data)

def kelvin_to_celsius(kelvin_temp):
    return round(kelvin_temp - 273.15, 2)
