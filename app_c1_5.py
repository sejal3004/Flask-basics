"""
Project 17 

Form data retrieval on the template
In the following example, the / URL renders a web page customer.html that contains a form 
which is used to take the customer details as the input from the customer.

The data filled in this form is posted to the /success URL which triggers the print_data() function. 
The print_data() function collects all the data from the request object and renders the result_data.html file which shows all the data on the web page.

this app_c1_5.py will also have customer.html as the front page and when 
it gets POST , then it will use the GET to retrive the result_data.html
"""


from flask import *  
app = Flask(__name__)  

@app.route('/')  
def customer():  
   return render_template('customer.html')  

@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form  
      return render_template("result_data.html",result = result)  



if __name__ == '__main__':  
   app.run(debug = False) 