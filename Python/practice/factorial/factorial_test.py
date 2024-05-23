import pytest
from Python.practice.factorial.factorial_calc import factorial_calculation


def test_factorial_calculation():
    """
    Function to test the factorial calculations with different arguments.
    This test function covers various cases including positive integers, zero, and negative integers.
    """
    # Test case for positive integer 4
    assert factorial_calculation(4) == 24, "Test failed for input 4"
    
    # Test case for positive integer 5
    assert factorial_calculation(5) == 120, "Test failed for input 5"
    
    # Test case for positive integer 10
    assert factorial_calculation(10) == 3628800, "Test failed for input 10"
    
    # Test case for 0
    assert factorial_calculation(0) == 1, "Test failed for input 0"
    
    # Test case for negative number
    assert factorial_calculation(-1) == 1, "Test failed for input -1"