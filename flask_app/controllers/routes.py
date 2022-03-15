from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt        
from flask_app.models.model_name import Class_Name

bcrypt = Bcrypt(app)

@app.route('/')
def show_home_page():
    return render_template('index.html')

@app.route('/process')
def process_form():
    data = {
        'key': request.form('value')
    }
    Class.create(data)
    return redirect('/')

@app.route('/some-page/<int:id>')
def show_something_else(id):
    data = {
        'id': id
    }
    return render_template('something.html', data)
