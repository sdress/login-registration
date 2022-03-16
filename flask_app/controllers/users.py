from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt        
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def show_home_page():
    return render_template('index.html')

@app.route('/create-user', methods = ['POST'])
def process_form():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password']),
    }
    if not User.validate(data):
        return redirect('/')
    user = User.create(data)
    session['user_id'] = user
    return redirect('/dashboard')

@app.route('/dashboard')
def show_dashboard():
    return render_template('dashboard.html', user=User.get_last())
