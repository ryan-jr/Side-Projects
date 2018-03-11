# Data Structures and Algorithms in Python

* https://doc.lagout.org/programmation/python/Data%20Structures%20and%20Algorithms%20in%20Python%20[Goodrich,%20Tamassia%20&%20Goldwasser%202013-03-18].pdf

### Stack

* Stacks are collections of objects that are last in first out(LIFO)

* Think of a stack of plates, or a pez dispenser.

* Common stack operation include pushing objects on the stack and popping objects off the stack

* Examples of stacks include recently visited websites that are stored in browser history, "undo" in text editors

* Stacks support at a basic level a push operation to add an element to the top of the stack and a pop operation to remove and return the top element from the stack, with an error if the stack is empty.  

* Extended stack support includes, top which returns a refrence to the top element of the stack without removing it but returning an error if the stack is empty.  isEmpty, which returns True if the stack is empty.  Len, which returns the number of elements in the stack.  

* Python lists natrually support stacks with the append operation, which appends to the end of the list, as well as the pop method which returns the last element of the list.  

* However despite this, lists do not precisely align with a stack abstraction/data structure, especially in terms of terminology and operations.  

* An adapter design pattern applies to a context where we want to modify an existing class so that its methods match those of a related, but different class/interface

* A generaly way to apply the pattern is to define a new class in a way that contains an instance of the existing class as a hidden field and then implement each mehtod of the new class using methods of this hidden instance variable.  THis allows us to create a new class that performs some of the same functions as an existing class, but repackaged.  

* Using the above concept we can adapt python's list class to correspond with a stack:

```
# Using Stack S
# Using List L
# == means "is equivalent to" in this case

S.push() == L.append
S.pop() == L.pop()
S.top() == L[-1]
S.isEmpty() == len(L) == 0
len(S) == len(L)

```

* The following would be an example of an implementation of a stack: (We name it ArrayStack to indicate that the underlying data structure is Array based)


```Python3


class ArrayStack:
	"""

	LIFO Stack implmentation using Python list as underlying storage

	"""

	def __init__(self):
	"""
	Creating an empty stack
	"""
	# private list instance
	self._data = []

	def __len__(self):
	"""
	Return the number of elements in the stack
	"""
	return len(self._data)

	def isEmpty(self):
	"""
	Return True if the stack is empty
	"""
	return len(self._data) == 0

	def push(self, e):
	"""
	Add element e to the top of the stack
	"""
	# New item stored at end of list
	self._data.append(e)

	def top(self):
	"""
	Return(but don't remove) the element at the top of the stack
	Raise an exception if the stack is empty
	"""
	if self.isEmpty():
		raise Empty("The stack is empty")
	return self._data[-1]

	def pop(self):
	"""
	Remove and return the element from the top of the stack
	Raise Empty exception if the stack is empty
	"""
	if self.isEmpty():
		raise Empty("The stack is empty")
	return self._data.pop()
```

* Runtime of stack operations:

```
push: O(1)
pop: O(1)
top: O(1)
isEmpty: O(1)
len(S)

```

* The space usage is O(n) dependent on the current number of elements in the stack

* It is generally better to reserve a set amount of space, than append N items.  

* We can use stacks to check for delimiter balance:

```
 def is matched(expr):
 ”””Return True if all delimiters are properly match; False otherwise.”””

 lefty = ({[ # opening delimiters
 righty = )}] # respective closing delims

 S = ArrayStack()

 for c in expr:
	 if c in lefty:
	 	S.push(c) 				# push left delimiter on stack
	 elif c in righty:
		 if S.is empty( ):
			return False 		# nothing to match with
		 if righty.index(c) != lefty.index(S.pop( )):
			 return False 		# mismatched
 return S.is empty( ) 			# were all symbols matched?
```

* Stacks can also be useful for checking for proper opening/closing tags in HTML pages


### Queues

* Queues are similar to stacks in that it is a collection of objects, but queues use first in first out(FIFO)

* Elements can be inserted, but only the element that has been in the queue the longest can be the next element removed

* A way to think about this is like a line, where people enter from the back, and leave from the front.  

* Store lines, reservations, printers that take multiple jobs, web servers processing requests, and similar services work based off of FIFO

* Queues have two primary operations: enque to add an element to the back of the queue, and dequeue to remove and return the first element from the queue with an error if the queue is empty.  

* Queues support the following methods: first, which returns a refrence to the element at the front of the queue without removing it raising an error if the queue is empty.  isEmpty, which returns True if the queue does not have any elements.  Len, which returns the number of elements in the queue.  

* With a queue we want to use a circular array in order to avoid inefficencies with having to loop through a queue in order to shift everything up.  

* To implement a circular array we have to advance the front index with arithmetic of f = (f + 1) % N 

* We need to implement the following 3 internal/private instance variables for a queue: _data to refrence a list instance with a fixed capacity, _size for an integer representing the current number of element stored in the queue(as opposed to the length of the _data list), and _front, which is an integer that represents the index within _data of the first elmeent fo the queue(assuming the queue is not empty)

```Python3


class ArrayQueue:
  """FIFO Queue implementation using a python list"""
  # Default capaicty for all new queues
  DEFAULTCAPACITY = 10
  
  def __init__(self):
    """Create an empty queue"""
    self._data = [None] * ArrayQueue.DEFAULTCAPACITY
    self._size = 0 
    self._front = 0 
    
  def __len__(self):
    """Return the number of elements in the queue"""
    return self._size 
    
  def iseEmpty(self):
    """Return True if the queue is empty"""
    return self._size == 0 
    
  def first(self):
    """Return (but don't remove) the element at the front of the queue 
    Raise Empty exception if the queue is empty 
    """
    
    if self.isEmpty():
      raise Empty("The queue is empty")
    return self._data[self._front]
    
  def dequeue(self):
    """
    remove and return the furst element of the queue 
    Raise empty exception if the queue is empty 
    """
    
    if self.isEmpty():
      raise Empty("Queue is empty")
    answer  = self._data[self._front]
    self._data[self._front] = None 
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return answer 
    
  def enqueue(self, e):
    """ Add an element to the back of the queue"""
    if self._size == len(self._data):
      # Doubling the array size 
      self._resize(2 * len(self.data))
    avail  = (self._front + self._size) % len(self._data)
    self._data[avail] = e 
    self._size += 1 
    
  def _resize(self, cap):
    """Resize to a new list of capacity >= len(self) """
    
    old = self._data 
    self._data = [None] * cap 
    walk = self._front
    for k in range(self._size):
      self._data[k] = old[walk]
      walk = (1 + walk) % len(old)
    self._front = 0 
    

```

* The enqueue method adds an element to the back of the queue, and determines the proper index for it, dequeue removes this reference as needed.  

* Resizing the queue means that we creat a temp refrence to the old list of values and allocate a new lsit that is twice the size and copy refrences from the old list to the new list and realign the front of the queue with index 0.  

* Runtime of queue operations:

```
enqueue: O(1)
dequeue: O(1)
first: O(1)
isEmpty: O(1)
len(S)

```


### Double Ended Queues(DEqueues, AKA: Deck)

* decks are data strucutres that support insertion and deletion at both the front and the back of the queue.  

* decks are mor general than stacks and queues, and this generality can be useful.  

* Decks include several methods: addFirst, add an element to the front of the deck.  addLast, add an element to the back of the deck.  deleteFirst, remove and return the first element from the front of the deck and return an error if the deck is empty.  deleteLast, remove and return the last element from the deck and return an error if the deck is empty.  

* Decks are available from python's collections class, and will guarantee O(1) operations at eitherend, but O(n) time worst case operations.  



