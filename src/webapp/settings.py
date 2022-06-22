from os import environ

SECRET_KEY = environ.get("SECRET_KEY")
API_KEY = environ.get("API_KEY")
API_URL = "https://api.openweathermap.org/data/2.5/weather?q=Stuttgart,de&units=metric&APPID={}"
