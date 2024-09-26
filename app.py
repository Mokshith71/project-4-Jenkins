from flask import flask 

app = Flask(__name__)
@app.route('/')
def hello world():
    return 'hello, junkins!'
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)