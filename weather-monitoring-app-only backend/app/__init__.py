from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Migrate
from celery import Celery
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Load config from environment variable
app.config.from_envvar('APP_CONFIG_FILE')

# SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, to suppress warnings

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

# Celery configuration for background tasks
def make_celery(app):
    celery = Celery(app.import_name, broker=os.getenv('CELERY_BROKER_URL'))
    celery.conf.update(app.config)
    return celery

celery = make_celery(app)

# Import your API routes after initializing the app and db
from app import api
