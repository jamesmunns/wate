from wate import app
#import db_ops
from flask import render_template, request, send_from_directory

@app.route('/')
def index():
    return "Hello world!"
