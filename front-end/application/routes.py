
from flask import render_template
from application import app
import requests

@app.route('/', methods = ['GET'])
def home():
    
    pickup_location = requests.get('http://service2-api:5001/get_location')
    grabber_resistance = requests.get('http://service3-api:5002/get_resistance')
    prize= requests.post('http://service4-api:5003/get_prize', json= {"location" : pickup_location.text, "resistance" : grabber_resistance.text})
    
    return render_template('index.html', pickup_location=pickup_location.text, grabber_resistance=grabber_resistance.text, prize=prize.text)
