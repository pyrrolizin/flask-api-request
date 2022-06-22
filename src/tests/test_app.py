from webapp import init_app

import pytest


@pytest.fixture
def client():
    """create TestClient"""
    app = init_app("settings_testing.py")
    app.config["TESTING"] = True

    with app.test_client() as client:
        with app.app_context():
            pass

        yield client

    # Tear down
    pass


def test_homepage(client):
    """Homepage loading - mock data"""
    rv = client.get("/")
    assert b"sunny - 23 " in rv.data


def test_404(client):
    """404 error"""
    rv = client.get("/_not_found")
    assert rv.status_code == 404
