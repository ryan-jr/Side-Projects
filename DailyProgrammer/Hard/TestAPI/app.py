from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello world"

@app.route("/goodbye")
def goodbye():
	return "bye!"

if __name__ == "__main__":
	app.run(debug = True)