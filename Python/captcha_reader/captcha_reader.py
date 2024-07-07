import os, time
import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Sart point of timing
    start_time = time.perf_counter()

    # read file to and tor it in'img'
    img = cv2.imread('Python/captcha_reader/25egp.png')


    # Check that image read correctly
    if img is None:
        print(f"Error: Image not loaded. Check the file path: {'Python/captcha_reader/25egp.png'}")
        return
    
    # Preprocess functions for an easier symbol detection
    img = get_grayscale(img) 
    img = thresholding(img)


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

if __name__ == "__main__":
    main()
