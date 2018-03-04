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
