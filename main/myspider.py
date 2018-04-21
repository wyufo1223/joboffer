# -*-coding:utf-8-*-  
import requests
from bs4 import BeautifulSoup
from lxml import html
from db import *

job_list = [];

def get_page(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "lxml")	
	return soup

def get_links(url):
	soup = get_page(url)
	links_td = soup.find_all('td', class_='zwmc')
	links = [td.div.a.get('href') for td in links_td]
	return links
		
def get_jobinfo(url):
	soup = get_page(url)
	offer_ul = soup.find_all('ul', class_="terminal-ul clearfix")[0].text.replace(u'\xa0', u'')
	offer_list = offer_ul.split('\n')
	#print offer_list
	for v in offer_list:
		if(v != u''):
			job_list.append(v[v.find(u'\uff1a') + 1:])
			print v[v.find(u'\uff1a') + 1:]
			
def get_jobdemand(url):
	soup = get_page(url)
	demand_div = soup.find_all('div', class_="tab-inner-cont")[0].text.replace(u'\xa0', u'')
	return demand_div.strip()

url = "https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E8%A5%BF%E5%AE%89&kw=java&isadv=0&isfilter=1&p=1&sf=15001&st=20000"
links = get_links(url)
#print links

url = "http://jobs.zhaopin.com/120185013250818.htm?ssidkey=y&ss=409&ff=03&sg=d964874b2a0d46f290547ed3a894a789&so=1"
jobinfo = get_jobinfo(url)
jobdemand = get_jobdemand(url)
job_list.append(jobdemand)
print jobdemand

print len(job_list)

#joboffer = [1,2,3,4,5,6,7,8,9]
insert_table_job(job_list)

#cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])




