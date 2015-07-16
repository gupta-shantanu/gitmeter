from flask import Flask,send_from_directory
from PIL import Image,ImageDraw
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Worldy!'

@app.route('/s/<name>.png')
def nam(name):
    return app.send_static_file('a.png')



if __name__ == '__main__':
    app.debug=False
    app.run(host='0.0.0.0',port=33507)
