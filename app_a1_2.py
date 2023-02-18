from flask import Flask

app = Flask(__name__)


@app.route('/page1')
def hello_world():
    return 'Hello World Flask'


#passing parameters (name)
@app.route('/page2/<name>')
def hello_world1(name):
    return '<h1> Hello %s, how are you?? </h1>'%name


#age
@app.route('/page3/<age>')
def hello_world2(age):
    return '<p>Age is %s</p>'%age


if __name__ == '__main__':

    app.run(debug= False)