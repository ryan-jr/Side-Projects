https://softwareengineering.stackexchange.com/questions/155639/which-algorithms-data-structures-should-i-recognize-and-know-by-name



https://www.geeksforgeeks.org/top-algorithms-and-data-structures-for-competitive-programming/


https://www.geeksforgeeks.org/top-10-algorithms-in-interview-questions/


https://www.quora.com/How-can-one-be-well-prepared-to-answer-data-structure-algorithm-questions-in-interviews


https://medium.freecodecamp.org/coding-interviews-for-dummies-5e048933b82b

http://ai.stanford.edu/users/sahami/CS2013/final-draft/CS2013-final-report.pdf
```

An objective response:
While my initial response to this question was based on my empirical experience as a soon-to-graduate CS student and my projected opinion of the type of people I wanted to work with in the CS field. There is actually an objective (with respect to the subjective opinions of the ACM SIGCSE and IEEE computing societies) answer. Every 10 years the ACM and the IEEE bodies cooperate on a joint publication that details suggestions for undergraduate computer science curriculum based on professional knowledge of the state of the computing industry. More information can be found at cs2013.org. The committee publishes a final report listing their curriculum recommendation.

That said, I still think my list is pretty good.

Original answer below.

What Should I Know?
Minimum
I think an adept programmer should have at least undergraduate level knowledge in Computer Science. Sure, you can be effective at many jobs with only a small subset of Computer Science because of the rock solid community CS sits upon, and the narrowed focus of most professional positions. Also, many people will further specialize after undergraduate study. However, I do not think either are an excuse to not be privy of foundational CS knowledge.

To answer the title question, here is what an undergraduate CS student (the foundation for an adept programmer) should know upon graduation:

Data Structures
Machine Data Representation
Ones, Two's Complement, and Related Arithmetic
Words, Pointers, Floating Point
Bit Access, Shifting, and Manipulation
Linked Lists
Hash Tables (maps or dictionaries)
Arrays
Trees
Stacks
Queues
Graphs
Databases
Algorithms
Sorting:
Bubble Sort (to know why it's bad)
Insertion Sort
Merge Sort
Quick Sort
Radix style sorts, Counting Sort and Bucket Sort
Heap Sort
Bogo and Quantum Sort (=
Searching:
Linear Search
Binary Search
Depth First Search
Breadth First Search
String Manipulation
Iteration
Tree Traversal
List Traversal
Hashing Functions
Concrete implementation of a Hash Table, Tree, List, Stack, Queue, Array, and Set or Collection
Scheduling Algorithms
File System Traversal and Manipulation (on the inode or equivalent level).
Design Patterns
Modularization
Factory
Builder
Singleton
Adapter
Decorator
Flyweight
Observer
Iterator
State [Machine]
Model View Controller
Threading and Parallel Programming Patterns
Paradigms
Imperative
Object Oriented
Functional
Declarative
Static and Dynamic Programming
Data Markup
Complexity Theory
Complexity Spaces
Computability
Regular, Context Free, and Universal Turing Machine complete Languages
Regular Expressions
Counting and Basic Combinatorics
Beyond
To get into what you're asking about later in your question, if you are familiar with the above, you should be easily able to identify the appropriate pattern, algorithm, and data structure for a given scenario. However, you should recognize that there is often no best solution. Sometimes you may be required to pick the lesser of two evils or even simply choose between two equally viable solutions. Because of this, you need the general knowledge to be able to defend your choice against your peers.

Here are some tips for algorithms and data structures:

Binary Search can only (and should) be used on sorted data.
Radix style sorts are awesome, but only when you have finite classes of things being sorted.
Trees are good for almost anything as are Hash Tables. The functionality of a Hash Table can be extrapolated and used to solve many problems at the cost of efficiency.
Arrays can be used to back most higher level data structures. Sometimes a "data structure" is no more than some clever math for accessing locations in an array.
The choice of language can be the difference between pulling your hair out over, or sailing through, a problem.
The ASCII table and a 128 element array form an implicit hash table (=
Regular expressions can solve a lot of problems, but they can't be used to parse HTML.
Sometimes the data structure is just as important as the algorithm.
Some of the above might seem like no brainers, and some may seem vague. If you want me to go into more detail, I can. But, my hope is when encountered with a more concrete question such as, "Design a function that counts the number of occurrences of every character in a String", you look to the tip about the ASCII table and 128 element arrays forming neat implicit hash tables for the answer.

```