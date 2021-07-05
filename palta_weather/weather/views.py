"""Weather API views."""
import os

from flask import render_template

from palta_weather.weather import weather_blueprint

CITY = os.environ["APP_NAME"]


@weather_blueprint.route(f"/{CITY}")
def index():
    """Weather index route."""
    return render_template("index.jinja2", city=CITY)
