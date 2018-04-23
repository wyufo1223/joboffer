# -*-coding:utf-8-*-  
import requests
from bs4 import BeautifulSoup
from lxml import html
from db import *

import schedule
import time	
import threading

job_list = []
param_dict = {}

def get_page(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "lxml")	
	return soup

def get_links(url):
	soup = get_page(url)
	links_td = soup.find_all('td', class_='zwmc')
	links = [td.div.a.get('href') for td in links_td]
	return links

def get_param(url, param_name):
	values = url.split('?' )[- 1 ]
	for  key_value  in  values.split( '&' ):
		#print key_value.split( '=' )
		#print key_value
		param_dict[key_value[ : key_value.find('=')]] = key_value[key_value.find('=') + 1 :]
	return param_dict
	
def get_jobinfo(url, job_list):
 	#kw = dict['kw']
	#job_list.append(kw)
	soup = get_page(url)
	offer_ul = soup.find_all('ul', class_="terminal-ul clearfix")[0].text.replace(u'\xa0', u'')
	offer_list = offer_ul.split('\n')
	#print offer_list
	for v in offer_list:
		if(v != u''):
			job_list.append(v[v.find(u'\uff1a') + 1:])
			#print v[v.find(u'\uff1a') + 1:]
			
def get_jobdemand(url):
	soup = get_page(url)
	demand_div = soup.find_all('div', class_="tab-inner-cont")[0].text.replace(u'\xa0', u'')
	return demand_div.strip()

#url = "https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E8%A5%BF%E5%AE%89&isadv=0&isfilter=1&p=1&sf=15001&st=20000&kw=java"

#url = "http://jobs.zhaopin.com/120185013250818.htm?ssidkey=y&ss=409&ff=03&sg=d964874b2a0d46f290547ed3a894a789&so=1"


def get_insert_data(url, keyword):
	url = url + keyword
	links = get_links(url)
	#dict = get_param(url, 'kw')
	
	for link in links:
		job_list = []
		job_list.append(keyword)
		jobinfo = get_jobinfo(link, job_list)
		jobdemand = get_jobdemand(link)
		job_list.append(jobdemand)
		insert_table_job(job_list)

def update_job_data():
	url = "https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E8%A5%BF%E5%AE%89&isadv=0&isfilter=1&p=1&sf=15001&st=20000&kw="
	keywords = select_distinct_keyword()
	for k in keywords:
		delete_job(k)
		get_insert_data(url, k[0])
		time.sleep(1)
	print "update_job_data is running"	
		
def update_job_data_thread():
    threading.Thread(target=update_job_data).start()
    print "update_job_data_thread is running"


def run_update_job_data():
	print "run_update_job_data is running"
	schedule.every().day.at("22:56").do(update_job_data_thread)
	while True:
	    schedule.run_pending()
	    time.sleep(1)
	


run_update_job_data()
  
#threading.Timer(1, update_job_data).start()  
 		

	





