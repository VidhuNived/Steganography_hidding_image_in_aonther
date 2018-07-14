# Steganography_hidding_image_in_aonther_using_python
# LSB_Encoding

Steganography is the hiding of a secret message within an ordinary message and the extraction of it at its destination. In this program we are going to hide (encode) a secret valuable image inside another image via using pixel value manipulations. And later retrieving the secret image back at the receiver end using the corresponding program as well.

The encoding of the secret content is performed using the well acknowledged encryption algorithm, LSB encoding, which is to perform mainpuation to LSB values of the byte, which in this case is the pixel value R,G and B.

JPEG images cannot be used for carrying the message because the hidden content inthe LSB of the image will be lost during compression, thus we must go for some other formats like PNG, where these issue doesnot exist.

The pograms Encoder and Decoder are used to encode and decode secret image into carrier image. Both communicating parties must have the same pair if encoder and decoder program inorder to function properly.

REQUIREMENTS

PIL package of python is neccessay to run the program. The instruction to install PIL is given below:

--->>> pip install pillow

pip is python package installer, it must be install first although its preinstalled in many Linux Distributions.

--->>> sudo apt-get install python-pip


orginal_image is the carrier image.
secret_image is the data to be hidden.
encrypted_image is the carrier image with hidden data, also this is the image which we transmit via network.
