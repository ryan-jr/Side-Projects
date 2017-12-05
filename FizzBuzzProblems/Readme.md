# Fizzbuzz problems

Fizzbuzz problems in general are meant to be quick questions to ask during an interview to figure out a candidate's aptitude with a particular language and its constructs.  

For README I'll be using Python, but any language should work.  

## 1.  Fizzbuzz

The problem: "Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”

(A potential) Solution:

```Python3

# Fizzbuzz 

"""

"Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”
"""

for i in range(0, 101):
  print(i)
  if(i % 3 == 0 and i % 5 == 0):
    print("FizzBuzz")
    
  elif(i % 3 == 0):
    print("Fizz")
  
  elif(i % 5) == 0:
    print("Buzz")

```

Some explanation: We put FizzBuzz as the inital condition to check for because if we put 3 at the top and then check for 5, and then check for 3 AND 5, we will end up printing out Fizz, Buzz, and FizzBuzz when we happen upon a multiple of 3 and 5.  

## 2.  Reverse a string

The problem: Take a standard input string, reverse it, and produce the output.  
Note: Some of these methods (reversed and negative stride) are likely specific to Python, but the others should be language agnostic.  

```Python 3

# Reverse a string 

# For loop into an empty string method
print("For loop method:")
string = "Hello"
string1 = ""

for i in string:
  string1 = i + string1
  
  
print(string1)



# While loop method
print("While loop method:")
ctr = 0 
while ctr < len(string):
  ctr += 1
  print(string[-ctr], end="")
  
  

# Negative stride method 
print()
print("Negative Stride method:")
print(string[::-1])


# Reversed method 
print("Reversed method:")
print("".join(reversed(string)))


```

## 3.  Find the largest/smallest value in a list/array

The problem: Given a list with an arbitrary amount of numbers, find the largest/smallest value.  

Note: Another way to go about this is to order the list with a sort and retrieve the last/first element of the array/list respectively.

```Python3
# Find the largest/smallest value in a list 

list1 = [22, 75, 99, 30, 12, 2]
value = list1[0]

# Find the largest value
for i in list1:
  if(i > value):
    value = i 
    
print(value)


# Find the smallest value
for i in list1:
  if(i < value):
    value = i 
    
print(value)
```