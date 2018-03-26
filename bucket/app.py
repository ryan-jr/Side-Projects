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

	
	pageSanitized = jsonify(json.loads(json_util.dumps(mydb.test.find())))
	
	return pageSanitized["County"]
	#return newPage

if __name__ == "__main__":
	app.run(debug = True, host = "0.0.0.0")






"""
<<<<<<< HEAD




=======



>>>>>>> 086c2d82708dd34108c16b0bc348976e1f584c6d
https://stackoverflow.com/questions/27839195/reading-a-json-string-typeerror-string-indices-must-be-integers
jsonify(json.loads(
# Example JSON objects

  {
    "County": "Adair", 
    "Date": "01/01/2000 12:00:00 AM", 
    "Democrat - Active": 1412, 
    "Democrat - Inactive": 59, 
    "FIPS": 19001, 
    "Grand Total": 5727, 
    "Libertarian - Active": "", 
    "Libertarian - Inactive": "", 
    "No Party - Active": 1874, 
    "No Party - Inactive": 127, 
    "Other - Active": "", 
    "Other - Inactive": "", 
    "Primary County Coordinates": "(41.3307464, -94.4709413)", 
    "Primary Lat Dec": 41.3307464, 
    "Primary Long Dec": -94.4709413, 
    "Republican - Active": 2190, 
    "Republican - Inactive": 65, 
    "Total - Active": 5476, 
    "Total - Inactive": 251, 
    "_id": {
      "$oid": "5ab30c110e89a751fb86557b"
    }
  }, 
  {
    "County": "Appanoose", 
    "Date": "01/01/2000 12:00:00 AM", 
    "Democrat - Active": 3213, 
    "Democrat - Inactive": 78, 
    "FIPS": 19007, 
    "Grand Total": 8930, 
    "Libertarian - Active": "", 
    "Libertarian - Inactive": "", 
    "No Party - Active": 2604, 
    "No Party - Inactive": 135, 
    "Other - Active": "", 
    "Other - Inactive": "", 
    "Primary County Coordinates": "(40.7431635, -92.8686104)", 
    "Primary Lat Dec": 40.7431635, 
    "Primary Long Dec": -92.8686104, 
    "Republican - Active": 2812, 
    "Republican - Inactive": 88, 
    "Total - Active": 8629, 
    "Total - Inactive": 301, 
    "_id": {
      "$oid": "5ab30c110e89a751fb86557c"
    }
  }

"""


