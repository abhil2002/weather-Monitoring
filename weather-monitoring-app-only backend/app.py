from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
import os

# Initialize Flask app
app = Flask(__name__)

# SQLAlchemy configuration for MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+pymysql://flaskuser:password@db/weather_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Celery configuration
def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=os.getenv('CELERY_BACKEND_URL', 'redis://redis:6379/0'),
        broker=os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0')
    )
    celery.conf.update(app.config)
    return celery

celery = make_celery(app)

# Import routes and tasks (ensure these files exist)
from app import api, tasks

# Main entry point
if __name__ == "__main__":
    # Run the Flask app on the default port 5000
    app.run(host="0.0.0.0", port=5000)
