#!/usr/bin/python3
from flask import Flask, redirect, request, render_template, url_for, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'A_unique_and_secret_key'
user_id, user_pwd = 'root', '123456'
db_conn = MongoClient('mongodb://{}:{}@mongo:27017/admin'.format(user_id, user_pwd))
db = db_conn['admin']['user']
# print(db.list_collection_names())
print('its working')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if 'user_id' in session:
        return redirect('/')
    if request.method == 'POST':
        user_id = request.form['username']
        user_pwd = request.form['password']
        find_result = db.find_one({
                'user_id': user_id
            })
        if find_result is not None:
            if find_result['user_pwd'] == user_pwd:
                session['user_id'] = user_id
                return redirect(url_for('home'))
            else:
                error = 'Incorrect password. Please try again.'
        else:
            error = 'Unknown username. Please try again.'
    elif request.method == 'GET':
        if 'user_id' in session:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = success = None
    if 'user_id' in session:
        return redirect('/')
    if request.method == 'POST':
        user_id = request.form['username']
        user_pwd = request.form['password']
        confirm_pwd = request.form['confirm_password']
        if user_id == '' or user_pwd == '':
            error = 'Please enter your username and password!'
        elif user_pwd != confirm_pwd:
            error = 'The passwords you entered do not match.'
        else:
            find_result = db.find_one({
                'user_id': user_id
            })
            if find_result is not None:
                error = 'This username has already been used.'
            else:
                db.insert_one({
                    'user_id': user_id,
                    'user_pwd': user_pwd
                })
                success = True
    return render_template('register.html', error=error, success=success)

@app.route('/', methods=['GET', 'POST'])
def home():
    # redirect to login page if not logged in
    if 'user_id' not in session:
        return redirect(url_for('login'))
    elif request.method == 'POST':
        session.pop('user_id')
        return redirect(url_for('login'))
    return render_template('index.html')

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8888, debug=True)  # when using docker 
#     # app.run(port=8888, debug=True)  # when using python3 app.py