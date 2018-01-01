# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 16:44:10 2017

@author: rjr

https://www.reddit.com/r/dailyprogrammer/comments/683w4s/20170428_challenge_312_hard_text_summarizer/?st=jbuzvkww&sh=6b3755be



# Step 1: Import the stopwords in a list
# Step 2: Grab the text you want to analyze
# Step 3: Split the text you want to analyze into various sentences
# Step 4: Analyze each of the words in those sentences
    4A: Assign the words a value: positive, negative, neutral, or null (if it's a stopword)
    4B: After cutting out each word that is a stopword, create 2 dicts
        One for the sentence and one for the paragraph/text overall 
    4C: The greater the count, the more important the word/concept/sentence is and it should
        be included/ranked higher 
# Step 5: We will return at most 2 sentences, so return the 2 highest ranked sentences

Journal:
    Ok, I think I'm doing too much with step 4A, so I'll likely include it in the next .  Reading through the steps a second time, I think the second part of 4B, might be too much as well, so for right now I'll just concentrate on the first half of 4B.  
    
    
    https://stackoverflow.com/questions/3849509/how-to-remove-n-from-a-list-element
    ITERABLE VAR HERE = list(map(lambda s: s.strip(), ITERABLE(LIST/DICT HERE)))
    
So at some point I want to extend this to grab newspaper articles, luckily the newspaper
library already does that... https://github.com/codelucas/newspaper

For now I'll just import the paragraph as a string and work from there

This was useful for the stopwords list I'm using: https://www.ranks.nl/stopwords

Ok, we don't want to remove the stopwords, but we DO want them to modify the sentence score
and possibly the paragraph score?

Useful stuff for replacing the words:
    https://stackoverflow.com/questions/3271478/check-list-of-words-in-another-string
    https://ubuntuforums.org/archive/index.php/t-331589.html
    
Having functions in your return statements is a good idea
"""


def paraScore(paraString, stopWords):
    """Takes in a string of text and removes the stopwords
    
    We take in the string and remove the stopwords in order to get a unique count
    of all the words in the sentence
    
    Args:
        paraString:
        stopWords:
    
    Returns:
        Returns a dict with the number of times each unique word occurs in the paragraph
        
    Raises:
        N/A
    """

    for word in stopWords:
        pass
       # print(word)
            
    print(paraString)


def stripText(paraString):
    """Takes in a string of text and removes what we don't want/need
    
    Args:
        paraString: A paragraph brought in as a string of text
        
    Returns:
        paraString: The original paramater modified to exclude what we don't want
        
    Raises:
        N/A   
    
    """

    
    excludeList = ["(", ")", "[", "]"]
    
    if "(" in paraString:
        x = paraString.find(excludeList[0])
        
        y = paraString.find(excludeList[1])
        
        paraString = paraString[0:x] + "" + paraString[y + 1:-1]
        
    if "[" in paraString:
        x = paraString.find(excludeList[2])
        
        y = paraString.find(excludeList[3])
        
        paraString = paraString[0:x] + "" + paraString[y + 1:-1]
    
    return paraString
       
    
    

# Reading stopwords, putting them into a list
f = open("stopWords.txt", "r")
stopList = f.readlines()
stopList = list(map(lambda s: s.strip(), stopList))


paraString = "The purpose of this paper is to extend existing research on entrepreneurial team formation under a competence-based perspective by empirically testing the influence of the sectoral context on that dynamics. We use inductive, theory-building design to understand how different sectoral characteristics moderate the influence of entrepreneurial opportunity recognition on subsequent entrepreneurial team formation. A sample of 195 founders who teamed up in the nascent phase of Interned-based and Cleantech sectors is analysed. The results suggest a twofold moderating effect of the sectoral context. First, a technologically more challenging sector (i.e. Cleantech) demands technically more skilled entrepreneurs, but at the same time, it requires still fairly commercially experienced and economically competent individuals. Furthermore, the business context also appears to exert an important influence on team formation dynamics: data reveals that individuals are more prone to team up with co-founders possessing complementary know-how when they are starting a new business venture in Cleantech rather than in the Internet-based sector. Overall, these results stress how the business context cannot be ignored when analysing entrepreneurial team formation dynamics by offering interesting insights on the matter to prospective entrepreneurs and interested policymakers."

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
paraString = stripText(paraString)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
paraScore(paraString, stopList)
paraList = paraString.split(". ")
print(paraList)

