import matplotlib.pyplot as plt
from app.models import WeatherSummary

def generate_daily_summary():
    summaries = WeatherSummary.query.all()
    # Use matplotlib or Plotly to create a plot here.
