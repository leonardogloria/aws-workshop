import boto.sqs

conn = boto.sqs.connect_to_region("sa-east-1",aws_access_key_id='bugala',aws_secret_access_key='bugala')
my_queue = conn.get_queue('images')
rs = my_queue.get_messages()
m = rs[0]
#q.delete_message(m)



print m.get_body()