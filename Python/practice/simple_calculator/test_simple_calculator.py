import pytest
from Python.practice.simple_calculator.simple_calculator import perform_operation

def test_addition():
    assert perform_operation('+', 5, 3) == "5 + 3 = 8"

def test_subtraction():
    assert perform_operation('-', 5, 3) == "5 - 3 = 2"

def test_multiplication():
    assert perform_operation('*', 5, 3) == "5 * 3 = 15"

def test_division():
    assert perform_operation('/', 6, 3) == "6 / 3 = 2.0"
    assert perform_operation('/', 5, 0) == "Division by zero is not allowed"

def test_modulus():
    assert perform_operation('%', 5, 3) == "5 % 3 = 2"
    assert perform_operation('%', 5, 0) == "Division by zero is not allowed"

def test_floor_division():
    assert perform_operation('//', 5, 3) == "5 // 3 = 1"
    assert perform_operation('//', 5, 0) == "Division by zero is not allowed"
