from app import db

class WeatherSummary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    temp = db.Column(db.Float, nullable=False)
    feels_like = db.Column(db.Float, nullable=False)
    main = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<WeatherSummary {self.city} {self.temp}°C>'
