from app import celery
from app.models import WeatherSummary, db
from app.utils import kelvin_to_celsius
import requests

@celery.task
def fetch_weather_data():
    API_KEY = os.getenv('OPENWEATHER_API_KEY')
    CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

    for city in CITIES:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()

        weather_summary = WeatherSummary(
            city=city,
            temp=kelvin_to_celsius(data['main']['temp']),
            feels_like=kelvin_to_celsius(data['main']['feels_like']),
            main=data['weather'][0]['main'],
            timestamp=data['dt']
        )
        db.session.add(weather_summary)
        db.session.commit()
