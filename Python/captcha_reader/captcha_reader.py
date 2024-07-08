import time
import cv2
import numpy as np
import pytesseract


def main():
    # read file and store it in 'img'
    img = load_image()

    # Sart point of timing
    start_time = time.perf_counter()

    # Preprocess functions for an easier symbol detection
    img = preprocess_image(img)

    #Save processed image to validate it 
    save_processed_image(img)

    # Print symbols from text
    print_text(img)

    # END timimng and counting the total execution time of run
    end_time = time.perf_counter()
    count_execution_time(start_time, end_time)


def get_image_path():
   try:
    return input("Please, prvoide code with a path to the image: ")
   except:
       ValueError

def preprocess_image(image):
    # Apply thresholding
    _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Denoise
    denoised = cv2.medianBlur(thresh, 3)
    
    # Dilation and erosion to remove noise
    kernel = np.ones((1, 1), np.uint8)
    dilated = cv2.dilate(denoised, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)
    
    return eroded


def print_text(image):
    custom_config = r'--oem 3 --psm 6 -l eng'
    print(pytesseract.image_to_string(image, config=custom_config))


def load_image():
    image_path = get_image_path()
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check that image read correctly
    if img is None:
        print(f"Error: Image not loaded. Check the file path: {image_path}")
        exit(1)
    else:
        return img
    

def save_processed_image(image):
    print("Image write:", "Succedded" if cv2.imwrite('Python/captcha_reader/processed_image.png', image) else "Failed")
    

def count_execution_time(start_time, end_time):
    print(f"Execution time: {end_time - start_time:.8f} seconds")


if __name__ == "__main__":
    main()
