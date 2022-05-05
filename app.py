from flask import Flask, render_template, session, redirect, jsonify
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = 'testing'

# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

# Routes

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
  return User().login()

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
  return render_template('dashboard.html')


class User:

  def start_session(self):
    session['logged_in'] = True
    return jsonify('logged In'), 200
    
  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):

    user = db.users.find_one({
      "email": 'email'
    })

    if user and (('password'), user['password']):
      return self.start_session(user)
    
    return jsonify({ "error": "Invalid login credentials" }), 401



if __name__== "__main__":
  app.run(debug=True)   