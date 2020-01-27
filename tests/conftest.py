import pytest

from app import create_app


@pytest.fixture
def client():
    flask_app = create_app()
    flask_app['DEBUG'] = True
    flask_app['TESTING'] = True
    with flask_app.test_client() as c:
        yield c
