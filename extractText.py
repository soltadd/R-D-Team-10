from PIL import Image
import os

def extract_message(imagePath):
    img = Image.open(imagePath)
    pixels = img.load()

    width, height = img.size

    char_bits = ""
    message = ""

    # Loop through each pixel
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]

            # Determine if the image is grayscale (1 channel), RGB (3 channels), or RGBA (4 channels)
            if len(pixel) == 4:  # RGBA
                r, g, b, a = pixel
                colors = (r, g, b)  # Only modify RGB values, not alpha (a)
            elif len(pixel) == 3:  # RGB
                r, g, b = pixel
                colors = (r, g, b)
            elif len(pixel) == 1:  # Grayscale (PGM)
                g = pixel[0]
                colors = (g,)

            # Extract the LSB from each color channel
            for color in colors:
                char_bits += str(color & 1)

                # After collecting 8 bits, convert them into a character
                if len(char_bits) == 8:
                    char = chr(int(char_bits, 2))
                    message += char

                    # Clear the bits for the next character
                    char_bits = ""

                    # Stop extraction if the custom delimiter "####END####" is found
                    if "####END####" in message:
                        # Remove the delimiter and return the extracted message
                        return message.replace("####END####", "")

    return message

#list images
def list_images(folder):
    images = [f for f in os.listdir(folder)]
    return images


open_another = True
while open_another:
    # Display image names in Output image folder
    output_image_folder = "Output image folder"
    images_in_folder = list_images(output_image_folder)
    for img in images_in_folder:
        print(f" - {img}")

    # Input image path
    print("\n")
    image_name = input("Please enter image name: ")
    image_folder = "Output image folder"
    image_path = os.path.join(image_folder, image_name)
    message = extract_message(image_path)

    # Output the hidden message to a text file
    output_file_path = input("Please enter name of output text file: ")
    with open(output_file_path, "w", encoding="utf-8-sig") as file:
        file.write(message)

    another = input("Would you like to encode another message? y/n: ")
    if another == "n":
        open_another = False
