from flask import Flask, jsonify

app = Flask(__name__)
app.run(debug=True)

# In the mindset/from the perspective of a server
# Post = receives data from a browser
# Get = used to send data back to the browser/user




# POST /store data = name, create a store w/ a given name 
# GET /store/<string:name>, get a store w/ a given name and return data
# GET /store, return a list of all the stores
# POST /store/<string:name>/item, create an item in a store w/ a given name
# GET /store/<string:name>/item, return data about an item from a store w/ a given name
# Keep in mind that browser requests are by default GET requests


# Store data

stores = [

	{
		"name": "Store 1",
		"items": [

			{
			 "name": "Item 1",
			 "price": 20.01

			}





		]


	}


]

@app.route("/")
def index():
	return "Hello world!"

# POST /store 
@app.route("/store", methods=["POST"])
def createStore():
	pass 


# GET /store/<string:name>
@app.route("/store/<string:name>") # http//127.0.0.1:5000/store/storeName
def getStore(name):
	pass 

# GET /store, return a list of all the stores
@app.route("/store")
def getStoreInfo():
	return "store"
	return jsonify({'stores': stores})


# POST /store/<string:name>/item
@app.route("/store/<string:name>/item", ["POST"])
def createItem(item):
	pass 

# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def itemData():
	pass

