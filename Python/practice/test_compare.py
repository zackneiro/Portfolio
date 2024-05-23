import pytest
from Python.practice.compare import is_even_or_odd

def test_even_or_odd():
    assert is_even_or_odd(4, 7) == "4 is even and 7 is odd"
    assert is_even_or_odd(1, 1) == "1 is even and 1 is odd"
    assert is_even_or_odd(3, 6) == "3 is odd and 6 is even"