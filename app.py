from flask import Flask, make_response
from flask_restful import Api
import json
from simplexml import dumps

from api.resourse import GetAddressDetails


app = Flask(__name__)
app.secret_key = 'secret_key'
api = Api(app)
app.config['JSON_SORT_KEYS'] = False


@api.representation('application/xml')
def output_xml(data, code, headers=None):
    resp = make_response(dumps({'root': data}), code)
    resp.headers.extend(headers or {})
    return resp


@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp


api.add_resource(GetAddressDetails, '/getAddressDetails')


if __name__ == '__main__':
    app.run()