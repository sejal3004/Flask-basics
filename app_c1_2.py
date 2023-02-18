"""
Project 15 - for dynamic printing or other things using demilter while rendering html 

Delimiters
Jinga 2 template engine provides some delimiters which can be used in the HTML to make it capable of dynamic data representation. The template system provides some HTML syntax which are placeholders for variables and expressions that are replaced by their actual values when the template is rendered.

The jinga2 template engine provides the following delimiters to escape from the HTML.

{% ... %} for statements
{{ ... }} for expressions to print to the template output
{# ... #} for the comments that are not included in the template output
# ... ## for line statements

"""
from flask import *  
app = Flask(__name__)  
  
@app.route('/user/<uname>')  
def message(uname):  
      return render_template('message1.html',name=uname)  
      
if __name__ == '__main__':  
   app.run(debug = False)  