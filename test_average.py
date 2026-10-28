import pytest
from average import average


def test_average_of_integers():
    assert average([1, 2, 3]) == 2


def test_average_of_floats():
    assert average([1.5, 2.5]) == 2.0


def test_average_single_value():
    assert average([5]) == 5


def test_average_empty_list_raises():
    with pytest.raises(ValueError):
        average([])