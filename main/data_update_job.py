# -*-coding:utf-8-*-  
from myspider import *

def run_update_job_data():
	print "run_update_job_data is running"
	schedule.every().day.at("23:00").do(update_job_data_thread)
	#schedule.every().day.at("23:00").do(update_job_data)
	while True:
	    schedule.run_pending()
	    time.sleep(1)	


run_update_job_data()
  
#threading.Timer(1, update_job_data).start() 
	





