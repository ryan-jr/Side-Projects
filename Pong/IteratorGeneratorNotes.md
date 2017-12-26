# Iteration vs Generation


* The diff between range and xrange is that xrange is a generator

* Generator functions allow us to write a function that can send a value to a function and resume where the generator left off, allowing us to generate a sequence of values over time, with the major difference being that the generator uses a yield statement in the syntax


* When a generator is compiled it becomes an object that supports an iteraton protocol.  

* The above means that the generator does not just get called in code and then exit.  What happens is that the generator will suspend/resume execution and state around the last value generated.  This is massively resource saving since it does not have to save every value generated in one list, etc...  (this execution suspension is known as state suspenion)



```Python3

# Notice how the generator function does NOT have a return statement, and as a result means that the output is NOT being stored in a return statement which saves memory, and to some extent avoids errors (with large numbers, because large numbers in lists can take up a lot of memory and lead to errors)

def gencubes(n):
	for num in range(n):
		yield num ** 3

for x in gencubes(10):
	print(x)			# 0, 1, 8, 27, 64...



# Fibbonacci

def fibbo(n):
	a = 1
	b = 1

	for i in range(n):
		yield 
		t = a
		a = b
		b = t + b

	# The above 3 lines can also be done by a, b = b, a + b


```

* An iterator is something that has a next function (think yield statments), but an iterable is some object that can be iterated over (think list or string)

* BUT we can convert an object (like a string) to an iterator object with # s = "hello" # stringIter = iter(x).  In this way we can call next(stringIter) on it and get # "h" as a result

* The big takeaway is that the yield keyword causes a function to turn into a generator and saves a TON of memory for large use cases.  

# Section 16: Lecture 88: Collections Module - Counter


* THe collections module implements a number of speicalized collections inculding namedTuple, OrderedDict, etc...

* The counter of the collections module, the elements are stored as keys and the counter is stored as values


```
# Counter
from collections import Counter

# Counting number of times an element occurs in a list
l = [1, 2, 3, 12, 10, 10]
Counter(l)	# {10: 2, 1: 1, 2: 1, 3: 1, 12: 1}

# This is super powerful and awesome


# Counting the number of occurances of a letter in a string
s = "aabccc"
Counter(s)	# {"c": 3, "a":2, "b":1}

# Counting the number of times a word occurs in a sentence

s = "Hello world"
words = s.split()
Counter(words)	# {Hello: 1, world: 1}


# Applying counter methods
c = Counter(words)

c.most_common(1)	# Returns [("Hello", 1), ("World", 1)] a tuple of the words that occur the number of times specified

sum(c.values())	# 2 (Returns the total number of words in the sentence)


### Other methods
c.clear() 	# resets all counts 
list(c)		# Returns a list of all unique elements
set(c)		# Returns a set of the sentence (Sets are dicts without values)
c.items()	# Convert c to a list of element, count pairs
Counter(dict(list_of_pairs))	# Convert from a list of elment, count pairs
c.most_common()[:-n-1:-1] 	# n least common elements
c += Counter()		# remove zero and negative counts


```


## Defaultdict

* dictionary like object that provides all methods provided by dicts but takes the first argument as the default data type for the dictionary.  

* THIS DOES NOT REPORT/RETURN A KEY ERROR

```Python3

from collections import defaultdict

# Normal dictionary

d = {"k1": 1}	
d["k1"]		# 1
d["k2"]		# KeyError

# Defaultdict
d = defaultdict(object)
d["one"]	#<object at 0x40dfd0> (No error!)

```


## OrderedDict

* a dictionary subclass that remembers the order in which its contents are added

```python3

# Normal dict

d = {}
d["a"] = "A"
d["b"] = "B"
d["c"] = "C"

for k, v in d.items()
	print(k, v)		# a A, c C, b B


# A normal dictionary is just a mapping that does not retain the order

d = OrderedDict()
d["a"] = "A"
d["b"] = "B"
d["c"] = "C"

for k, v in d.items()
	print(k, v)		# a A, , b B, c C

```


## Namedtuple

* t = (1, 2, 3)
* t[0] 	# 1


```python3

from collection simport namedtuple

Dog = namedtuple("Dog", "age breed name")

sam = Dog(age = 2, breed = "Lab", name = "Sammy")




```



