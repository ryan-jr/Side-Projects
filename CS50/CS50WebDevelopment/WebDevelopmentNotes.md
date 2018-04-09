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

* 