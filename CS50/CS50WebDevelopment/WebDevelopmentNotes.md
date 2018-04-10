# CS 50 Web Development

### Lecture 1

* Overview

```
Git

HTML, CSS, SaaS

Flask

SQL

APIs

JS

Front Ends

Django

Testing CI/CD

Scalability (DNS, load balancing, etc...)

Security

Projects

```


##### Version Control

- Git used in conjunction/on github

* Important Git commands

```

>git clone <URL>(ends in .git)	# Pull down/download a repository(code store)

>git add <filename>/./-A 		# Start tracking a file

>git commit -m "INSERT MESSAGE"	# Save a snapshot of your tracked file

>git status						# Shows what's happening in the repo

>git push 						# Uploads code to the server

>git pull 						# Lets you download the latest version of code from a repo

>git log						# Shows a history of commits/commit messages

>git reset	--hard <commit>		# Revert back to a specific commit

>git reset --hard origin/master	# Revert back to the original version

```

* Merge conflicts occur when the changes in local and the changes in remote are different, and git doesn't know what to do.

* A merge conflict will occur when you try to pull down changes to your local machine

* A merge conflict will show as:


```
OK/NON-CONFLICTING CODE HERE
<<<<<< HEAD
LOCAL CHANGED CODE HERE
======
REMOTE CHANGED CODE HERE
>>>>> 57656c636f6d65207fa922 # Conflicting commit hash
OK/NON-CONFLICTING CODE HERE

```

* To resolve the merge conflict, open the file that you tried to pull(it should now have the HEAD ====, etc... in it).  From there you edit the file to resolve the conflict and git add the file again,and then push it.


##### HTML

* HTML tags etc... have a number of attributes to make pages responsive etc... (e.g. 50% size of a picture)

* HTML allows for the creation of forms, which are usually accompanied with inputs (with the type of input specificed in the attributes), and a submit button

* Placeholder attribute is the light text in an input before you type stuff 

##### Document Object Model (DOM)

* Think of a page as a tree with each of the tags as a node that are elements/under the head HTML tag

##### CSS (Cascading Style Sheets)

* CSS is there to make web pages nicer and provide more granular control

* DIVs are useful(divs are just divisions of code/code that you want to do something with) and allow us to separate/control different parts of the HTML page

* Margins are the space around the outside of an element, but padding generally controls the spacing between the inside of an element and the next element 

* Documentation and Google are your friend for finding different CSS properties

* Divs and Span tags let us name/divide up different parts of our page.  

* IDs must be unique, but you can have multiple tags w/ the same class name

***

### Lecture 1: HTML, CSS




### Lecture 2: Flask

##### Python

* Python is an interpreted language


##### Flask

* Generic flask code


```
from flask import Flask

app = Flask(__name__)

@app.route("/"
def index():
	return "hello world!"

```

* Flask is designed in routes, which are associated w/ the website address you want to go to

* Flask can create a dynamic page by specifying in the route what kind of information will be taken in

```

@app.route("/<string:name>")
def hello(name):
	name = name.capitalize()
	return f"Hello, {name}!"	# String formatting, we can also throw HTML in here.

```

* For us to render and actual HTML page we need to import render_template

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

```

* The argument in render_template is telling flask to look in the templates directory and find/return/display index.html

* If we wnated to add variables to Flask/the HTML page we would do:

```
### app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

	# Setting the variable
	headline = "Hello, world!"

	# Returning the variable
	return render_template("index.html", headline=headline)


### index.html
 # boilerplate tags here

 <body>
 	{{headline}}
 </body>

 # closing boilerplate here
```

* Note that we can update the variable as we want and it will change what is displayed in the HTML page.  


* Using this information we can build a simple website that can check and see if it is a certain day/holiday

```

# app.py

from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
	now = datetime.datetime.now()
	new_year = now.month == 1 and now.day == 1
	return render_template("index.html", new_year = new_year)

# index.html

# Boilerplate html

<body>
	{% if new_year %}  # {% %} introduces python syntax into HTML
		<h1> Happy new Year! </h1>
	}
	{% else %}
		<h1>No!</h1>
	{% endif %}
</body>

# Closing boilerplate HTML

```

* We could put the Python inside the flask app.py, but if we generate more applications, having the code inside the HTML can help keep it more modular/clear

* It is possible to use JS with flask apps


* Looping w/ Flask

* We do it pretty much the same as we would in python, but we just wrap it in {% for x in names %}   and end it with {% endfor %}.

* If we wanted to have each of those names in their own separate paragraph or in a bullet point in a list we would use <p>/<li>{{ x }}</p>/</li>

* Note that when you inspect the HTML, it will not show the {{%%}} at all, only the HTML

* How to link routes back and forth


```
# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/more")
def more():
	return render_tempate("more.html")



# index.html

# boilerpalte html

<body>
<h1> First Page</h1>

# note URL for and the route/function that it's linked to
<a href ="{{ url_for("more") }}">See more...</a> 




# more.html

# boilerpalte html

<body>
<h1> More Page</h1>

# note URL for and the route/function that it's linked to
<a href ="{{ url_for("index") }}">Go back...</a> 

```

* What if we want to abstract away all the boilerplate code and just extend it/add on to it/use it as a template?

* For this, we would use template inheritance



```

# layout.html

# boilerplate html

 <body>
	<h1>{% block heading %} {% endblck %}</h1>

	{% block body %}
	{% endblock %}
 </body>
# end boilerplate html

# index.html

{% extends "layout.html" %}

{% block heading %}
	First page
{% endblock %}

{% block body %}
	<p> Stuff goes here </p>
<a href = "{{ url_for("more") }}">See more...</a>

{% endblock %}

```

* Template inheritance lets you make a change once, and have it reflected in the other files/html pages

* Forms!!!

```
# app.py

from flask import Flask, render_template, request	# request is important

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
	name = request.form.get("name")	# notice how we know what form to get based upon the name provided
	return render_template("hello.html" name=name)



# index.html

{% extends "layout.html" %}

{% block heading %}
	First Page
{% endblock %}

{% block body %}
	<form action="{{ url_for('hello') }}" method="post">
		<input type="text" name="name" placeholder="Enter your name"
		<button>Submit</submit>
	</form>
{% endblock %}



# hello.html

{% extends "layout.html" %}
	Hello!
{% endblock %}

{% block body %}
	Hello, {{ name }}!
{% endblock %}



```

* Submitting data to a server uses the post method, getting data from a server uses get method(s)

* To accept multiple types of requests we would update the @ line to read @app.route("/hello", methods=["POST", "GET"])



* Storing information in sessions!


* For a note taking application we would have an empty list, and where if there were a POST request, wee would get info from the notes form and append the note to the list, and then we would return the page we want, passing in the notes list

* The issue with the note list, is that it's a global variable, meaning here's only one notepad.  To solve this we import session as well as/and from flask_session import Session

* In the index function we would use

```
notes = []

@app.route
def index():
	if session.get("notes") is None:
		session["notes"] = []
		
	if request.method == "POST":
		note = request.form.get("note")
		session["notes"].append(note)