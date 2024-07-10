import time
import cv2
import numpy as np
import pytesseract


def main():
    # Sart point of timing
    start_time = time.perf_counter()
    print(f"{start_time:.8f}")
    

    # read file to and store it in'img'
    path = "Python/captcha_reader/Images/3.png"
    img = load_image(path)

    # Preprocess functions for an easier symbol detection
    img = preprocess_image(img)

    #Save processed image to validate it 
    save_processed_image(img)

    # Print symbols from text
    print_text(img)

    # END timimng and counting the total execution time of run
    end_time = time.perf_counter()
    print(f"{end_time:.8f}")

    count_execution_time(start_time, end_time)


def preprocess_image(image):
    # Apply thresholding
    _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Denoise
    denoised = cv2.medianBlur(thresh, 1)
    
    # Dilation and erosion to remove noise
    kernel = np.ones((1, 1), np.uint8)
    dilated = cv2.dilate(denoised, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)
    
    return eroded


def print_text(image):
    custom_config = r'--oem 3 --psm 6 -l eng'
    text = pytesseract.image_to_string(image, config=custom_config)
    print(text)
    return text


def load_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Check that image read correctly
    if img is None:
        result = None
        print(f"Error raised: check the file path {path}")
        return result
    else:
        return img
    

def save_processed_image(image):
    print("Image write:", "Succedded" if cv2.imwrite('Python/captcha_reader/processed_image.png', image) else "Failed")
    return image
    

def count_execution_time(start_time, end_time):
    execution_time = end_time - start_time
    result = f"Execution time: {execution_time:.8f} seconds"
    print(result)
    return result



if __name__ == "__main__":
    main()
