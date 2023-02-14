from flask import Flask
import database.db as db



app = Flask(__name__)

@app.route("/post/<username>")
def new_user(username):
    return db.new_employee(username)

@app.route("/get/<username>")
def get_user(username):
    return db.get_employee(username)
    
    
