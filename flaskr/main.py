"""
League of Lords' Flask app
"""

from flask import Flask, render_template, redirect, url_for, request, session, abort
from os import urandom
import imp
import os
pwds = imp.load_source('pwds', 'pwds.py')

app = Flask(__name__)
app.secret_key = urandom(pwds.KeySeed)

@app.route('/')
def main():
    """This the the homepage"""
    return ("HELLO WORLD")

@app.route('/login', methods=['POST','GET'])
def login():
    if session.get('logged_in') == True:
        return ("Already logged in")

    if request.method == 'POST':
        log_in = db.checkUser(username=request.form['username'],password=request.form['password'])
        if log_in == True:
            session['logged_in'] = True
            return('Logged in')
        else:
            return('Failed log in')

    else:
        return render_template('login.html')

@app.route('/createUser', methods=['POST','GET'])
def createUser():
    if not session.get('logged_in'):
        return ("Yo you ain't logged in")

    if request.method == 'POST':
        db.addUser(username=request.form['username'],password=request.form['password'])
        return "Success"        

    else:
        return render_template('createUser.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
