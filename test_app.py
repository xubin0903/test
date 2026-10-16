import pytest

from app import add, divide


def test_add_normal_values():
    assert add(2, 3) == 5
    assert add(0, 0) == 0


def test_add_negative_numbers():
    assert add(-1, -2) == -3
    assert add(-5, 3) == -2


def test_divide_normal_values():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="b must not be zero"):
        divide(1, 0)


def test_divide_negative_numbers():
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    assert divide(-10, -2) == 5
