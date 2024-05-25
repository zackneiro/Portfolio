import subprocess
import os

def test_compare_script_execution(monkeypatch):
    """
    Test the execution of the compare script as a standalone program.
    """
    # Test the script using environment variables to simulate input
    monkeypatch.setenv('TESTING', 'true')
    monkeypatch.setenv('INPUT1', '4')
    monkeypatch.setenv('INPUT2', '7')

    result = subprocess.run(['python', 'Python/practice/compare/compare.py'], capture_output=True, text=True)

    # Check the output
    assert "Starting the compare script..." in result.stdout
    assert "4 is even and 7 is odd" in result.stdout
    assert result.returncode == 0
