
"""
BEGIN

IMPORT pytesseract, opencv-python,
matplotlib

PREPROCESSING OF THE IMAGE

Load the image and save it in the buffer
so I can work with that.
work with a img = imread(file_name, cv.IMREAD_GRAYSCALE)
    Read an image with (function) that
    save the file to a buffer
Check that image was read sucsesfull with assert statement.
assert img is not None, "file could not be read, check with os.path.exists()"

Next, I need to take all colors off,
so it is easier to read a symbols from
image

ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

TEXT LOCALIZATION


CHARACTER SEGMENTATION
I will go with pytesseract

CHARACTER RECONGNITION

POST PROCESSING


END
"""
import pytesseract, cv2, os
import matplotlib.pyplot as plt
import numpy as np


def main():

   # Print the current working directory
    print("Current working directory:", os.getcwd())

    # List files in the current directory
    print("Files in the current directory:", os.listdir())
 
    img = cv2.imread('25egp.png')

    # Checks if the image is loaded correctly
    if img is None:
        print("Error: Image not loaded. Check the file path.")
    else:
        print("Image loaded successfully.")

    img = get_grayscale(img)
    img = noise_removal(img)
    img = thresholding(img)


    # Save the processed image
    processed_image_path = 'processed_image.png'
    cv2.imwrite(processed_image_path, img)
    print(f"Processed image saved as {processed_image_path}")


    # Display the processed image for veritification
    plt.imshow(img, cmap='gray')
    plt.title('Processed Image')
    plt.show()


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
# noise removal
def noise_removal(image):
    return cv2.medianBlur(image,5)

# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]



if __name__ == "__main__":
    main()