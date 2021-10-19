from flask import request, jsonify, make_response
import requests
import xml.etree.ElementTree as ET
from flask_restful import Resource
from sqlalchemy import text
class GetAddressDetails(Resource):
    def get(self):
        address           = request.args['address']
        output_format     = request.args['output_format']
        

        output_data   = get_coordinates(address, output_format)
        
        response      = make_response(output_data)
        format    =         output_format = "xml"

        if format.lower() == "xml":
            response.headers["Content-Type"] = "application/xml"
            
        else:
            response.headers["Content-Type"] = "application/json"
        return response

    def post(self):
        print()
        address           = request.form['address']
        output_format     = request.form['output_format']
        
        output_data   = get_coordinates(address, output_format)
        print(output_data)
        response      = make_response(output_data)
        format = output_format
        if format.lower() == "xml":
            response.headers["Content-Type"] = "application/xml"
            
        else:
            response.headers["Content-Type"] = "application/json"
        return response






def get_coordinates(address, output_format):
    API_KEY = Your_KEY
    url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    parameters = {
        "address": address,
        "key": API_KEY
    }
    response_data = requests.get(url, params=parameters).json()
    output_json_data = {
        "coordinates": {
            "lat": response_data['results'][0]['geometry']['location']['lat'],
            "lng": response_data['results'][0]['geometry']['location']['lng']
        },
        "address": response_data['results'][0]['formatted_address']
    }
    if output_format == 'xml' or output_format == 'XML':
        return {
            "coordinates": {
                "lat": response_data['results'][0]['geometry']['location']['lat'],
                "lng": response_data['results'][0]['geometry']['location']['lng']
            },
            "address": response_data['results'][0]['formatted_address']

        }
        
    return output_json_data
