from PIL import Image

# Creating a image object
org_img = Image.open('original_image.png')
sec_img = Image.open('secret_image.jpg')

# Creating new image object with image mode and dimensions as that of original image
enc_img = Image.new( org_img.mode, org_img.size)

# Loading pixel values of original image, each entry is pixel value ie., RGB values as sublist
org_pix = org_img.load()
sec_pix = sec_img.load()
enc_pix = enc_img.load()

# First is used to store the lenght of image in its R & G pixels
# Second is used to store the width of image in its R & G pixels
rgb=org_pix[0,0]
width=sec_img.size[0]/255
height=sec_img.size[1]/255
hid_pix[0,0] = (width,sec_img.size[0]%255,rgb[2])
hid_pix[0,1] = (height,sec_img.size[1]%255,rgb[2])

# We follow LSB Encoding with Bit size 's'
s=4

# Traversing through the pixel values
for row in range(org_img.size[0]):
    for col in range(org_img.size[1]):

	# Writng the secret image image as per its dimensions to original image
        if row<sec_img.size[0] and col<sec_img.size[1]:
		
		# Fetching RGB value a pixel to sublist
	        org_rgb=org_pix[row+1,col+1] 
        	sec_rgb=sec_pix[row,col]
		
		# Performing LSB Encoding
		red   = org_rgb[0] - (org_rgb[0] % s) + (s*sec_rgb[0] / 255)
        	green = org_rgb[1] - (org_rgb[1] % s) + (s*sec_rgb[1] / 255)
        	blue  = org_rgb[2] - (org_rgb[2] % s) + (s*sec_rgb[2] / 255)
        	hid_pix[row+1,col+1] = (red,green,blue)
        else:
		# Secret images pixel values are over so we copy that of original image's
		 enc_pix[row,col]=org_pix[row,col]

# Closing the image objects
sec_img.close()
org_img.close()

# Display the image
enc_img.show()     

# Save the image          
enc_img.save("encrypted_image.png") 
enc_img.close()


# This saved encrypted file can the be transmitted on the network, with any third party having no knowledge of the hidden content within the file.
