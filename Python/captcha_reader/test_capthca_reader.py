import pytest
import time
from captcha_reader import preprocess_image, print_text, load_image, save_processed_image, count_execution_time

def test_count_execution_time():
    assert count_execution_time(3280.60102784, 3282.509321012) == "Execution time: 1.90829317 seconds"
    assert count_execution_time(3350.11232500, 3351.41737203) == "Execution time: 1.30504703 seconds" 
    assert count_execution_time(3357.87964458, 3358.91290679) == "Execution time: 1.03326221 seconds"
    assert count_execution_time(3360.47498972, 3361.72458960) == "Execution time: 1.24959988 seconds"