from PIL import Image

def extract_message(imagePath):

    img = Image.open(imagePath)
    pixels = img.load()

    width, height = img.size

    binary_message = ""
    char_bits = ""
    message = ""

    for y in range(height):
        for x in range(width):
            r, g, b, irr = pixels[x, y]

            #get lsb from each r,g,b of pixel
            for color in (r, g, b):
                char_bits += str(color & 1)

                #After 8 bits, convert to character
                if len(char_bits) == 8:
                    binary_message += char_bits
                    char = chr(int(char_bits, 2))

                    # Stop if we hit the delimiter (null character '\0')
                    if char == '\0':
                        return message
                    else:
                        message += char

                    char_bits = ""

    return message


imagePath = "outputImage.png"
message = extract_message(imagePath)
print("Hidden Message: ", message)
