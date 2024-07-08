import os, time
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
from pytesseract import Output

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
    img = get_grayscale(img) 
    img = thresholding(img)
    #img = noise_removal(img)
    #img = morphological_transform(img)
    #img = remove_lines(img)
    # Get boxes aroug the characters
    img = get_boxes(img, 'Python/captcha_reader/boxed_image.png')

    # Print symbols from captcha
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


# Get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Noise removal
def noise_removal(image):
    return cv2.medianBlur(image, 5)

# Thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Morphological transformations
def morphological_transform(image):
    kernel = np.ones((2,2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    return image


def get_boxes(image, save_path=None):
    d = pytesseract.image_to_data(image, output_type=Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if save_path is not None:
        saved = cv2.imwrite(save_path, image)
        if saved:
            print(f"Image successfully saved as {save_path}")
        else:
            print(f"Failed to save image as {save_path}")
                  
    return image

# Remove lines
def remove_lines(image):
    # Detect lines in the image using Hough Transform
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    
    if lines is not None:
        for rho, theta in lines[:,0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 0), 2)
    return image

def print_text(boxed_image):
    custom_config = r'-l eng --psm 1 '
    print(pytesseract.image_to_string(boxed_image, config=custom_config))

if __name__ == "__main__":
    main()
