from src import swe_hw_3


def test_sanity():
    assert 1 + 1 == 2


def test_add():
    assert swe_hw_3.add_numbers(1, 2) == 3
