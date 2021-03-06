from flask import render_template,flash,redirect,url_for,request
from . import auth
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import LoginForm,RegistrationForm,Subscription
from .. import db
from ..email import mail_message

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invaid username or Password')

    title = 'Blog login'
    return render_template('auth/login.html',login_form = login_form,title=title) 

@auth.route('/login/subscription', methods = ['GET','POST'])

def subscribtion():
   form = Subscription()

   if form.validate_on_submit():
       user = User(email = form.email.data, username = form.username.data,password = form.password.data)
       subscribe = Subscribe(name = form.name.data,email = form.email.data)
       db.session.add(subscribe)
       db.session.commit()
       
       mail_message("Welcome to Blog","email/welcome_user",user.email,user=user)
   else:   
       return render_template('auth/login.html',Subscription = form) 
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

       
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)