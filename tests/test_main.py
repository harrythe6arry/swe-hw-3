import pytest

from src.leetcode.main import fibonacci, is_palindrome


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("", True),
        ("A man, a plan, a canal: Panama", True),
        ("racecar", True),
        ("hello", False),
        ("12321", True),
    ],
)
def test_is_palindrome(input_str, expected):
    assert is_palindrome(input_str) == expected


def test_fibonacci_valid():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55


def test_fibonacci_invalid():
    with pytest.raises(ValueError):
        fibonacci(-1)
