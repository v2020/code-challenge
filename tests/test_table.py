from project.utils.table import Column


def test_column_without_sort():
    column_item = Column("impact", None, None)
    assert column_item.is_active() == False


def test_column_sort():
    column_item = Column("impact", "impact", None)
    assert column_item.is_active() == True
    assert column_item.is_up() == True


def test_column_sort_reverse():
    column_item = Column("impact", "-impact", None)
    assert column_item.is_active() == True
    assert column_item.is_up() == False


def test_column_name_title():
    column_item = Column("last_detected_at", "-impact", None)
    assert column_item.name == "Last Detected At"
