"""
Project 16 - 

Embedding Python statements in HTML

Due to the fact that HTML is a mark-up language and purely used for the designing purpose, sometimes, 
in the web applications, we may need to execute the statements for the general-purpose 
computations. For this purpose, Flask facilitates us the delimiter {%...%} which can be used to embed the simple python statements into the HTML.

Example
In the following example, we will print the table of a number specified in the URL, 
i.e., the URL http://127.0.0.1/:5000/table/10 will print the table of 15 on the browser's window.

"""

from flask import *  
app = Flask(__name__)  
  
@app.route('/table/<int:num>')  
def table(num):  
      return render_template('print-table.html',n=num)  
if __name__ == '__main__':  
   app.run(debug = False)  