import pytest

from leetcode.leetcode import clean_string, fibonacci, is_palindrome, reverse_string


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
    assert fibonacci(20) == 6765


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("racecar") == "racecar"
    assert reverse_string("12321") == "12321"


def test_clean_string():
    assert (
        clean_string("asdfj dlsa;kf jds sdlkaf jas;ldfj ")
        == "asdfjdlsakfjdssdlkafjasldfj"
    )
    assert clean_string("racecar") == "racecar"
    assert clean_string("12321") == "12321"


def test_fibonacci_invalid():
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_empty_string():
    assert is_palindrome("") == True


def test_negative_number_fib():
    with pytest.raises(ValueError):
        fibonacci(-1)
