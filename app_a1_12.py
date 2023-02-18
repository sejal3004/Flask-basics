from flask import *   
app = Flask(__name__)


@app.route('/home/<int:age>')
def message(age):
    return '<h1>Age is %d'%age

@app.route('/home1/<text>/<int:age>')
def message1(text, age):
    return f'<h1>Text is {text} and age is {age}</h1>'


if __name__ == '__main__':

    app.run(debug= False)  