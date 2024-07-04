from PIL import Image #PIL (Python Imaging Library)


def encrypt_image(input_path, output_path, key):
    # Open the input image file
    img = Image.open(input_path)
    
    # Load the pixel data of the image
    pixels = img.load()
    
    # Get the width and height of the image
    width, height = img.size
    
    # Loop through each pixel in the image
    for i in range(width):
        for j in range(height):
            # Get the red, green, and blue values of the current pixel
            r, g, b = pixels[i, j]

            # Example encryption: swap the red and blue channels
            encrypted_pixel = (b, g, r)

            # Update the pixel with the encrypted value
            pixels[i, j] = encrypted_pixel
    
    # Save the modified image to the output path
    img.save(output_path)

def decrypt_image(input_path, output_path, key):
    # Open the encrypted image file
    img = Image.open(input_path)
    
    # Load the pixel data of the image
    pixels = img.load()
    
    # Get the width and height of the image
    width, height = img.size

    # Loop through each pixel in the image
    for i in range(width):
        for j in range(height):
            # Get the blue, green, and red values of the current pixel
            # Note that these values were swapped during encryption
            b, g, r = pixels[i, j]

            # Example decryption: swap the blue and red channels back
            decrypted_pixel = (r, g, b)

            # Update the pixel with the decrypted value
            pixels[i, j] = decrypted_pixel
    
    # Save the modified image to the output path
    img.save(output_path)

input_image = r"C:\Users\ALLI\Downloads\download.jpeg"
encypted_image =r"C:\Users\ALLI\Downloads\encrypt.jpeg"
decrypted_image =r"C:\Users\ALLI\Downloads\decrypt.jpeg"
encrypt_image(input_image, encrypt_image, key=None)

decrypt_image(input_image , decrypted_image , key=None)
