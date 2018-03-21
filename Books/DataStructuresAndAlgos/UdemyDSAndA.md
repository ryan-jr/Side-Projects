# Udemy Data Structures and Algos


### Section 1: Intro to Data Structures and Algos(DS&A)



##### Lecture 1: DS&A

* Program development requries representing data eficently and developing a step by step procedure.  

* Data strucrues represent the former and algos represent the latter

* Data structures are made up of data representation methods including arrays, linked lists, trees.  

* Algos are procedures that contain steps for performing a task

* When choosing an algo we have to select a data strucutre to use

* And when choosing a data structure we have to develop an efficent algorithm to use on it

* There can be many algos to solve a problem, but when there are multiple choices we want to try and use the most efficent/best suited one.  

* Algo efficency depends on runtime and memory



##### Algo runtime

* 2 methods to measure runtime:

```
1.  Experimental Method:
Implement the algo, run it on different inputs, and time the algo using timeit() or equivalent.

The above issue has the limitation of being limited to specific languages, and hardware.  This may also have a limited number of inputs, which means we may miss different behavior for different inputs.  

2.  Analytical Method(Asymptotic analysis):

The analytical method allows us to analyze the runtime independent of the software/hardware, and consider all inputs.

```


##### Asymptotic Analysis

* Runtime depends on the input size(e.g. as size increases so does runtime)

* Asymptotic analysis looks at how the runtime of an algo increases with the input size.  It's not the exact runtime, but rather a large input

* To deterimne algo efficency we have to see how the algo behaves when the input size is increased(e.g. the growth rate) for this we look use Big O notation

##### Big O Notation

* This lets us see how fast a function grows as N becomes large

* Common Asymptotic Functions(AKA: Common Growth rates)

```

More efficent

1
log n
n
n log n
n^2
n^3
...
n^k
2^n
3^n
...
k^n
n!

Less efficent


```


##### Finding Big O

* In Big O analysis we only care about the value of N as N becomes large, and when N becomes large, the fastest growing term becomes dominant(i.e. the N term with the greatest power), constants(and lower terms) become insignificant. 


* General rules are:

```

Keep the fastest growing term and discard lower terms/constants

Ignore coefficents

If f(n) is constant we say that f(n) is O(1)

The base of a logarithm is not important (e.g. 8log(2)N and 23log(10)N are both O(log(N)))


```

##### Tight and Loose upper bounds

* To satisfy O(N) we want to find the least/tight upper bound so we know AT LEAST how fast N is growing


***

### Quiz 1:

```

1.  In Asymptotic Analysis, the exact runtime is calculated
A: False

We calculate the general runtime, and at least how fast N is growing

2.  For analyzing an algorithm, we study how the runtime of the algorithm increases with an increasing input size.
A: True

We want to see how the algorithm scales with increasing inputs

3.  Growth rate of n is greater than growth rate of log(n)
A: True

See chart above

4.  For finding big O for a function, we have to keep the (Fastest/Slowest) growing term of the function, and discard all the lower terms/constants.

A: Fastest

The fastest growing term will provide us with at least how fast the algorithm will grow

5.  WHile computing the O notation, the base of the logarithm is not important.

A: True

O analysis ignores the base

6.  What is the big O for the function 3N^2 + 5N + 18
A: O(N^2)

7: What is the big O for the function 100
A: O(1)


8: For the function 4N^3 + 3N^2 + 7N, how would you classify the statement: f(N) is O(N^5)
A: It is correct, but not informative

* It is correct because it is greater than the minimum growth rate of our function O(N^3) so it COULD be a growth rate of the function, but it is NOT the LEAST/TIGHT BOUND growth rate.  


9: Arrange functions in order of asymptotic complexity

10: True/False: N^3 + 3^N is O(N^3)
A: False

The rate 3^N is a faster growth rate than a cubic rate

```

<<<<<<< HEAD


##### Big O Analysis of Algos and Finding Time Complexity

* Runtime is proportional to the number of primitive operations executed during runtime.

* To find the runtime we need to express the number of primitive operations executed during runtime in terms of N

* For Big O analysis we aren't interested in how much time an operation takes on a computer, but rather how many times the operations is executed.

* A big part of this is looking at operations where the number of iterations depend on N


```

In a loop if we do something like:

while i >= 1:
	i /= 2

OR

while i < n:
	i *= 2

Because of the logarithmic nature of the operation on N, (decrementing in the first case, incrementing in the latter), the runtime will always be O(log(n)) since the base/constant doesn't matter.  

```


* For nested loops we care more about the inner loop because the inner loop will always execute more times than the outer loop.  Oftentimes the runtime of the inner loop will be n * n (N^2)

* For if/else statements we consider the runtime to be that of which the runtime is larger(e.g. when the if statement is N^2 and the else statement is O(n) we would say the runtime is N^2))

* For a loop that performs an operation a constant number of times (such as for i in range(5)) we would say that it is O(1)


##### Best, Average, and Worst Case Analysis

* The best, average, and worst case gives us the minimum, average, and maximum runtime of an algorithm for input size N

