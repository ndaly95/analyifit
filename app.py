from flask import Flask
import pandas as pd
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return ""

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'fitness101' and request.form['username'] == 'analyifit':
        session['logged_in'] = True
        return render_template('index.html')
    else:
        flash('wrong password!')
    return home()

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
