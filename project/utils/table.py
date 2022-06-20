from typing import Any, Dict, List, Optional, Type, Union

from flask import render_template

from .dataload import VulnerabilityDataBase
from .form import BaseForm, FilterForm, HiddenField, SelectField


class Column:
    """The column table class which helps to generate sortable header"""

    def __init__(
        self, key: str, active_key: str, table_filters: Union[Dict, None]
    ) -> None:
        self._key = key
        # check sort column
        self._active_key = active_key
        self.active = key == self.clean_key(active_key)
        # sort direction
        self.is_up = False
        if self.active and not self._active_key.startswith("-"):
            self.is_up = True

        self.table_filters = table_filters

    @staticmethod
    def clean_key(key):
        if key:
            return key[1:] if key.startswith("-") else key

    @property
    def name(self):
        return self._key.replace("_", " ").title() + " " + self._get_arrow()

    def _get_arrow(self):
        if self.active:
            return "🔼" if self.is_up else "🔽"
        return ""

    @property
    def params(self) -> str:
        """return get parameters for each column
        TODO: Refactoring needs
        Returns:
            str: get parameters
        """
        param = f"?sort={self._key}"
        if self.is_up and self.active:
            # reverse sort
            param = f"?sort=-{self._key}"

        if self.table_filters:
            for i in self.table_filters:
                # save filter form values
                if i != "sort":
                    param += f"&{i}={self.table_filters[i]}"

        return param

    @property
    def key(self):
        return self._key


class TableUtilsBase:
    """The base table class to sort and to filter the data"""

    COLUMNS: List = []
    form_class: Union[Type[BaseForm], None]

    def __init__(
        self,
        vulnerability_data: VulnerabilityDataBase,
        request: Any,
    ) -> None:
        self.vulnerability_data = vulnerability_data
        self.data = self.vulnerability_data.get_list()
        self.request = request
        if self.form_class:
            self.form: BaseForm = self.form_class(request)

    def get_list(self) -> List[Dict]:
        result_list = []
        for i in self.data:
            item = {j: i[j] for j in self.COLUMNS}
            result_list.append(item)
        return result_list

    def check_table_sort_key(self, active_key):
        if Column.clean_key(active_key) not in self.COLUMNS:
            active_key = self.COLUMNS[0]
        return active_key

    def get_table(self, active_key: str) -> List[Dict]:
        form_data: Dict = self.form.get_filled_data()
        result_list = self.get_list()

        # apply filter
        filter_list = []
        for i in result_list:
            add_item = True
            for j in form_data:
                if (j in i) and (form_data[j]):
                    if form_data[j] != i[j]:
                        add_item = False
            if add_item:
                filter_list.append(i)

        # apply sort(active) key
        active_key = self.check_table_sort_key(active_key)
        reverse = bool(active_key.startswith("-"))
        active_key = Column.clean_key(active_key)

        return sorted(filter_list, key=lambda d: d[active_key], reverse=reverse)

    def get_table_header(self, active_key):
        active_key = self.check_table_sort_key(active_key)
        table_filters = self.form.get_filled_data()
        return [Column(key, active_key, table_filters) for key in self.COLUMNS]

    def get_item(self, id) -> Union[Dict[str, Any], None]:
        return next((i for i in self.data if i["_id"] == id), None)

    def get_statistic_by_name(self, name: str) -> Dict[str, int]:
        values: Dict[str, int] = {}
        for i in self.data:
            if i[name] in values:
                values[i[name]] += 1
            else:
                values[i[name]] = 1
        return values

    def get_options_by_name(self, name: str) -> List[str]:
        values: List[str] = []
        for i in self.data:
            if i[name] not in values:
                values.append(i[name])
        return values

    def get_form(self) -> BaseForm:
        return self.form

    def form_setup(self):
        raise NotImplementedError()


class TableUtils(TableUtilsBase):
    """The custom table class with column list and filter names"""

    COLUMNS = [
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

    form_class = FilterForm

    def __init__(self, vulnerability_data: VulnerabilityDataBase, request: Any) -> None:
        super().__init__(vulnerability_data, request)

        if self.form:
            self.form_setup()

    def form_setup(self):
        self.form.add_field(SelectField("impact", self.get_options_by_name("impact")))
        self.form.add_field(
            SelectField("category", self.get_options_by_name("category"))
        )
        self.form.add_field(SelectField("type", self.get_options_by_name("type")))
        self.form.add_field(HiddenField("sort"))
