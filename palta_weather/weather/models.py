"""Weather models."""
from datetime import datetime

from palta_weather.extensions import db


class Weather(db.Model):
    """Weather model."""

    __tablename__ = "weather"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    temp = db.Column(db.Integer(), nullable=False)
    feels_like = db.Column(db.Integer(), nullable=False)
    condition = db.Column(db.String(22), nullable=False)
    wind_speed = db.Column(db.Integer(), nullable=False)
    wind_dir = db.Column(db.String(2), nullable=False)
    pressure_mm = db.Column(db.Integer(), nullable=False)
    pressure_pa = db.Column(db.Integer(), nullable=False)
