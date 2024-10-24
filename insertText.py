from PIL import Image

def remove_non_ascii(text):
    return ''.join(char for char in text if ord(char) <= 127)


#Convert message to binary
def message_binary(message):
    #Go through each character in string, convert to ASCII, and then format it into binary
    #Join all binary bits with ''. No whitespace
    binary = ''.join(format(ord(char), '08b') for char in message)
    return binary

# Modify LSB of pixel
def modify_pixel(pixel, bit):
    r, g, b, Irr = pixel
    r = (r & ~1) | int(bit[0])
    g = (g & ~1) | int(bit[1])
    b = (b & ~1) | int(bit[2])
    return (r, g, b, Irr)

#Encode message
def encode_message(image, output, message):
    #Get image
    img = Image.open(image)
    pixels = img.load()

    # Convert message to binary
    ascii_message = remove_non_ascii(message)

    delimiter = message_binary("####END####")
    binary_message = message_binary(ascii_message) + delimiter

    binary_index = 0
    width, height = img.size

    # Starting from first pixel, insert message
    for y in range(height):
        for x in range(width):
            if binary_index < len(binary_message):
                pixel = pixels[x, y]
                # Take 3 bits from the binary text
                bit_chunk = binary_message[binary_index:binary_index + 3].ljust(3, '0')
                # Modify the pixel's RGB values
                new_pixel = modify_pixel(pixel, bit_chunk)
                pixels[x, y] = new_pixel
                binary_index += 3

    # Save the modified image
    img.save(output)


#Get user input for image being used and file
#input
image_path = input("Please enter image name: ")
output_path = "outputImage.png"

text_file = input("Please enter text file: ")

with open(text_file, "r", encoding="utf-8-sig") as file:
    message = file.read()

encode_message(image_path, output_path, message)
