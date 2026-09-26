import pytest

from fibonacci_kata.core import fibonacci


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (10, 55),
        (20, 6765),
    ],
)
def test_fibonacci_contract(n, expected):
    assert fibonacci(n) == expected


def test_fibonacci_rejects_negative_input():
    with pytest.raises(ValueError):
        fibonacci(-1)
    with pytest.raises(ValueError):
        fibonacci(-10)
