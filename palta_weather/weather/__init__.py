"""Weather API Blueprint."""

from flask import Blueprint

weather_blueprint = Blueprint("weather", __name__, url_prefix="/weather")

from . import events, models, tasks, views  # noqa
