"""Palta weather app definition."""
import os

from flask import Flask

from palta_weather import extensions
from palta_weather.config import config
from palta_weather.error_handlers import page_not_found


def create_app(config_name=None):
    """Application Factory."""
    if config_name is None:
        config_name = os.environ["FLASK_CONFIG"]

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)
    register_shell_context(app)

    return app


def register_extensions(app):
    """Register application extensions."""
    extensions.ext_celery.init_app(app)
    extensions.ma.init_app(app)
    extensions.migrate.init_app(app, extensions.db)
    extensions.socketio.init_app(
        app, message_queue=app.config["SOCKETIO_MESSAGE_QUEUE"]
    )
    extensions.db.init_app(app)


def register_blueprints(app):
    """Register application blueprints."""
    from palta_weather.weather import weather_blueprint

    app.register_blueprint(weather_blueprint)


def register_error_handlers(app):
    """Register application error handlers."""
    app.register_error_handler(404, page_not_found)


def register_shell_context(app):
    """Register application shell context."""

    def get_shell_context():
        """Shell context objects."""
        return {
            "app": app,
            "db": extensions.db,
        }

    app.shell_context_processor(get_shell_context)
