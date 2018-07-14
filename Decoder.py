from PIL import Image

# Creating a image object
enc_img = Image.open('encrypted_image.png')

# Loading pixel values of encoded image, each entry is pixel value ie., RGB values as sublist
enc_pix = enc_img.load()

# First is uesd to store the lenght of image in its R & G pixels
rows = enc_pix[0,0]
size1 = rows[0]*255+rows[1]

# Second is uesd to store the width of image in its R & G pixels
rows = enc_pix[0,1]
size2 = rows[0]*255+rows[1]
size=(size1,size2)

# Recreating hidden image object with its saved dimensions
sec_img = Image.new(enc_img.mode,size)
sec_pix = sec_img.load()

# We follow LSB Encoding with Bit size 's'
s=4

# Traversing through the pixel values
for row in range(size1-1):
    for col in range(size2-1):

	# Performing LSB Decoding
        enc_rgb = enc_pix[row+1,col+1]
        red   = (enc_rgb[0] % s) * 255 / s
        green = (enc_rgb[1] % s) * 255 / s
        blue  = (enc_rgb[2] % s) * 255 / s
	sec_pix[row,col] = (red,green,blue)

# Display the image
sec_img.show()

# Saving the image          
sec_img.save('hidden_image.jpg')

# CLosing the image objects
sec_img.close()
enc_img.close()
