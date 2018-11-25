from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required
from ..models import User,PhotoProfile,Post,Role
from .forms import UpdateProfile,CommentForm
from .. import db,photos

# Views

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')



@main.route('/Comment', methods = ['GET','POST'])
def comment():
     form = CommentForm()
    
     if form.validate_on_submit():
        username.comment = form.username.data
        comment.comment =form.comment.data
        comment = comment(username,comment)
        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('.comment'))
     return render_template('post_comment.html',CommentForm=form)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/pofile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():

        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        user_photo = PhotoProfile(pic_path = path)
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))     