import pytest
from project import create_app
from project.utils import VulnerabilityDataJson, VulnerabilityUtils


@pytest.fixture()
def client():
    # test client
    flask_app = create_app()
    with flask_app.test_client() as client:
        with flask_app.app_context():
            yield client


@pytest.fixture()
def vdata():
    # VulnerabilityUtils test
    return VulnerabilityUtils(VulnerabilityDataJson("tests/data/test_data.json"))
