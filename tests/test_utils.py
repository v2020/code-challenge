import pytest
from project.utils import CountBox


def test_count():
    output = CountBox("3.0-medium", 98)
    assert output.label == "Medium"
    assert output.css_class == "medium"
    assert output.count == 98


def test_count_raises_value():
    with pytest.raises(ValueError):
        output = CountBox("3.0-high", 98)


def test_utils_statistic(dashboard_utils):
    output = dashboard_utils.get_statistic_by_name("impact")
    assert output == {"2.0-low": 1, "3.0-medium": 1}


def test_utils_statistic_key_error(dashboard_utils):
    with pytest.raises(KeyError):
        output = dashboard_utils.get_statistic_by_name("test")


def test_utils_get_item(vdata):
    output = vdata.get_item("28f9f088e5d50baad9b53d130d9301e2586ca085")
    assert output["_id"] == "28f9f088e5d50baad9b53d130d9301e2586ca085"


def test_utils_get_item_not_found(vdata):
    output = vdata.get_item("18f9f088e5d50baad9b53d130d9301e2586ca085")
    assert output is None
