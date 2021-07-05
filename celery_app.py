"""Palta weather app factory instance."""
from subprocess import call

import click

from palta_weather import create_app
from palta_weather.extensions import ext_celery

app = create_app()
celery = ext_celery.celery


@app.cli.command("celery_worker")
@click.option("--loglevel", type=str)
def celery_worker(loglevel):
    """Run Celery worker."""
    from watchgod import run_process

    def run_worker():
        """Run worker."""
        call(
            [
                "celery",
                "-A",
                "celery_app.celery",
                "worker",
                f"--loglevel={loglevel}",
                "--uid=nobody",
                "--gid=nogroup",
            ]
        )

    run_process(".", run_worker)
