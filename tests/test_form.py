from project.utils import HiddenField, SelectField


def test_field_hidden():
    name = "test"
    value = "test value"
    field = HiddenField(name)
    field.value = value
    assert field.name == name
    assert field.value == value


def test_field_select():
    name = "test"
    value = "test value"
    options = ["1", "2", "test value"]
    field = SelectField(name, options)
    field.value = value
    assert field.name == name
    assert field.value == value
    assert field.options == options
