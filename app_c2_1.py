from flask import *
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home1.html')

@app.route('/login')
def login():
    return render_template('login1.html')

@app.route('/validate',methods = ['POST', 'GET'])  
def validate():  
   if request.method == 'POST' and request.form['password'] == 'abcd' and request.form['email'] == 'agarwalsejal30@gmail.com' or request.form['password'] == '1234' and request.form['email'] == 'raina.sehgal@gmail.com' or request.form['password'] == '5678' and request.form['email'] == 'aaryamathur25@gmail.com':
    return redirect(url_for('fillform'))
    #return redirect(url_for('login'))
   else:
    abort(401)


#@app.route('/success')
#def success():
 #   return '<h1>Welcome user</h1>'


@app.route('/fillform')  
def fillform():  
   return render_template('fill_form.html')  

@app.route('/success1',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form  
      return render_template("display_form.html",result = result)  




if __name__ == '__main__':
    app.run(debug= False)