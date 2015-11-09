from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.session import SqlAlchemySessionInterface as sasi
import os

class TempConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'bad_secrets'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SESSION_TYPE = 'SqlAlchemySessionInterface'

app = Flask(__name__, static_url_path='')
#app.config.from_object('TempConfig')
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'bad_secrets'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SESSION_TYPE'] = 'SqlAlchemySessionInterface'


app.session_interface = sasi( app=app,
                              db=db,
                              table='sessions',
                              key_prefix="",
                              use_signer=True,
                              permanent=True )



import wate.iterviews
