from flask import *   
app = Flask(__name__)


@app.route('/CEO')  
def CEO():  
    return 'Welcome 1'  
#app.add_url_rule("/CEO","CEO",CEO) 

@app.route('/employees')  
def employees():  
    return 'Welcome 2'  
#app.add_url_rule("/employees","employees",employees) 

@app.route('/clients')  
def clients():  
    return 'Welcome 3'  

#app.add_url_rule("/clients","clients",clients) 



#dynamic redirect functions
def func_CEO_loggedin():
    return 'You are officially logged in for viewing confindential information'

app.add_url_rule("/CEO_loggedin","CEO_loggedin",func_CEO_loggedin) 


def func_employees_loggedin():
    return 'Welcome to CRM'

app.add_url_rule("/employees_loggedin","employees_loggedin",func_employees_loggedin) 

def func_clients_loggedin():
    return 'Welcome to Stratacent'

app.add_url_rule("/clients_loggedin","clients_loggedin",func_clients_loggedin) 

# so this is where the url_function helps in redirects (dynamic redirect)  
@app.route('/loggedin/<role>')  
def loggedin(role):  
    if role == 'CEO':  
        return redirect(url_for('CEO_loggedin'))  
    if role == 'employees':  
        return redirect(url_for('employees_loggedin'))  
    if role == 'clients':  
        return redirect(url_for('clients_loggedin')) 



@app.route('/loggedin/<role>/<int:id>')
def logging1(role,id):
    if role == 'clients' and id >= 9000 and id < 9999:
        return f'<h1>Hello {role}, with id {id} welcome to the portal </h1>'

    else:
        return '<h1>Please enter valid id Number</h1>'

    if role == 'employees' and id >= 1000 and id < 9999:
        return f'<h1>Hello {role}, with id {id} welcome to the portal </h1>'

    else:
        return '<h1>Please enter valid id Number</h1>'

        
if __name__ =="__main__":  
    app.run(debug = False) 


