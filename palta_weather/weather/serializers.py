"""Weather serializers."""
from marshmallow import EXCLUDE

from palta_weather.extensions import ma
from palta_weather.weather.models import Weather


class WeatherSchema(ma.SQLAlchemyAutoSchema):
    """Weather Schema."""

    class Meta:
        """Schema meta-class."""

        model = Weather
        unknown = EXCLUDE
        load_instance = True
        datetimeformat = "%Y-%m-%dT%H:%M:%S+00:00"
