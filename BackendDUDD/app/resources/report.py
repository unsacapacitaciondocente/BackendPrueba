from flask_restful import Resource
from flask import jsonify

class Report(Resource):
    def get(self):
        return jsonify([weather])
    def post(self):
        return jsonify({"message":"This module has no post. That was a test!"})

#borrar 
weather = {
"data": [
    {
        "day": "1/6/2019",
        "temperature": "23",
        "windspeed": "16",
        "event": "Sunny"
    },
    {
        "day": "2/6/2019",
        "temperature": "21",
        "windspeed": "18",
        "event": "Rainy"
    },
    {
        "day": "3/6/2019",
        "temperature": "31",
        "windspeed": "12",
        "event": "Sunny"
    },
    {
        "day": "4/6/2019",
        "temperature": "5",
        "windspeed": "28",
        "event": "Snow"
    },
    {
        "day": "5/6/2019",
        "temperature": "17",
        "windspeed": "18",
        "event": "Rainy"
    },
    {
        "day": "6/6/2019",
        "temperature": "19",
        "windspeed": "21",
        "event": "Rainy"
    },
    {
        "day": "7/6/2019",
        "temperature": "28",
        "windspeed": "14",
        "event": "Sunny"
    }
    ]
}
#borrar

#restful apli x
#reestructuracion de carpetas -
#postman x