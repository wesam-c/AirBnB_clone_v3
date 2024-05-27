#!/usr/bin/python3
"""
APP
"""

from flask import Flask, make_response, jsonify
from flask_cors import CORS
from os import getenv
from models import storage
from api.v1.views import app_views
from flasgger import Swagger

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)

app.config['SWAGGER'] = {
    'title': 'AirBnB clone - RESTful API',
    'description': 'This is the api that was created for the hbnb restful api project,\
    all the documentation will be shown below',
    'uiversion': 3}

Swagger(app)


@app.teardown_appcontext
def teardown(exception):
    """Function that closes the storage on teardown"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """not found route"""
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_HOST', '5000')
    app.run(host=host, port=port, threaded=True)
