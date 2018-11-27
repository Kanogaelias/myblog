import os 
import os.path as op

class Config:

    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kanogaelias:mikedad2002@localhost/blogmy'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    DEBUG = True
    

config_options ={
"production":ProdConfig,
"development":DevConfig
}

