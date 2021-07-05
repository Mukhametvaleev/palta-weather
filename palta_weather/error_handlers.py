"""Weather error handlers."""
from flask import redirect, url_for


def page_not_found(e):
    """If page not found"""
    return redirect(url_for("weather.index"))
