"""API caller helper module"""

import urllib.request
import json
from flask import current_app


def getWeather(app):
    """Example API caller.
    request the current weather from Openweathermap

    To mock the API set API_URL to "MOCK". returns str: "sunny - 23 °C"

    Args:
        app (Flask): current flask app

    Returns:
        str: current weather description - temperature °C
    """
    app.logger.info("API Call")
    API_KEY = app.config["API_KEY"]
    API_URL = app.config["API_URL"]
    if API_URL == "MOCK":
        return "sunny - 23 °C"
    url = API_URL.format(API_KEY)
    response = urllib.request.urlopen(url)
    data = response.read()

    jsonObj = json.loads(data)

    current_weather = "{condition} - {temp:.1f} °C".format(
        condition=jsonObj["weather"][0]["description"], temp=jsonObj["main"]["temp"]
    )
    return current_weather
