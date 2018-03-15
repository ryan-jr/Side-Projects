# Data Structures class

https://www.youtube.com/watch?v=rXET0bup-vg&list=PLC617CBC8385356FF&index=2
### Collections

* COLLECTION

* Collection is an object that gather/organizes other objects(elements)

* Many types of fundamental collections include stacks queues lists trees graphs and are broadly categorized as linear or nonlinear

* Elements in a collection are usually based on when they were added or possibly some type of relationship among the elements

* The type of collection you use depends on what you want to accomplish

* ABSTRACTION

* An abstraction hides certain details at certain times, and provides a way to deal w/ the complexity of  asystem.  

* A collection like any well defined object is an abstraction

* E.g. you can say car engine and most people know what you're talking about, the opposite of an abstraction is detail

* We want to separate the interface of the collection(how we interact with it) from the underlying details of how we choose to implement it.  E.g. A well define dinterface masks the implementation of the collection

 * TERMS

 * The terms used for collections are used a variety of ways

 * Data type: A group of values and the ops defined on those values

 * Abstract data type: A data type whose values/operations are not inherently defined in a language

 * data structure: The programming constructs used to implement a collection

 * STACK COLLECTION

 * LIFO(Last In First Out)

 * Elements can only be added on the top of the stack and removed from the top of the stack

 * Stacks are used when you want to go through things sequentially

 * COLLECTION OPERATIONS

 * Every collection has a set of ops that defines how we interact with it including: adding/removing elements, length of the collection, etc...

 * STACK OPERATIONS

 * Stack operations include: push(add), pop(remove), peek(examine element at the top of the stack), isEmpty(Determines if the stack is empty), size(determines # of elements in the queue)

* INHERITANCE

* In OOP inhertiance means to derive a class from the definition of another class.  

* Inheritance is usually easier/faster/cheaper, and is at the heart of software reuse.  

* In software a mamal class would have vars/method that describe the state/behavior of mammals, and from that class we could derive a horse or a dog class that would inhereit variables/methods from the mammal class, and the horse/dog class could have variables/methods of their own. 

* The original class that is used to establish a new class is known as the parent class, super class, or base class.  

* This derivation is known as an IS-A relationship(e.g. a hore IS A mammal)



* POLYMORPHISM

* Polymorihic means that the variable can refer to different types of objects at different points in time

* The specific method invoked by a polymorphic refrence can change from one invocation to the next.  

* Polymorphism calls for dyanmic binding which means that the binding cannot occur until runtime.  


* JAVA INTERFACES
* Interfaces are a convenient way to define operations on a collection
* USING STACKS
* Helpful for solving certain types of problems(undo operation in an application, keeps track of the most recent operations)
　
* POSTFIX EXPRESSIONS
　
* In a postfix expression the operator comes after the operands e.g. 3 4 + 2 * would be written in infix as (3 + 4) * 2.  
　
* Scan for L to R, determine if the next toke is an operator or operaand, if operand push it on the stack, if an operator pop the stack twice to get the two operands.  
　
* EXCEPTIONS
　
* Collctions must always manage problem situations carefully(e.g. removing something from an empty stack)
　
* The designer of the collection determines how it might be handled
　
* Or might a structure be full(e..g. the underlying structure might run out of memory).  
　
* Thus capacity managment is a thing
　
* Generally we should not pass along an error/raise an implementation issue with the user unless there is a good reason to do so
　
* Exceptions can generally be handled 3 ways:
　
```
Not handled at all
Handle the exception where it occurs
Handle the exception at another point in the program
```
　
* When not handled the program will generally terminate, if yo uhandle the excpetion where it occurs usually there is a try/catch/else statement.  
　
***
