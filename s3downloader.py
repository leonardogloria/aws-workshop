from boto.s3.connection import S3Connection
import sepia

conn = S3Connection('bugala', 'bugala')
mybucket = conn.get_bucket('lgloriaworkshopaws') # Subs
#bucket_list = mybucket.list()


	#keyString = str("3be00413-1b56-41ad-8224-4d9e7b0fd5bb.jpg")
key = mybucket.get_key("3be00413-1b56-41ad-8224-4d9e7b0fd5bb.jpg")
	# check if file exists locally, if not: download it
key.get_contents_to_filename("3be00413-1b56-41ad-8224-4d9e7b0fd5bb.jpg")

sepia.make_bw("3be00413-1b56-41ad-8224-4d9e7b0fd5bb.jpg")

