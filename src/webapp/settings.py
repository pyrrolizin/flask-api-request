"""Settings file for development / production"""

from os import environ

#: flask secret key for (future) session handling
SECRET_KEY = environ.get("SECRET_KEY")

#: API-Key for Openweathermap
API_KEY = environ.get("API_KEY")

#: Link to the openweathernet-API with city name.
#: Template-String: {} will be replaced with API-Key. """
API_URL = "https://api.openweathermap.org/data/2.5/weather?q=Stuttgart,de&units=metric&APPID={}"
