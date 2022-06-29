from webapp import init_app
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv(".env")
    app = init_app("settings.py")
    app.run(debug=True)
