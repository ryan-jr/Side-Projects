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

