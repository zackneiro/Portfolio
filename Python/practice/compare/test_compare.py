import pytest
from Python.practice.compare.compare import is_even_or_odd

def test_even_or_odd():
    assert is_even_or_odd(4, 7) == "4 is even and 7 is odd"
    assert is_even_or_odd(2, 2) == "2 is even and 2 is even"
    assert is_even_or_odd(1, 5) == "1 is odd and 5 is odd"