* In most cases we use the worst case runtime as it will tell us that the algo will perform no worse than that case, and the best case does not occur very often.  


##### Common Complexities

O(1): Constant runtime (same time for any input size)

O(log(n)) Logarithmic (Usually an algo that reduces the operation/size each time through, binary search, etc...)

O(n) Linear (When each element is touched/processed)

O(n log n) Linear Logrithmic

O(N^2) Quadratic (Usually nested for loops)

O(N^3) Cubic (matrix multiplication etc...)

O(N^k) Polynomial

O(x^N) Exponential

##### Abstract Data Types

* ADT is a concept that defines a data type logically

* An ADT specicfies a set of data and a set of operations that can be performed on the data.  

* So a stack ADT could be carried out with a singly linked list, a doubly linked, list or an array.  

* Data strucutre is the implementation of the ADT

```
ADT: Logical view of data and the operations to manipulate the data

Data Structure: Actual representation of data and methods/algos to manipulate the data

The ADT is the what, the data structure is the how
```

* An ADT specification is often called an interface

=======
***

### Section 2: Linked Lists
　
```
All linked list lecture notes

* List ADTs can be implemented using Arrays, or with a linked list

* Linked list are not contiguous

* Links are refs to the next item in the list, the list item and the link are a Node.  

* Linked lists are a dynamic data strucutre made up of nodes(e.g. it does not have a fixed size and can allocate memory as needed)

* Insertion/deletion of elements is easier

* lists can be used to implement ADTs such as data types like lists, stacks and queues.  

* Lists require more memory, and random access is an issue due to the sequential nature.

* The node class has info and a  link which is set to none, and the  link list class has the init which creates a start which is set to None

* To traverse a linked list we need to move the refrence forward by getting the refrence from the link(in the case of getting the first node we need to get the ref from start)

* We break/stop when the ref is None.  This means that we can use a loop, and as we are using a loop it means that we can initialize and use a counter

* To find a ref to the last node we loop through the list and when the loop hits None, it will be the last node of the list

* To find the second to last node we loop through until p.link.link is None

* To find a node with particualar info, we break when we find the argument that is passed into the function in p.info (e.g. p.info == x)

* To find a ref to a predecessor of a node with particular info(e.g. the node before the one with the info we want to find) we would use(if p.link.info == x) in the loop 

* To find a ref to a node at a particular position we pass the argument k(the node at the position we want) and use (while ctr < k and p is not None)

* To insert a new node we have to create a temp Node and set the proper refs/link


* OK THE CONCEPT THAT I HAVEN'T been able to wrap my head around is that there are TWO pieces to each Node in the linked list, and the LINK points to the next piece of data, NOT the next link in the chain, but the next NODE.  

* To insert a node at the begininning of a list we need to make sure that self.start = temp since start was originally None

* To insert a node at the end of a list we find the ref at the end/last node of the list and we update p.link = temp in order to insert the node at the end of the list

* To insert a node between two nodes we need to make sure that temp.link = p.link(so we can get the ref to the next node), then we need to make sure that p.link = temp(so that the node we're going in front of refs to the temp(aka new) node)

* To insert after a node that has a given value
```

##### Lecture 14: Introduction
　
* We have seen the list Abstract Data Type, and it can be implemented with an Array or with a Linked list.  

* Arrays maintain items in a sequential order, but with Linked Lists, there is no sequential order but rather the order is maintained with a link that points to the next item.  

* A node is a combonation of the item/object that is being stored along with the pointer/ref to the next object.  

* We need to know where the first node(start) is but after that we can figure out the rest of the nodes.  

* A linked list is a dynamic data structure made up of nodes

* Dynamic in this case means that we/the structure can allocated/deallocate memory as needed
```
OK so a point of confusion for me was understanding that a linked list can be ARRAY BASED.  
This is confusing because arrays are CONTIGUOUS MEMORY, whereas linked lists are nonsequential/contiguous.  
For a linked list to be array based the node is stored in a single element array(e.g. [Node]) that points to another single element array.
In order to dynamically allocate we may need to create several empty arrays
　
```
* Insertion/deletion of elements is easier in linked lists as we do not need to shift the entire array, only update the pointer/ref to the next and/or previous node.  

* The disadavantages of linked lists include that efficent random access is not possible(due to no indexing), and that implementation requires extra memory due to the link that is required for each item.  

* Linked list variants are: Singly linked list, doubly linked list, circular linked list, linked list w/ header node, sorted linked list.  
　
* Single linked list contains the object and the link to the next node.  

* Doubly linked list contains the obeject the the link(s) to the next/previous node.  
　
```Python3

class Node:
def __init__(self, value):
    self.info = value
    self.link = None
class SingleLinkedList:
def __init__(self, value):
    self.start = None
def displayList(self):
    pass
def countNodes(self):
    pass
def search(self, x):
    pass


```
　
##### Lecture 15: Traversing a linked list
　
* Traversal means visiting a node once

* To move a refrence forward we set the ref of p = p.link

