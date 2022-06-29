"""Settings file for pytest"""
import secrets

#: Random flask secret key
SECRET_KEY = secrets.token_hex()

#: Activate mocking of API
API_KEY = "MOCKING"
API_URL = "MOCK"
