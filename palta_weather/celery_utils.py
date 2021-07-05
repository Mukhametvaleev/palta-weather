"""Weather Celery app instance factory."""

from celery import current_app as current_celery_app, Task


def make_celery(app):
    """Make Celery app."""
    celery = current_celery_app
    celery.config_from_object(app.config)

    if not hasattr(celery, "flask_app"):
        celery.flask_app = app

    class ContextTask(Task):
        """Celery task running within a Flask application context."""

        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return Task.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery
