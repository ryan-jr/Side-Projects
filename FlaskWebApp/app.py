from flask import Flask, render_template

app = Flask(__name__)

#from app import app 

#@app.route("/")
#def hello():
	#return render_template("index.html")


@app.route('/index')
def there():

	# Creating username dict and posts list
    user = {'username': 'Ryan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    # Passing back the template, where it should be, it's title and args
    return render_template("index.html", title="Home", user=user, posts=posts)

if __name__ == "__main__":
	app.run(debug=True)