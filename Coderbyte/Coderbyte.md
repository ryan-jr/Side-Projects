# Coderbyte challenges



### Question 1: Longest Word

```

Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 

```



* Inital Solution:

```Python3

def LongestWord(sen): 
    longestWord = ""
    this = "this"
    wordList = sen.split()

    for word in wordList:
        print(longestWord)
        if len(word) > len(longestWord):
            longestWord = ""
            for character in word:
                if character.isalpha():
                    
                    longestWord += character
        else:
            pass
                
    return longestWord
 


```


* Refactored Solution:

```Python3

# I was failing too many test cases, so I refactored this to include/cover 
# instances in which numbers are part of the string, and to cover instances
# in which a prior word is longer than/of equal length to the word currently
# being evaluated
# Examples of formerly failed test cases are included below

"""
print(LongestWord("hello world"))
print(LongestWord("this is some sort of sentence" ))
print(LongestWord("longest word!!" ))
print(LongestWord("a beautiful sentence^&!" ))
print(LongestWord("oxford press" ))
print(LongestWord("123456789 98765432"  ))
print(LongestWord("letter after letter!!" ))
print(LongestWord( "a b c dee" ))
print(LongestWord("a confusing /:sentence:/[ this is not!!!!!!!~"))

"""

def LongestWord(sen): 
    
    # Set variables
    longestWord = ""
    wordList = sen.split()
    
    # Loop through each word, check each word length
    # If word length larger than already stored, change longestWord
    for word in wordList:
    	# Had to make sure things were unicode here so Python
    	# Would properly evaluate numbers/use the isnumeric() function

        word = unicode(word, "utf-8")

        # Checking to make sure everything is an alpha character

        if word.isalpha() and len(word) > len(longestWord):
            longestWord = ""
            for character in word:
                if character.isalpha() or character.isnumeric():
                    longestWord += character

        # Dealing with the numeric case

        elif word.isnumeric() and len(word) > len(longestWord):
            longestWord = ""
            for character in word:
                if character.isalpha() or character.isnumeric():
                    longestWord += character

        # Catch all

        else:
            pass
          
    return longestWord


```

* Solution Explanation/thought process:

```

When I first saw the problem I was thinking of diffrent ways to approach it between lists or hasmaps/dictionaries, but a list through Python's .split seemed to be the most straightforward.  After going with that I knew I had to loop through each word and compare it in some way.  

I actually got stuck for about 5 minutes or so, because I wasn't doing the right comparision between word and longestWord as I was only using len(word) to compare against longestWord.  

Comparing just the alpha also turned out to be an issue becuase there were test cases that tested numbers as well, that I didn't prepare for.  

The runtime should be roughly O(n^2) because we touch every item/word in the wordList, and then on top of that touch every character in each item/word.  

```


### Question 2: Factorial


* Question:

```


Using the Python language, have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it (e.g. if num = 4, return (4 * 3 * 2 * 1)). For the test cases, the range will be between 1 and 18 and the input will always be an integer.


Sample Test Cases:

Input:4

Output:24

Input:8

Output:40320

```

```Python3

# Recursive Solution
def FirstFactorial(num): 

  if num <= 1:
    return 1
  else:
    returnNum = num * FirstFactorial(num - 1)
    return returnNum
    
# keep this function call here  
print FirstFactorial(raw_input())


# Iterative Solution:

def firstFactorial(num):
    product = 1
    for i in range(num):
        product *=   i + 1

    return product

print(firstFactorial(3))


```

* Solution Explanation/thought process:

```

So this one was pretty straightforward since I have a handle on recursion, but the thing that threw me at first was returning FirstFactorial(num * num - 1), when I needed to only get the factorial of the second term.  For me, in this instance recursion feels naturaly, but it's also possible to use the iterative version of this


```


### Question 3: Reverse a string

```
Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH. 

```


* Answer 3:


```Python3

def FirstReverse(str): 

    str1 = list(reversed(str))
    str1 = "".join(str1)
    
    return str1
    
# keep this function call here  
print FirstReverse(raw_input())

```


* Solution Explantion/Thought process:

```

This one is fairly straightforward with Python's builtin reversed function.  I got stuck for a minute when I just used str1 = reversed(str), which returned an object(a reverse iterator) which has to have a list applied to it.  From there we apply a join to the list and assign that to the variable we want to return.  

```


### Question 4: Letter Changes

```
Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 


Test Case:

Input: "coderbyte"
Output: "dpEfsczUf"


```


* Answer 4:


```Python3

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

vowels = ["a", "e", "i", "o", "u"]

def LetterChanges(str): 

  str = str.lower()
    
  returnData = ""
  modifiedReturnData = ""


  # Initalize Letter index 
  # This works becuase it assumes that the index starts at 0 and ONLY updates 
  # if/after the next character is found in alpha
  letterIndex = 0

  for i in str:
    if i not in alpha:
      returnData += i 
    else:
        letterIndex = alpha.index(i)
        # Deal with "z" case
      	if i == "z":
        	letterIndex = -1
      letterIndex += 1
      returnData += alpha[letterIndex]
      
  # Update/modify vowels if needed
  for j in returnData:
    if j not in vowels:
      modifiedReturnData += j 
    elif j in vowels:
      modifiedReturnData += j.upper()
      
  
  return modifiedReturnData

```


* Solution Explantion/Thought process:

```

So this one was more of a challenge for me from listing out all of the alphabet/vowels, and then breaking down the problem into solveable steps. 

I opted first to tackle the case in which something may not be an alpha character, or if it is handle the case that it might be "z".  For the case of anything else it will return the index of that particular character, modify it by 1, and add the corresponding index in the list to returnData.  

From there I loop through return data to find any vowels and upper case them as needed, we then return everything we need to.

Because the for loops are separate, rather than nested the runtime is O(n), not 2 * O(n) since with big O we drop the constant(s).

```


### Question 5: Simple Adding

```
Have the function SimpleAdding(num) add up all the numbers from 1 to num. For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10. For the test cases, the parameter num will be any number from 1 to 1000. 

Use the Parameter Testing feature in the box below to test your code with different arguments.

Test Case:

Input: 4
Output: 10


```

* Answer 5:

```Python3

def SimpleAdding(num): 

    addingArr = []
    total = 0
    for i in range(0, num):
      addingArr.append(i)
      
    addingArr.append(num)
    
    for j in addingArr:
      total += j 
      
    
    # code goes here 
    return total

```

* Solution Explantion/Thought process:

```

For this one, reduce would be a perfect choice, but it's not part of Python 3 so I opted to append everything from 0 up to and EXCLUDING the paramater provided into a list, then appending the paramater itself.  After that I sequentially added the numbers together into the total to be returned.  

Like the one before, this uses 2 for separate for loops and as such is O(n)

```


### Question 6: Letter Capitalize


* Answer

```

Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space. 

Test Case:
Input: "argument goes here"
Output: "Argument Goes Here"



```


```Python3

def LetterCapitalize(str):
  wordArr = str.split(" ")
  newArr = []
  for word in wordArr:
    newArr.append(word.replace(word[0], word[0].upper()))
    
    
  return " ".join(newArr)


```

* Explanation

```

This one splits every word passed in via str into the wordArr, we then loop through each word in wordArr, taking care to append each word into newArr, but not before replacing the first character of each word with its uppercase equivalent.  At the end we have to join each word together with a space so that we return a complete sentence. 

This one runs in constant time as well.  

```