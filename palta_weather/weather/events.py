"""Weather SocketIO events."""
import os

from flask_socketio import emit, join_room

from palta_weather.extensions import socketio
from palta_weather.weather.serializers import WeatherSchema
from palta_weather.weather.services import get_last_weather

room = os.environ["APP_NAME"]


def notify_weather_update():
    """Notify room that weather was updated."""
    last_weather = get_last_weather()
    weather_schema = WeatherSchema(many=True)
    weather_dicts = weather_schema.dump(last_weather)

    emit("weather_update", weather_dicts, room=room, namespace="/weather")


@socketio.on("join", namespace="/weather")
def on_join_weather():
    """On join weather city room."""
    join_room(room)
    notify_weather_update()
