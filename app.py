from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/joblist', methods=['GET'])
def joblist():
    
    return render_template('joblist.html', joblist=joblist)


if __name__ == '__main__':
    app.run("localhost", 8080)