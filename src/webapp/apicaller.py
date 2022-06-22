import urllib.request, json

from flask import current_app


def getWeather(app):
    app.logger.warning("API CAll")
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
