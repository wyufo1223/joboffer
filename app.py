from flask import Flask, request, render_template
from main.db import *
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/joblist/<keyword>', methods=['GET'])
def joblist(keyword):  
    joblist = select_table_job(keyword)
    return render_template('joblist.html', joblist=joblist)


if __name__ == '__main__':
    app.run("localhost", 8080)