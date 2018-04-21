from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'hello, Ada!'
   

   
if __name__ == '__main__':
    app.run()