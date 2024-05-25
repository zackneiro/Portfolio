import pytest
from Python.practice.compare.compare import get_input, is_even_or_odd, main
import os

def test_is_even_or_odd():
    """
    Function to test the is_even_or_odd function.
    """
    assert is_even_or_odd(4, 7) == "4 is even and 7 is odd"
    assert is_even_or_odd(2, 2) == "2 is even and 2 is even"
    assert is_even_or_odd(1, 5) == "1 is odd and 5 is odd"

def test_get_input(monkeypatch):
    """
    Function to test the get_input function.
    """
    def mock_input(prompt):
        if "first" in prompt:
            return 4
        elif "second" in prompt:
            return 7
    
    # Mock the input function
    monkeypatch.setattr('builtins.input', mock_input)
    
    # Test the get_input function
    assert get_input() == (4, 7)

@pytest.fixture
def no_env(monkeypatch):
    """
    Fixture to clear environment variables for testing.
    """
    monkeypatch.delenv('CI', raising=False)
    monkeypatch.delenv('INPUT1', raising=False)
    monkeypatch.delenv('INPUT2', raising=False)

def test_get_input_with_env(monkeypatch):
    """
    Test get_input function when CI environment variable is set.
    """
    monkeypatch.setenv('CI', 'true')
    monkeypatch.setenv('INPUT1', '4')
    monkeypatch.setenv('INPUT2', '7')
    assert get_input() == (4, 7)

def test_get_input_without_env(monkeypatch, no_env):
    """
    Test get_input function when CI environment variable is not set.
    """
    def mock_input(prompt):
        if "first" in prompt:
            return 4
        elif "second" in prompt:
            return 7

    monkeypatch.setattr('builtins.input', mock_input)
    assert get_input() == (4, 7)

def test_main(monkeypatch, capsys):
    """
    Test the main function.
    """
    def mock_get_input():
        return (4, 7)

    # Mock get_input to return predefined values
    monkeypatch.setattr('Python.practice.compare.compare.get_input', mock_get_input)
    
    # Call main function
    main()
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Verify the output
    assert "Starting the compare script..." in captured.out
    assert "4 is even and 7 is odd" in captured.out
