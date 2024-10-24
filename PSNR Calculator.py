import cv2
import numpy as np
import os

#Calculate MSE
def get_mse(original_image, modified_image):
    original = np.array(original_image)
    modified = np.array(modified_image)
    mse = np.mean((original - modified) ** 2)
    return mse

#Calculate PSNR
def calculate_psnr(original_image, modified_image):
    mse = get_mse(original_image, modified_image)

    #can be 1
    psnr = 10 * np.log10(255.0 ** 2 / mse)
    return psnr


another_image = True
while another_image:
    image_name = input("Enter original Image Name: ")
    image_folder = "Images folder"
    image_path = os.path.join(image_folder, image_name)
    original_image_path = image_path

    modified_image_name = input("Enter modified Image Name: ")
    modified_image_folder = "Output image folder"
    m_image_path = os.path.join(modified_image_folder, modified_image_name)
    modified_image_path = m_image_path

    # Read images using OpenCV
    original_image = cv2.imread(original_image_path, cv2.IMREAD_COLOR)
    modified_image = cv2.imread(modified_image_path, cv2.IMREAD_COLOR)

    # Calculate PSNR
    psnr_value = calculate_psnr(original_image, modified_image)
    print(f"PSNR value is {psnr_value} dB")

    another = input("Would you like to encode another message? y/n: ")
    if another == "n":
        another_image = False
