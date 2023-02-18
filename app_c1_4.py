#simple rendering a page from templates on css through message.html


from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def message():  
      return render_template('message2.html')  
      
if __name__ == '__main__':  
   app.run(debug = False)  