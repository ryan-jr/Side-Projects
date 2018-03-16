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

***

### Section 2: Linked Lists
　
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
　
