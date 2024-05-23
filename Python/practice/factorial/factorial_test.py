import pytest
from Python.practice.factorial.factorial_calc import factorial_calculation

def test_factorial_calculation():
    assert factorial_calculation(4) == 4
    assert factorial_calculation(5) == 120
    assert factorial_calculation(10) == 3628800
    assert factorial_calculation(0) == 1 # test case for 0
    assert factorial_calculation(-1) == 1 # test case for negative number