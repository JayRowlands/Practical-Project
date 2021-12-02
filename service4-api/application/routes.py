from application import app
from flask import Response, request
from application.models import Prize
import random
@app.route('/get_prize', methods=['POST'])
def service4():

    received= request.get_json()
    location=received['location']
    resistance=received['resistance']

    location_ascii= [x.split() for x in location[ : : 1]]
    location_val = ord(''.join(filter(str.isalpha,location_ascii[0]))) + ord(''.join(filter(str.isalpha, location_ascii[1]))) 
    key_value= int(resistance) % int(location_val)

    if  key_value>1 and all(key_value%i for i in range(2, int(key_value**.5+1))):
        prize_model = Prize.query.filter_by(prize_id=random.randint(0,9)).first()
        prize = prize_model.prize_name
    else: 
        prize = "No prize won"
    return Response(prize, mimetype='text/plain')