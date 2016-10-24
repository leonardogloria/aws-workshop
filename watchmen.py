import schedule
import time
import json
import boto.sqs
from boto.s3.connection import S3Connection
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
	



def download_from_s3(filename):
	conn = S3Connection('bugala', 'bugala')
	mybucket = conn.get_bucket('lgloriaworkshopaws') # Subs
	#bucket_list = mybucket.list()


	#keyString = str("3be00413-1b56-41ad-8224-4d9e7b0fd5bb.jpg")
	key = mybucket.get_key(filename)
	# check if file exists locally, if not: download it
	key.get_contents_to_filename(filename)

	#sepia.make_bw("3be00413-1b56-41ad-8224-4d9e7b0fd5bb.jpg")	

def get_messages_from_sqs():
	conn = boto.sqs.connect_to_region("sa-east-1",aws_access_key_id='bugala',aws_secret_access_key='bugala')
	my_queue = conn.get_queue('images')
	rs = my_queue.get_messages()
	print len(rs)
	for m in rs:

		json_data = json.loads(m.get_body())
		fileName = json_data['filename']
		fileType = json_data['type']
		download_from_s3(fileName)
		print ("Transformando o arquivo: ")
		print (fileName)
		if(fileType == '1'):
			make_sepia(fileName)
		else:
			make_bw(fileName)

		my_queue.delete_message(m)
		#print json_data["imagem"]['fileName']



def job():
	print("Iniciei a execucao")
	get_messages_from_sqs()

schedule.every(20).seconds.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)