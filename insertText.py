from PIL import Image

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
    binary_message = message_binary(message) + '00000000'

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

#input
image_path = "inputImage.png"
output_path = "outputImage.png"
message = "I am a hidden message"

encode_message(image_path, output_path, message)

