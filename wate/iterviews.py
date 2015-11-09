from wate import app
#import db_ops
from flask import render_template, request, send_from_directory, session

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return str(session['counter']) 
