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


```

### Lecture 3: SQL

* Databases

```

Used to store/manipulate data

Relational databases can be thought of like tables

Imagine we were trying to store a table/database for an airline company: They would have columns for origin, destination, and duration

SQL: Structure Query Langauge

PostgreSQL is the version used

SQL has multiple datatypes including:
Integer: Integer
Decimal: Floats
Serial: Incremented integers
VARCHAR(Variable length of characters): For strings etc...
BOOLEAN: T/F



```


* Creating a table in sql

```
CREATE TABLE flights (
	id SERIAL PRIMARY KEY   	# id is a unique identifier that is incremented, and is specificlay unique
	origin VARCHAR NOT NULL,	# origin is a string that cannot be null
	destination VARCHAR NOT NULL,	# See above
	duration INTEGER NOT null       # Above, but w/ integer

);


```

* You can host a postgreSQL on your sever, or you can find databases online

* psql allows you to start a server, or pull from a URL


* /d allows you to display the tables that existin the DB

* Constratins include: 

```
NOT NULL: Value cannot be empty
UNIQUE: Must be unqiue (no two values can be the same(e.g. usernames))
PRIMARY KEY: Single way to refrence a table/row
DEFAULT: Can have a default value
CHECK: Only allow values that meet certain cosntraints


```


* INSERT command

```

INSERT INTO flights(origin, destination, duration) VALUES ("New York", "London", 415);

```

* SELECT: Query to read from a database



```

SELECT * FROM flights;	# Simplest select statement, specifies to grab everything and FROM what table


Other type of select queries include:

SELECT origin, destination FROM flights; # Returns only the origin/destination columns

SELECT * FROM flights WHERE id = 3;	# The WHERE columns specifies the row(s)

SELECT * FROM flights WHERE origin = "New York";	# Returns flights from New York

SELECT * FROM flights WHERE duration > 500; # Returns flights that have a duration greater than 500

SELECT * FROM flights WHERE destination = "Paris" AND duration > 500;	# Pretty much like it says, but we could also use an OR rather than an AND

SELECT destination, duration FROM flights;	# returns only the destination/duration columns from flights


```

* SQL is very powerful because it has functions that we can access and apply to our tables/queries

```

SELECT AVG(duration) FROM flights;	# 501.6667, returns the average duration of a flight

SELECT AVG(duration) FROM flights WHERE origin = "New York";	# returns the average duration of a flight from New York

```

* Another popular function is the COUNT function which counts the number of rows given a set of criteria



```
SELECT COUNT(*) FROM flights; 	# Returns the number of rows in the flights table

SELECT COUNT(*) FROM flights WHERE origin = "New York";	# Returns the number of rows in the flights table that have an origin of New York

```


* MIN and MAX are also popular functions:


```

SELECT MIN(duration) FROM flights;	# Returns the shortest flight duration(ONLY that number, not the row) from flights

# SELECT * FROM flights WHERE duration = 245;	# Returns the row of the flight that has a duration of 245 minutes

```

* The IN keyword can also be useful

```

SELECT * FROM flights WHERE origin IN ("New York", "Lima")	# Returns flights that have an origin of either Lima or New York
```

* You can also do string matching with the LIKE keyword

```
SELECT * FROM flights where origin LIKE "%a%"	# Think of % as a Regex delimiter that means certain amount of text preceding or following.  This returns anything from the origin that has an "a" in it preceded by some amount of text, and followed by some amount of text

```

* SQL Functions

```
SUM
COUNT
MIN
MAX
AVG

```

* What if we want to update data?

* We use the UPDATE keyword

```
UPDATE flights
	SET duration = 430
	WHERE origin = "New York"
	AND destination = "London";

# Note that we need to have the WHERE/AND clauses in there otherwise we would update the entire table to have a duration of 430

```

* DELETE

```

DELETE from flights
	WHERE destination = "Tokyo";

```

* IDs are usually static/unique(meaning that if you delete something with ID 3, nothing else will have ID 3 again), this is because as we deal with connecting/relational databases, it would confuses the databases if something were to replace an ID.  

* LIMIT limits the number of results you get back

```
SELECT * FROM flights LIMIT 2;	# returns the first 2 flights

```

* We can sort the data by using the ORDER BY keyword:

```

SELECT * FROM flights ORDER BY duration ASC;	# Returns all the flights from shortest at the top to longest at the bottom

SELECT * FROM flights ORDER BY duration ASC LIMIT 3;	Returns the 3 shortest flights


```

* NOTE ASC is ascending order, DESC is descending order

* We can interact with databases with ORMs and directly from the command line

* To find the flights that are most popular we would use GROUP BY with other commands such as:


```
SELECT origin, COUNT(*) FROM flights GROUP BY origin;	# Returns a list of origins and the count 

# To find something greater than, we use the HAVING clause which is SIMILAR TO the WHERE clause but COMES AFTER a GROUP BY clause.  

SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;

```

* Freign keys

* Foreign keys are ways to connect DBs together, if the DB gets more complicated/has more rows/columns etc...

* Foreign Keys allow us to connect databases in an easier way.  This is because instead of repeating information all throughout the table and taking up unneccessary space etc... we can use an identifier/number in the column to refer to another DB that is holding all of that similar information.  It is not easily human readable, but it is an easy lookup for SQL.  This is also used to keep things organized by separating the data.

* A foreign key, is refrecning from a different table

* JOINs allow you to refrence multiple tables, and tell them how they relate together


* 45.44 timeframe

```

SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id 

SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id WHERE name = "Alice";

```

* SQL assumes that when you JOIN you want to only get the things that match, but you can use a LEFT JOIN statement to get everything from the table that is refrenced on the left of the LEFT JOIN statement even if it does not match


```
SELECT origin, destination, name FROM flights LEFT JOIN passengers ON passengers.flight_id = flights.id;

```

* indexing

* AN index is like an index an in a book, to easily look things up (you can create an index on an arbitrary column to speed things up) We don't do it for every column, because of space/time concerns

* Nested queries

* Combining multiple queries, this can be easier when you break them into one query at a time...

* SECURITY CONSIDERATIONS!!!

* SQL Injection

* SQL injection is where you put in a SQL query into the form.  

* To prevent this SQL has some escape characters, and sanitizes input.  

* RACE CONDITIONS

* If multiple databases are accessed by multiple people, and if people try to do things at the same time, operations execute in a strange order (e.g. bank databases)  First you should make sure the bank balance is correct, and that they can withdraw a certain amount.  But if two people are going to different ATMs and they both have access to the same account and the commands can run in the same order...but the output would be incorrect.  

* We would solve this with locking/transactions.  E.g. lock out others from updating things until the process is complete

* This is done with the BEGIN command in SQL followed by the command(s) you want to run and then use COMMIT

* HOW do we bridge the gap between Flask and SQL?

* We can use a library like SQLAlchemy which connects Python and SQL

* If we wanted a python program that would output everything we had in the flights database it would look like so:

```Python3
import os 


from sqlalchemy import create_engine
from sqlalcehmy import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))	# creates different sessions for different people to allow them to modify the database individually

def main():
	flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
	for flight in flights:
		print(f"{flight.origin} to {flight.destination})


if __name__ == "__main__":
	main()


```

* fetchall() returns a list

* HOWTO: insert data into a database from Python

