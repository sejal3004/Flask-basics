from flask import Flask

app = Flask(__name__)


@app.route('/home')
def hello_world():
    return 'Home page'


@app.route('/about_us')
def hello_world1():
    return '<h1> About us  </h1>'


@app.route('/Location')
def hello_world2():
    return '<p>Location page</p>'


@app.route('/Contact_us')
def hello_world3():
    return '<p>Contact us page</p>'



if __name__ == '__main__':

    app.run(debug= False)