import pytest
from project.app import create_app
from project.utils import DashboardUtils, VulnerabilityDataJson


@pytest.fixture()
def client():
    """test client"""
    flask_app = create_app()
    with flask_app.test_client() as client:
        with flask_app.app_context():
            yield client


@pytest.fixture()
def dashboard_utils():
    """DashboardUtils test"""
    return DashboardUtils(VulnerabilityDataJson("tests/data/test_data.json"))


@pytest.fixture()
def vdata():
    """VulnerabilityDataJson test"""
    return VulnerabilityDataJson("tests/data/test_data.json")
