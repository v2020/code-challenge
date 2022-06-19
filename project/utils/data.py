from .dataload import VulnerabilityDataBase, VulnerabilityDataJson

IMPACT_CRITICAL = "5.0-critical"
IMPACT_HIGH = "4.0-high"
IMPACT_MEDIUM = "3.0-medium"
IMPACT_LOW = "2.0-low"
IMPACT_INFO = "2.0-info"

COUNT_LIST = [IMPACT_CRITICAL, IMPACT_HIGH, IMPACT_MEDIUM, IMPACT_LOW, IMPACT_INFO]


class InfoCount:
    def __init__(self, value, count) -> None:
        if value not in COUNT_LIST:
            raise ValueError(f"Incorrect impact {value}")
        self._value = value
        self._count = count

    @property
    def count(self):
        return self._count

    @property
    def label(self):
        return self._value.split("-")[1].title()

    @property
    def css_class(self):
        return self.label.lower()


class VulnerabilityUtils:
    COLUMNS = [
        "domain",
        "impact",
        "status",
        "category",
        "ipv4_address",
        "port",
        "first_detected_at",
        "last_detected_at",
        "type",
        "host",
    ]

    COUNTS = []

    def __init__(self, vulnerability_data: VulnerabilityDataBase) -> None:
        self.vulnerability_data = vulnerability_data
        self.data = self.vulnerability_data.get_list()

    def get_list(self):
        result_list = []
        for i in self.data:
            item = {j: i[j] for j in self.COLUMNS}
            result_list.append(item)
        return result_list

    def get_item(self, id):
        for i in self.data:
            if i["_id"] == id:
                return i

    def get_statistic_by_name(self, name):
        values = {}
        for i in self.data:
            if i[name] in values:
                values[i[name]] += 1
            else:
                values[i[name]] = 1
        return values

    def get_counts(self):
        impacts = self.get_statistic_by_name("impact")
        return [InfoCount(i, impacts.get(i, 0)) for i in COUNT_LIST]
