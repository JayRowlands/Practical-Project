from application import app
from flask import Response
import random

@app.route('/get_location', methods=['GET'])
def service2():
    xAxis = [['A'], ['B'], ['C'], ['D']]
    yAxis = [['A'], ['B'], ['C'], ['D']]
    rand_location = xAxis[random.randint(0,3)] + yAxis[random.randint(0,3)]
    location=''.join(rand_location)
    return Response(location, mimetype='text/plain')