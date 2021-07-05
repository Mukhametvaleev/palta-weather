"""Weather Celery Tasks definitions."""
import os

import requests
from celery import shared_task
from celery.utils.log import get_task_logger

from palta_weather.extensions import db
from palta_weather.weather.events import notify_weather_update
from palta_weather.weather.serializers import WeatherSchema

logger = get_task_logger(__name__)


@shared_task(ignore_result=True)
def update_weather():
    """Update weather pipeline."""
    chain = fetch_weather.s() | parse_and_store_weather.s()
    chain()


@shared_task
def fetch_weather():
    """Fetch new weather values."""
    lat, lon = os.environ["COORD"].split(",")
    api_key = os.environ["YANDEX_API_KEY"]
    headers = {"X-Yandex-API-Key": api_key}
    response = requests.get(
        f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}",
        headers=headers,
    )
    weather_dict = response.json()["fact"]
    return weather_dict


@shared_task(ignore_result=True)
def parse_and_store_weather(weather_dict):
    """Parse and store weather in database."""
    weather_schema = WeatherSchema()
    weather = weather_schema.load(weather_dict)
    try:
        db.session.add(weather)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
    else:
        notify_weather_update()
