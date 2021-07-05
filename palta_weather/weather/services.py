"""Weather services."""
from sqlalchemy import desc

from palta_weather.weather.models import Weather


def get_last_weather(limit: int = 10):
    """Returns last weather rows based on `limit` arg."""
    return reversed(Weather.query.order_by(desc(Weather.id)).limit(limit).all())
