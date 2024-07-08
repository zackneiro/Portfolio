import os, time
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pytesseract

def main():
    # Sart point of timing
    start_time = time.perf_counter()

    # read file to and tor it in'img'
    img = cv2.imread('Python/captcha_reader/1.png')

    # Check that image read correctly
    if img is None:
        print(f"Error: Image not loaded. Check the file path: {'Python/captcha_reader/1.png'}")
        return
    
    # Preprocess functions for an easier symbol detection
    img = preprocess_image(img)

    # Print symbols from text
    print_text(img)

    # Save the processed image
    processed_image_path = 'Python/captcha_reader/processed_image.png'
    cv2.imwrite(processed_image_path, img)
    print(f"Processed image saved as {processed_image_path}")

    # Display the processed image for verification
    plt.imshow(img, cmap='gray')
    plt.title('Processed Image')
    plt.show()

    # END timimng and counting the total execution time of run
    end_time  = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.8f} seconds")


def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Denoise
    denoised = cv2.fastNlMeansDenoising(thresh, None, 10, 7, 21)
    
    # Dilation and erosion to remove noise
    kernel = np.ones((1, 1), np.uint8)
    dilated = cv2.dilate(denoised, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)
    
    return eroded

def print_text(boxed_image):
    custom_config = r'--oem 3 --psm 6 -l eng'
    print(pytesseract.image_to_string(boxed_image, config=custom_config))

if __name__ == "__main__":
    main()
