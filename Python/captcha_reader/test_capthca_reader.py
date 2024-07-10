import pytest
import re
from .captcha_reader import preprocess_image, print_text, load_image, save_processed_image, count_execution_time

def test_count_execution_time():
    assert count_execution_time(3280.60102784, 3282.509321012) == "Execution time: 1.90829317 seconds"
    assert count_execution_time(3350.11232500, 3351.41737203) == "Execution time: 1.30504703 seconds" 
    assert count_execution_time(3357.87964458, 3358.91290679) == "Execution time: 1.03326221 seconds"
    assert count_execution_time(3360.47498972, 3361.72458960) == "Execution time: 1.24959988 seconds"

def test_preprocess_image():
    img = load_image("Python/captcha_reader/Images/1.png")
    processed_img = preprocess_image(img)
    assert processed_img is not None
    assert processed_img.shape == img.shape
    saved_image = save_processed_image(processed_img)
    assert saved_image.shape == processed_img.shape

def test_save_processed_image():
    img = load_image("Python/captcha_reader/Images/1.png")
    processed_img = preprocess_image(img)
    assert processed_img is not None
    assert processed_img.shape == img.shape
    saved_image = save_processed_image(processed_img)
    assert saved_image.shape == processed_img.shape





def clean_text(text):
    # Replace curly quotes with straight quotes
    text = text.replace("“", "\"").replace("”", "\"")
    text = text.replace("‘", "'").replace("’", "'")
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove all non-alphanumeric characters except spaces
    text = re.sub(r'[^a-z0-9\s]', '', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', '', text).strip()
    
    return text

def test_print_text():
    img = load_image("Python/captcha_reader/Images/1.png")
    processed_img = preprocess_image(img)
    result = print_text(processed_img)
    
    expected_text = """That "page of text" assumption is so incredibly important. If you're OCR'ing a
    scanned chapter from a book, the default Tesseract PSM may work well for you. But
    if you're trying to OCR only a single line, a single word, or maybe even a single
    character, then this default mode will result in either an empty string or nonsensical
    results."""
    
    # Print full OCR result for inspection
    print("Full OCR Result:")
    print(result)
    
    cleaned_result = clean_text(result)
    cleaned_expected = clean_text(expected_text)
    
    print("Cleaned OCR Result:")
    print(cleaned_result)
    
    assert cleaned_result == cleaned_expected, f"OCR result doesn't match expected text.\nExpected: {cleaned_expected}\nGot: {cleaned_result}"
