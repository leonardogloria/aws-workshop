from PIL import Image, ImageOps

def make_linear_ramp(white):
    # putpalette expects [r,g,b,r,g,b,...]
    ramp = []
    r, g, b = white
    for i in range(255):
        ramp.extend((r*i/255, g*i/255, b*i/255))
    return ramp

def make_sepia(img):


	# make sepia ramp (tweak color as necessary)
	sepia = make_linear_ramp((255, 240, 192))

	im = Image.open(img)

	# convert to grayscale
	if im.mode != "L":
	    im = im.convert("L")

	# optional: apply contrast enhancement here, e.g.
	im = ImageOps.autocontrast(im)

	# apply sepia palette
	im.putpalette(sepia)

	# convert back to RGB so we can save it as JPEG
	# (alternatively, save it in PNG or similar)
	im = im.convert("RGB")
	 
	im.save(img)


def make_bw(img):
	image_file = Image.open(img) # open colour image
	image_file = image_file.convert('1') # convert image to black and white
	image_file.save(img)
	

