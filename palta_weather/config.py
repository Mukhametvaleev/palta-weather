"""Application config definition."""

import os


class BaseConfig:
    """Base configuration"""

    TESTING = False
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    SOCKETIO_MESSAGE_QUEUE = os.environ["SOCKETIO_MESSAGE_QUEUE"]

    broker_url = os.environ["CELERY_BROKER_URL"]
    result_backend = os.environ["CELERY_RESULT_BACKEND"]

    CELERYBEAT_SCHEDULE = {
        "update-weather": {
            "task": "palta_weather.weather.tasks.update_weather",
            "schedule": int(os.environ["SCHEDULE"]),
        },
    }


class DevelopmentConfig(BaseConfig):
    """Development configuration"""

    DEBUG = True


config = {
    "development": DevelopmentConfig,
}
