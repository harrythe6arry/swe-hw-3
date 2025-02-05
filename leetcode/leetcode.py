def is_palindrome(s: str) -> bool:
    cleaned_str = clean_string(s)
    return cleaned_str == reverse_string(cleaned_str)


def clean_string(s: str) -> str:
    return "".join(c.lower() for c in s if c.isalnum())


def reverse_string(s: str) -> str:
    return s[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
