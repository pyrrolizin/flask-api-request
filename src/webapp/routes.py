"""Main blueprint for routing"""

from flask import (
    Blueprint,
    render_template,
    current_app,
)

from . import apicaller

from .cache import cache

bp = Blueprint("bp", __name__)


@bp.route("/")
@cache.cached()
def home():
    """Homepage ("/")

    Renders the template home.j2 and adds the output from the api helper function.

    Returns:
        home.j2
    """
    current_weather = apicaller.getWeather(current_app)
    return render_template("home.j2", current_weather=current_weather)
