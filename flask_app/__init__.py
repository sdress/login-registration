from flask import Flask

app = Flask(__name__)
app.secret_key = "mysupersecretkey" # create secret key

# don't forget to import flask, pymysql, and flask-bcrypt in shell