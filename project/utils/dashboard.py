from re import I
from typing import Any, Dict, List, Optional, Union

from .dataload import VulnerabilityDataBase, VulnerabilityDataJson
from .table import Column, FilterForm, HiddenField, SelectField

IMPACT_CRITICAL = "5.0-critical"
IMPACT_HIGH = "4.0-high"
IMPACT_MEDIUM = "3.0-medium"
IMPACT_LOW = "2.0-low"
IMPACT_INFO = "2.0-info"

COUNT_LIST = [
    IMPACT_CRITICAL,
    IMPACT_HIGH,
    IMPACT_MEDIUM,
    IMPACT_LOW,
    IMPACT_INFO,
]


class CountBox:
    def __init__(self, value: str, count: int) -> None:
        if value not in COUNT_LIST:
            raise ValueError(f"Incorrect impact {value}")
        self._value = value
        self._count = count

    @property
    def count(self):
        return self._count

    @property
    def label(self) -> str:
        return self._value.split("-")[-1].title()

    @property
    def css_class(self) -> str:
        return self.label.lower()


class DashboardUtils:
    def __init__(self, vulnerability_data: VulnerabilityDataBase) -> None:
        self.vulnerability_data = vulnerability_data
        self.data = self.vulnerability_data.get_list()

    def get_statistic_by_name(self, name: str) -> Dict[str, int]:
        values: Dict[str, int] = {}
        for i in self.data:
            if i[name] in values:
                values[i[name]] += 1
            else:
                values[i[name]] = 1
        return values

    def get_counts(self) -> list[CountBox]:
        impacts = self.get_statistic_by_name("impact")
        return [CountBox(i, impacts.get(i, 0)) for i in COUNT_LIST]
