from flask import Flask 
from pymongo import MongoClient
import datetime
from flask.json import jsonify
from flask import request
import json
from bson import json_util, ObjectId


client = MongoClient("mongodb://localhost:27017/")

# Database name 
mydb = client["Test"]

app = Flask(__name__)


@app.route("/")
def index():
	pageSanitized = jsonify(json.loads(json_util.dumps(mydb.Test.find())))
	return pageSanitized

if __name__ == "__main__":
	app.run(debug = True, host = "0.0.0.0")