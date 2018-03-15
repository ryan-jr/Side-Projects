# Java Software Structures

* Collections/a collection is an object that gathers/organizes other objects

* Elements within the collection aretypcially organized by the order of theier additon or by some relationship among the elements

* An abstraction hids certain details at certain times.  Interfaces allow access to the abstraction in some way(e.g. a car engine is controlled by the ignition, and the throttle(the interfaces)

* Data types are a group of values and the operations defined on those values.  An Abstact data type is a data type whose values and operations are not inherently defined in the programming language

* A data structure is the underlying programming construct used to implement a collection.  

* A stack collection operates in LIFO and includes push, pop, peek, isEmpty, and size.  

* Inheritance is the process of deriving a new class from an exsisting one and is key for software reuse.  Inheriticed variables/methods can be used in a derived class as if they had been declared locally.

* Inheritance creates an IS-A relationship between all parent/child classes.  (A horse IS A mammal)

* We can create class hierarchies in which the child of one class, can be the parent of another class, with common features being as high up as possible. 


*** WHAT IS POLYMORPHISM ***???!!!

* Polymorphic refrences use the type of object not the type of reference to determine which version of a method to invoke.  






***





### Ch 3: Collections(Cont) AND (The Beginning of) Ch 4: Linked Structures


* ARRAYSTACK

* The easiest way to generally implement something is through an array.  
* One of the design implementation decisions is to set a specific size/length, or if it will be dynamic.  

* Because the stack operations only work on one end, they are generally efficent which means that operations are O(1)

* CHAPTER 4: LINKED STRUCTURES

* REFS AS LINKS

* There are many ways to implement a collection, a linked structure uses object ref variables to link one object to another.  

* Recall that an object ref variable stores the address of an object, in this way an object ref is a pointer to an object.

* A list ref can be used to form a linked list, in which one object refers to the next object.  

* Each object in the list is known as a node.  

* A linked list is a dynamic structure in that its size grows/shrinks as needed, unlike a static array.  

* NONLINEAR STRUCTURES

* A linked list is a linear structure, but object refrences allow us to create nonlinear structures such as hierarchies/graphs

* MANAGING LINKED LISTS

* THe refs in a linked list must be carefully managed to maintain the integrity of the structure

* Speical care should be taken to ensure that the entry point into the list is maintained properly

* The order in which certain steps are taken is important

* Consider inserting/deleting nodes in various postions within the list

* This may mean creating a temp node, just in case you delete an interior node and need to keep a ref to the next node

* ELEMENTS WITHOUT LINKS

* The problems w/ self ref objects is that they must know they are part of the list, the better approach is to manage a separate list of nodes that also ref the objects stored in the list

* The list is still managed using the same techniques, and the objects stored in the list need no special implementation to be part of the list.

* A generic list collection can be used to store any kind of object

* SENTINEL NODES

* THere are variations on the implementation of linked lists that may be useful such as the use of sentinel/dummy nodes on either end of the list

* This eliminates the special cases of inserting/deleting nodes at the beginnning/end of the list


* DOUBLY LINKED LISTS

* Each node as has a ref to both the next and prev node which makes traversing the list easier

* IMPLEMENTING A STACK WITH LINKS

* We can used a linked list to implement the stack collection, to do this though we would need to create a Node class to represent a node in the list.  

* The linked list version of a stack is similar to an array version, but the linked list version does not have index numbers.  

* The linked version of a stack would have the same operations, but they would be implemented differently because it's a different basic structure.  

* The linked list stack operations will have a runtime of O(1)(i.e. the same as the array implementation)

* USING STACKS

* One classic way of using stacks is to keep track of alternatives in maze traversal or other trial/error algorithms

* Using a stack this way simulates recursion, and can keep track of the moves that have been tried/not tried.



```
Assignment 1: 
Write a program that can be used as a database of student's information for a department.  THe program should be able to dynamically allocate/deallocate storage for student records using linked lists.  

You must use a linked list to keep the list of items for this program.


The database should have the following fields:
First Name
Last Name
Course Code 
Grade

The program should have the following menu:
Press 1 to insert a new record
Press 2 to delete a record
Press 3 to search the database(by last name)
Press 4 to print a range in the database
Press 5 to to find the class average for the course
Press 9 to quit


The insert function should work regardless of position.  Position 0 refers to the position before the first record.  Any positon greater than the length of the database should be put as the last postion.  

Similarly the delete postion should work for any position.  Make sure it works even when deleting the first, last, or middle records.

The search function should be used to search by last name.  If the student is found, all records associated w/ that student should be printed on screen.  

The print function should work regardless of the range requested.  If the start/end ranges are not defined, only valid records should be printed.  

To compute the class average, first search the field with the course code, and only average those grades that match w/ the proper course code.    
```





