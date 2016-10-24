import schedule
import time

def job():
	print("Helo Wolrd ")

schedule.every(1).seconds.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)