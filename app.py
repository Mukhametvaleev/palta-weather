"""Palta weather app factory instance."""
import eventlet

eventlet.monkey_patch()

from palta_weather import create_app
from palta_weather.extensions import socketio

app = create_app()

if __name__ == "__main__":
    socketio.run(app, debug=True, use_reloader=True, host="0.0.0.0")
