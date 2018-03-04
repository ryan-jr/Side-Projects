# Coderbyte challenges



1.  Question:

```



```



* Solution:

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
 
print LongestWord(raw_input())


```

* Solution Explanation/thought process:

```

When I first saw the problem I was thinking of diffrent ways to approach it between lists or hasmaps/dictionaries, but a list through Python's .split seemed to be the most straightforward.  After going with that I knew I had to loop through each word and compare it in some way.  

I actually got stuck for about 5 minutes or so, because I wasn't doing the right comparision between word and longestWord as I was only using len(word) to compare against longestWord.  

Comparing just the alpha also turned out to be an issue becuase there were test cases that tested numbers as well, that I didn't prepare for.  

The runtime should be roughly O(n^2) because we touch every item/word in the wordList, and then on top of that touch every character in each item/word.  

```
