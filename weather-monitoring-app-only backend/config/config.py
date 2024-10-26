from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "mysql+pymysql://user:password@localhost/weather"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Recommended to avoid overhead
    CELERY_BROKER_URL = os.getenv(
        "CELERY_BROKER_URL", "redis://localhost:6379/0"
    )
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
