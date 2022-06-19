import pytest
from project import create_app


@pytest.fixture()
def client():
    # test client
    flask_app = create_app()
    with flask_app.test_client() as client:
        with flask_app.app_context():
            yield client
