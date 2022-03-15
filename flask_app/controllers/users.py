from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt        
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def show_home_page():
    return render_template('index.html')

@app.route('/create-user')
def process_form():
    data = {
        'key': request.form('value')
    }
    User.create(data)
    return redirect('/')

@app.route('/dashboard')
def show_something_else(id):
    data = {
        'id': id
    }
    return render_template('something.html', data)
