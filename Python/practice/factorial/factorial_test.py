import pytest
from .factorial_calc import factorial_calculation


@pytest.mark.parametrize('x, expected', [(4, 24), (5, 120), (10, 3628800), (0, 1), (-1, 1)])
def test_factorial_calculation(x, expected):
    """
    Function to test the factorial calculations with different arguments.
    This test function covers various cases including positive integers, zero, and negative integers.
    """
    # Test case for positive integer 4
    assert factorial_calculation(x) == expected, "Test failed for input 4"
    
    # Test case for positive integer 5
    assert factorial_calculation(x) == expected, "Test failed for input 5"
    
    # Test case for positive integer 10
    assert factorial_calculation(x) == expected, "Test failed for input 10"
    
    # Test case for 0
    assert factorial_calculation(x) == expected, "Test failed for input 0"

    # Test case for negative number
    assert factorial_calculation(x) == expected, "Test failed for input -1"


    
