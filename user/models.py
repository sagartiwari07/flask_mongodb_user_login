# from flask import Flask, jsonify, request, session, redirect
# from passlib.hash import pbkdf2_sha256
# # from app import db

# class User:

#   def start_session(self):
#     session['logged_in'] = True
#     return jsonify('logged In'), 200
    
#   def signout(self):
#     session.clear()
#     return redirect('/')
  
#   def login(self):

#     user = db.users.find_one({
#       "email": 'email'
#     })

#     if user and (('password'), user['password']):
#       return self.start_session(user)
    
#     return jsonify({ "error": "Invalid login credentials" }), 401