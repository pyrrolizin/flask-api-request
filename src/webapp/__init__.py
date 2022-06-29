"""This project is a starting platform for a SSR (Server Side Rendered) Flask
project that pulls data from an external API and caches the result.
The project includes a responsive Jinia2 template with Bootstrap.

main flask application"""

from flask import Flask
import secrets

from .cache import cache


def init_app(config):
    """Generates a new aaplication instatance and loads the corresponding
    settings file.

    Args:
        config (string): filename. `settings.py` or `settings_testing.py`

    Raises:
        Exception: missing API_KEY. Please provice API_KEy with environment
                   variable or .env

    Returns:
        Flask: Flask application
    """

    app = Flask(__name__)
    app.config.from_pyfile(config)

    # init apps for middleware
    # e.g. db.init_app(app)
    cache.init_app(
        app, config={"CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 300}
    )

    with app.app_context():
        if app.config["SECRET_KEY"] == "" or app.config["SECRET_KEY"] is None:
            app.logger.warning("SECRET_KEY missing. Creating a random SECRET_KEY")
            app.config["SECRET_KEY"] = secrets.token_hex()

        if app.config["API_KEY"] == "" or app.config["API_KEY"] is None:
            app.logger.error("API_KEY missing. exiting.")
            raise Exception("API_KEY missing. exiting.")

        # Include Routes
        from webapp.routes import bp as main_bp

        # Register Blueprints
        app.register_blueprint(main_bp)

    return app
