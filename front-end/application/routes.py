
from flask import render_template
from application import app
import requests

@app.route('/', methods = ['GET'])
def home():

    return render_template('index.html')
