from flask import Flask, request, render_template
from main.db import *
from main.myspider import *
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/joblist/<keyword>', methods=['GET'])
def joblist(keyword):  
    joblist = select_table_job(keyword)
    
    if len(joblist) == 0:
        url = "https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E8%A5%BF%E5%AE%89&isadv=0&isfilter=1&p=1&sf=15001&st=20000&kw="
        get_insert_data(url, keyword)
        joblist = select_table_job(keyword)
        return render_template('joblist.html', joblist=joblist)
    
    return render_template('joblist.html', joblist=joblist)


if __name__ == '__main__':
    app.run("localhost", 8080)