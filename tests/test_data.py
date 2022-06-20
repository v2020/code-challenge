import pytest
from project.utils import VulnerabilityDataJson


def test_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        data_load = VulnerabilityDataJson("tests/data/test.json")


def test_data_load_two_items():
    data_load = VulnerabilityDataJson("tests/data/test_data.json")
    assert len(data_load.get_list()) == 2


def test_data_file_empty_json():
    with pytest.raises(Exception):
        data_load = VulnerabilityDataJson("tests/data/test_data_empty.json")
