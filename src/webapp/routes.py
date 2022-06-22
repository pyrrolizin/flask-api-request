from flask import (
    Blueprint,
    render_template,
    url_for,
    flash,
    redirect,
    send_file,
    request,
    current_app,
    send_from_directory,
)

from . import apicaller

from .cache import cache

bp = Blueprint("bp", __name__)


@bp.route("/")
@cache.cached()
def home():
    """Startseite ("/")

    Returns:
        home.j2
    """
    current_weather = apicaller.getWeather(current_app)
    return render_template("home.j2", current_weather=current_weather)
