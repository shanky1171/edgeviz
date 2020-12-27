# app.py


from flask import Flask
from flask import request, render_template, flash, redirect, url_for, json
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(BaseConfig)
app.config['MONGODB_SETTINGS'] = {
    'db': 'edgedb',
    'host': 'mongodb',
    'username': 'edgedbuser',
    'password': 'edgedb',
    'port': 27017
}
db = SQLAlchemy(app)

mdb = MongoEngine()
mdb.init_app(app)

from forms import LoginForm
from forms import RegistrationForm
from models import *
from nosqlmodels import *

#@app.route('/', methods=['GET', 'POST'])
#def index():
#    if request.method == 'POST':
#        text = request.form['text']
#        post = Post(text)
#        db.session.add(post)
#        db.session.commit()
#    posts = Post.query.order_by(Post.date_posted.desc()).all()
#    return render_template('index.html', posts=posts)

@app.route('/')
def index():
        return "Hello World from Shanky!"

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		print("Login :" + form.username.data + form.password.data)
		flash('Login requested by user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		user1 = EUser.query.filter_by(EntUserName=form.username.data).first()
		if user1 is None or not user1.check_password(form.password.data):
			flash('Login has Failed!!!')
			return render_template('login.html', title='Sign In', form=form)
		flash('Login is Successful!!!')
		return render_template('start.html', title='Main Application')
	return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
        form = RegistrationForm()
        if form.validate_on_submit():
                user = EUser(EntUserName=form.username.data, EntUserEmail=form.email.data)
                user.set_password(form.password.data)
                db.session.add(user)
                db.session.commit()
                print("UserName :" + form.username.data)
                print("Email:    " + form.email.data)
                print("Password: " + form.password.data)
                flash('Congratulations, you are now a registered user!!!')
                return redirect(url_for('login'))
        return render_template('register.html', title='Regsiter', form=form)

@app.route('/register1', methods=['GET', 'POST'])
def register1():
        form = RegistrationForm()
        if form.validate_on_submit():
                user = User(name=form.username.data, email=form.email.data)
                user.save()
                print("UserName :" + form.username.data)
                print("Email:    " + form.email.data)
                print("Password: " + form.password.data)
                flash('Congratulations, you are now a registered user!!!')
                return redirect(url_for('login'))
        return render_template('register.html', title='Regsiter', form=form)


@app.route('/dboard', methods=['GET', 'POST'])
def dboard():
        return render_template('dboard.html')

def add_user_db():
    print("In add_user_db()")
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    print(username, email, password)
    user1 = EUser(EntUserName=username, EntUserEmail=email)
    user1.set_password(password)
    user1.EntUserID = 1010
    db.session.add(user1)
    db.session.commit()
    return("User added succesfully")

def validate_user():
    print("In validate_user()")
    username = request.form['username']
    password = request.form['password']
    print(username, password)
    user1 = EUser.query.filter_by(EntUserName=username).first()
    if user1 is None or not user1.check_password(password):
        print ('Authentication failed!')
        return Response("Authentication failed!", 401)
    print ('Authentication Success!')
    return Response("Authentication Success!!!", 200)

if __name__ == '__main__':
    app.run()
