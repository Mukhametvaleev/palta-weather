"""Application extensions definitions."""
from flask_celeryext import FlaskCeleryExt
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from palta_weather.celery_utils import make_celery

ext_celery = FlaskCeleryExt(create_celery_app=make_celery)
ma = Marshmallow()
migrate = Migrate()
socketio = SocketIO()
db = SQLAlchemy()
