from flask_restful import *
from flask import *
import records 
import json 
import os  
import flask
import tablib


app = Flask (__name__)

dataset = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__), "out.csv")) as f:
	dataset.csv = f.read() 


@app.route("/")
def index():
	return flask.jsonify(eval(str(dataset)))


if __name__ == "__main__":
	app.run(debug = True)


# TODO, get rid of zero width spaces as found...https://stackoverflow.com/questions/14844687/invalid-character-in-identifier
# You tried to jsonify and json.dumps things but both resulted in a "not serializable object" error