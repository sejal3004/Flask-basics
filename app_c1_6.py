from flask import *  
app = Flask(__name__)  

@app.route('/')  
def customer():  
   return render_template('empform.html')  

@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form  
      return render_template("display.html",result = result)  



if __name__ == '__main__':  
   app.run(debug = False) 

   