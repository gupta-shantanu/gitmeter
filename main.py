from flask import Flask,request,send_file
from imageGenerator import gitinfo,createNew
from io import BytesIO as byte
app = Flask(__name__)

@app.route('/')
def blank():
    return '<h1>Want Some Badges? Nope not here........ :p</h1>'


@app.route('/<user>/<repo>/logo.jpg', methods=['GET'])
def getBadge(user,repo):
    ob=gitinfo.repository(user,repo)
    ob.fetch(request.args)
    image=createNew.createNew(ob.repData)
    

    return send_file(byte(image),mimetype='image/jpeg')
    
@app.route('/<name>.png')
def test(name):
    return app.send_static_file('a.png')



if __name__ == '__main__':
    app.debug=True
    app.run('0.0.0.0',port=33507)
#https://api.github.com/repos/gupta-shantanu/macroflash-smashit/stats/commit_activity
