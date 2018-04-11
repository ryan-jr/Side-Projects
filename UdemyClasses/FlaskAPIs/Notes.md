# Notes

### Section 1

```Python3
# List comprehension notes
List comprehensions allows us to create lists programatically, but also manipulate them at the time of creation e.g. [x * 3 for x in range(5)] # 0, 3, 6, 9, 12

List comprehensions also allow us to easily include conditions on what/what not to include e.g. [x for x in range(10) if x % 2 ==  0]

We can also chain methods in list comprehensions:
  people = ["bob", "SUSAN", " gR Eg"]
  normalPeople = [person.strip().lower() for person in people] # ["bob", "susan", "greg"]
  
Keep in mind with list comprehensions the tradeoff between readability and code complexity 

```


### Section 3

* HTTP Verbs

```

A web server is a piece of software designed to accept incoming requests

A GET request is a verb that is provided a path and a protocol

Depending on the code on the server, it may respond differently to the GET request

Going to a page will always do a GET< but there are also other operations including POST, DELETE< PUT, OPTIONS, HEAD etc..

GET = Retrieve something
PUT = Make sure something is there(doesn't neccessarily create something)
POST = Receive data, and use it
DELETE = Remove something

```

* REST Principles

```

REST is a way of thinking about how a web server responds to your requests

* THe server responds with resources, not JUST data

* Resources may have the same endpoint that will interact differently depending on the type of request

* REST is stateless, which means that one request cannot depend on any other/previous requests.  The server only knows about that request at that point in time, not previous ones.  

* If a user logs into a web application, the web server does not know the user is logged in since the API does not remember state, but a unique piece of data is exchanged between the user in the server over the course of the session.  



```


* Creating an API

```
* Browsers by default do GET requests

* Note that JSONs are not dictionaries, but long strings of text

* This is because, dictionaries are a python thing, whereas strings of text can be sent over the internet

* This is where the jsonify library comes in e.g. from flask import jsonify

* Say we have a list of dictionaries.  This line: return jsonify({'stores': stores}), would provide a dictionary with one key("stores"), that we could then iterate/search through because it converts the variable into a dictionary.  

```


