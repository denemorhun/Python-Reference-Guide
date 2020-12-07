
from flask import Flask, jsonify, request, Response
from flask_api import status

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

# @app.route("/name", methods=["POST"])
# def setName():
#     if request.method=='POST':
#         posted_data = request.get_json()
#         data = posted_data['data']
#         return jsonify(str("Successfully stored  " + str(data)))

# @app.route("/message", methods=["GET"])
# def message():
#     posted_data = request.get_json()
#     name = posted_data['name']
#     return jsonify(" Hope you are having a good time " +  name + "!!!")

@app.route("/healthz", methods=["GET"])
def healthz():
    status_code = flask.Response(status=201)
    return jsonify("status code" + status_code)

app.run(host='0.0.0.0', port=8080, debug=True)
