from werkzeug.security import generate_password_hash,check_password_hash
from . import db 
from flask_login import UserMixin
from . import login_manager,admin
from flask_sqlalchemy import SQLAlchemy


from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import ModelView


class Comment(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(120))
    comment = db.Column(db.Text, nullable=False)

    def __str__(self):
        return self.comment


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    path = db.Column(db.Unicode(128))

    def __unicode__(self):
        return self.name

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    
    def __repr__(self):
        return f'User {self.username}'
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")
    
    def __repr__(self):
        return f'User {self.name}'

class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))        


post_tags_table = db.Table('post_tags', db.Model.metadata,
                           db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
        
                           )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    user = db.relationship(User, backref='posts')

    

    def __str__(self):
        return self.title
 

    def __init__(self, session):
        # Just call parent class with predefined model.
        super(PostAdmin, self).__init__(Post, session)



admin.add_view(ModelView(Post,db.session))
admin.add_view(ModelView(User,db.session))
