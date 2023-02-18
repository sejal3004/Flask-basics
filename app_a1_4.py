from flask import *

app = Flask(__name__)

@app.route('/')
def message():
    return render_template('app_a1_4_message.html')

@app.route('/home')
def message1():
    return render_template('app_a1_4_message2.html')

if __name__ == '__main__':

    app.run(debug= False)

