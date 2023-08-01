from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templets', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key '


#Code goes below here 

@app.route('/')
def home():
    return render_template('new_index.html')

#Code goes above here

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=5003)
