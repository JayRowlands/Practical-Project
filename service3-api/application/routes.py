from application import app
from flask import Response
import random

@app.route('/get_resistance', methods=['GET'])
def service3():
    resistance = str(random.randrange(10000000, 99999999))

    return Response(resistance, mimetype='text/plain')