* Keep in mind that p.link is the next node

* To traverse a linked list we would do:

```Python3

# first node
p = self.start 

print(p.info)
ctr = 0
while p is not None
	ctr += 1
	p = p.link

	print(p.info)
	print(ctr)

```


```Python 3
# Code for Linked List

class Node:
	def __init__(self, value):
		self.info = value
		self.link = None

class SingleLinkedList:
	
	def __init__(self):
		self.start = None

	def displayList(self):
		if self.start is None:
			print("List is empty")
			return
		else:
			print("List is:  ")
			p = self.start
			while p is not None:
				print(p.info)
				p = p.link
			print()

	def countNodes(self):
		p = self.start
		ctr = 0

		while p is not None:
			ctr += 1
			p = p.link

		print("The number of nodes in the list is:", ctr)

	def search(self, x):
	position = 1
	p = self.start
	while p is not None:
		if p.info is x:
			print("The term is:", x, "which is at position", position)
			return x

		elif p.info is not x:
			position += 1
			p = p.link
			continue

	print(x, "was not found!")




dataList = SingleLinkedList()

dataList.createList


```


##### Lecture 16: Finding refs in a single linked list

* To find the ref to second to last item in the list:

```

# This finds the second to last node, because p.link.link will "look ahead" one ref and get that data

p = self.start
while p.link.link is not None:
	p = p.link


# To find a node w/ particular info
# Let's say we have to find x(a particular value that we want)

p = self.start
while p is not None:
	if p.info == x:
		break
	p = p.link


# To find a predecessor node w/ particular info

p = self.start
while p.link is not None:
	if p.link.info == x:
		break
	p = p.link


# To find ref to a node at a particular position(at position k)

p = self.start
ctr = 1
while ctr < k and p is not None:
	p = p.link
	ctr += 1




```



##### Lecture 17: Insertion in a single linked list

* There are multiple insertion cases including, at the beginning, into an empty list, at the end, and between nodes.

* To insert a new node we allocate a node, and associate it with a temp variable:

```Python3

# What the Node class looks like:
"""
def __init__(self, value):
	self.info = value
	self.link = None




```

* To insert at the beginning:

```Python 3

# Setting up the node order correctly

temp = Node(data)
temp.link = self.start


self.start = temp

```

* Inserting a Node in an empty list

```
self.start = temp


```

* Inserting at the End

```

p = self.start
while p.link is not None
	p = p.link

p.link = temp

```


### Lecture 18: Insertion in a singly linked list

* Inserting between nodes

```Python3


# This updates the temp node so that temp will take the current link from p and point to the correct next node.
temp.link = p.link

# This updates p so that p.link points to the temp node.  
p.link = temp

```

* Insertion after a node

```python3

# Insert a new node after the node having value x

p = self.start
while p is not None:
	if p.info == x:
		break
	p = p.link
	temp = p.link
	p.link = temp

```

* Insertion before a node

```Python3


p = self.start
while p is not None:
	if p.info == x:
		break
	p = p.link
	temp.link = p.link
	p.link = temp



```


* Insertion at a given position

```Python3

# Given value k, insert at k position

# Insert between 3, and 4, 4 now becomes position 5/shift everything right by 1

p = self.start
ctr = 1

while ctr < k - 1 and p is not None
	p = p.link
	ctr += 1

temp.link = p.link
p.link = temp


```



##### Deletion in a singly linked list

* These cases are much the same as insertion with deletion of the first node, deletion of the only node, deletion between nodes in the list, deletion at the end

```
# PSUEDOCODE For deletion of the first node

self.start = self.start.link

```

```
# PSUEDOCODE for deletion of the only node
self.start = None
```

```
# PSUEDOCODE for deletion between nodes in the list

p.link = p.link.link

```

```
# PSUEDOCODE for deletion at the end of the list

p.link = None

```

```Python3

# Actual methods to be used

def deleteNode(self, x):
		
	if self.start is None:
		print("List is empty")
		return

	# Deletion of first node
	if self.start.info == x:
		self.start = self.start.link
		return

	# Deletion betwen nodes/at the end
	p = self.start
	while p.link is not None:
		if p.link.info == x:
			brea
		p = p.link


	if p.link is None:
		print("Element", x, "not in list")
	else:
		p.link = p.link.link

def deleteFirstNode(self):
	if self.start == None:
		return
	self.start = self.start.link

def deleteLastNode(self):

	if self.start is None:
		return

	if self.start.link is None:
		self.start = None
		return

	p = self.start
	while p.link.link is not None:
		p = p.link
	p.link = None

```


##### Reversing a single linked list

* For this we need 3 refs: prev, p, next

```

# PSUEDOCODE to reverse a singly linked list

prev = None
p = self.start
while p is not None:
	next = p.link
	p.link = prev
	prev = p
	p = next
self.start = prev

```


```Python3

# Code to reverse a singly linked list

def reverseList(self):
	prev = None
	p = self.start
	while p is not None:
		next = p.link
		p.link = prev
		prev = p
		p = next
	self.start = prev


```



