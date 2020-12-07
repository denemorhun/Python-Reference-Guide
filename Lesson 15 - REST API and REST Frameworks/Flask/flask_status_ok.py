
from flask import Flask, jsonify, request, Response, make_response
from flask_api import status

import requests

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return jsonify(message='Hello!'), 200

@app.route('/make_response')
def hello():
    data = {'hello': 'world'}
    return make_response(jsonify(data), 403)

@app.route("/healthz")
def healthz():
    return jsonify(status_code=200, version="0.0.1", uptime="YYYY MM DD"), 200


@app.route('/not_found')
def not_found():
    return jsonify(message="That resource was not found"), 404


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message="Sorry " + name + " you are not old enough"), 401
    else:
        return jsonify(message="Welcome " + name + ", to paradise")


app.run(host='0.0.0.0', port=8080, debug=True)
