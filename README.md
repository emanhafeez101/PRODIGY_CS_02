# PRODIGY_CS_02
The script contains two main functions, encrypt_image and decrypt_image, that perform simple encryption and decryption on an image file by swapping the red and blue channels of each pixel.
Function: encrypt_image
Input Parameters:

input_path: Path to the input image file that needs to be encrypted.
output_path: Path to save the encrypted image.
key: Currently not used but can be used for future encryption methods.
Functionality:

The function opens the input image and loads its pixel data.
It retrieves the dimensions (width and height) of the image.
It loops through each pixel of the image, swaps the red and blue channels (a simple form of encryption), and updates the pixel data.
The modified image is saved to the specified output path.
Function: decrypt_image
Input Parameters:

input_path: Path to the encrypted image file that needs to be decrypted.
output_path: Path to save the decrypted image.
key: Currently not used but can be used for future decryption methods.
Functionality:

The function opens the encrypted image and loads its pixel data.
It retrieves the dimensions (width and height) of the image.
It loops through each pixel of the image, swaps the blue and red channels back to their original positions (a simple form of decryption), and updates the pixel data.
The modified image is saved to the specified output path.
Main Execution
Paths to Images:

input_image: Path to the original image file.
encrypted_image: Path to save the encrypted image.
decrypted_image: Path to save the decrypted image.
Encrypt the Image:

The encrypt_image function is called with the input_image path, the encrypted_image path, and None for the key.
Decrypt the Image:

The decrypt_image function is called with the encrypted_image path, the decrypted_image path, and None for the key.
