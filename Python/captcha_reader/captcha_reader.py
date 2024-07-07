import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("Current working directory:", os.getcwd())
    print("Files in the current directory:", os.listdir())

    # Correct image path
    img = cv2.imread('Python/captcha_reader/25egp.png')

    if img is None:
        print(f"Error: Image not loaded. Check the file path: {'Python/captcha_reader/25egp.png'}")
        return

    img = get_grayscale(img)
    img = noise_removal(img)
    img = thresholding(img)

    # Save the processed image
    processed_image_path = 'Python/captcha_reader/processed_image.png'
    cv2.imwrite(processed_image_path, img)
    print(f"Processed image saved as {processed_image_path}")

    # Display the processed image for verification
    plt.imshow(img, cmap='gray')
    plt.title('Processed Image')
    plt.show()

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
