import pytest
import re
import torch
import cv2
import os
import numpy as np
from .captcha_reader import preprocess_image, print_text, load_image, save_processed_image, count_execution_time, main 


def test_main():

    # Preparing an enviroment
    input_image_path = "Python/captcha_reader/Images/1.png"
    img = load_image(input_image_path)
    processed_image = "Python/captcha_reader/processed_image.png"

    # Ensure path exists
    assert os.path.exists(input_image_path), "Input image does not exist"

    # Calling the main function for testing
    main()

    # Verify the proceed image
    assert os.path.exists(processed_image), "Output image path does not exist"



# Run the integration test
if __name__ == "__main__":
    pytest.main([__file__])


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


def test_load_image_correct_path():
    result = cv2.imread("Python/captcha_reader/Images/1.png", cv2.IMREAD_GRAYSCALE)

    assert result is not None

    assert len(result.shape) == 2, "Image is not a grayscale image"

    assert result.dtype == np.uint8, "Image is not of type uint8"


    
def test_load_image_invalid_path(capfd):

   result = load_image("Python/captcha_reader/Images/non_existent_image.png")

   out, err = capfd.readouterr()

   assert result is None

   assert out.strip() == "Error raised: check the file path Python/captcha_reader/Images/non_existent_image.png"

def test_thresholding():
    # Create a sample grayscale image (e.g., 10x10 pixels with gradient values)
    image = np.array([[i for i in range(10)] for _ in range(10)], dtype=np.uint8)
    
    # Apply the thresholding function
    _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Check that the output image is binary (only contains 0 and 255)
    unique_values = np.unique(thresh)
    assert len(unique_values) <= 2  # Should only contain 0 and 255
    assert set(unique_values).issubset({0, 255})  # Ensure values are either 0 or 255



def test_denoise_image():
    img = cv2.imread("Python/captcha_reader/Images/3.png", cv2.IMREAD_GRAYSCALE)

    assert img is not None, "Image not loaded"

    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    assert thresh is not None, "Thresholding failed"

    before = calculate_RMS_STD(thresh)

    denoised = cv2.medianBlur(thresh, 3)

    assert denoised is not None, "Denoised Failed"

    after = calculate_RMS_STD(denoised)

    assert before > after, "Denoised didn't reduce the noise"



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

        

def calculate_RMS_STD(input):
    
    if not isinstance(input, torch.Tensor):
        input = torch.tensor(input, dtype=torch.float32)

    psum = input.sum()
    psum_sq = (input ** 2).sum()

    # pixel count
    height, width = input.shape
    count = height * width

    # mean and std
    total_mean = psum / count
    total_var = (psum_sq / count) - (total_mean**2)
    total_std = torch.sqrt(total_var)

    #   output
    print("mean: " + str(total_mean.item()))
    print("std:  " + str(total_std.item()))

    return total_mean, total_std