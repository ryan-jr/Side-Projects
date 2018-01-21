from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps 

e = create_engine('sqlite:///out.db')

app = Flask (__name__)
api = Api(app)

class FIPS(Resource):
	def get(self):
		# Connect to DB 
		connection = e.connect()

		# Query the db and return JSON 
		query = connection.execute("select distinct FIPS from out")
		return {'FIPS': [i[0] for i in query.cursor.fetchall()]}

api.add_resource(FIPS, '/')

if __name__ == "__main__":
	app.run()

# C:\Users\rjr\documents\github\sideprojects\dailyprogrammer\hard\333-apisite