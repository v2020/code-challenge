from typing import List, Optional, Union

from flask import render_template


class Field:
    def __init__(self, name) -> None:
        self._name = name
        self._value = ""

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def get_context(self, **kwargs):
        return {"name": self.name, "value": self.value}

    @property
    def render(self):
        context = self.get_context()
        return render_template(self.field_template, **context)


class HiddenField(Field):
    field_template = "fields/hidden.html"


class SelectField(Field):
    field_template = "fields/select.html"

    def __init__(self, name, options) -> None:
        super().__init__(name)
        self._options = options

    @property
    def options(self):
        return self._options

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value in self.options:
            self._value = value

    def get_context(self, **kwargs):
        context = super().get_context(**kwargs)
        context.update({"options": self.options})
        return context


class BaseForm:
    def __init__(self, request) -> None:
        self._fields: Union[List, List[Field]] = []
        self.request = request

    def add_field(self, field):
        request_value = self.request.args.get(field.name, None)
        if request_value:
            field.value = request_value
        self._fields.append(field)

    def get_data(self):
        return {i.name: i.value for i in self._fields}

    def get_filled_data(self):
        return {i.name: i.value for i in self._fields if i.value}

    def setup(self):
        raise NotImplementedError()

    @property
    def fields(self):
        return self._fields


class FilterForm(BaseForm):
    pass
