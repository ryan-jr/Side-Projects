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

Making a capitalized version of stopwords:
https://stackoverflow.com/questions/29334276/capitalize-first-letter-of-the-first-word-in-a-list-in-python

Making sure to know how join works is pretty nice...
https://stackoverflow.com/questions/493819/python-join-why-is-it-string-joinlist-instead-of-list-joinstring

I love having a findAll methdod in my toolbox...sooooo useful already


Useful for understanding the job hunt: https://blog.stephanbehnke.com/how-i-learned-to-stop-worrying-and-love-the-job-hunt-in-toronto/


I tried to replace part of a tuple that was in a list, then I realized I could
replace the tuple itself, which is what I wanted in the first place
https://stackoverflow.com/questions/9479184/replace-a-tuple-inside-of-a-list-by-its-first-entry


I have to regularly remember that zipping something doesn't make it a list, and it
isn't easily printable
https://stackoverflow.com/questions/19777612/python-range-and-zip-object-type

Well dang that was easy to turn a list of tuples into a dict:
    dict(scoreTuples)    # wayyyyy to easy and I love it


"This case describes the establishment of a new Cisco Systems R&D facility in Shanghai, China, and the great concern that arises when a collaborating R&D site in the United States is closed down. What will that closure do to relationships between the Shanghai and San Jose business units? Will they be blamed and accused of replacing the U.S. engineers? How will it affect other projects? The case also covers aspects of the site's establishment, such as securing an appropriate building, assembling a workforce, seeking appropriate projects, developing managers, building teams, evaluating performance, protecting intellectual property, and managing growth. Suitable for use in organizational behavior, human resource management, and strategy classes at the MBA and executive education levels, the material dramatizes the challenges of changing a U.S.-based company into a global competitor."


"The purpose of this paper is to extend existing research on entrepreneurial team formation under a competence-based perspective by empirically testing the influence of the sectoral context on that dynamics. We use inductive, theory-building design to understand how different sectoral characteristics moderate the influence of entrepreneurial opportunity recognition on subsequent entrepreneurial team formation. A sample of 195 founders who teamed up in the nascent phase of Interned-based and Cleantech sectors is analysed. The results suggest a twofold moderating effect of the sectoral context. First, a technologically more challenging sector (i.e. Cleantech) demands technically more skilled entrepreneurs, but at the same time, it requires still fairly commercially experienced and economically competent individuals. Furthermore, the business context also appears to exert an important influence on team formation dynamics: data reveals that individuals are more prone to team up with co-founders possessing complementary know-how when they are starting a new business venture in Cleantech rather than in the Internet-based sector. Overall, these results stress how the business context cannot be ignored when analysing entrepreneurial team formation dynamics by offering interesting insights on the matter to prospective entrepreneurs and interested policymakers."

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
TODO: Ok, so I've got it done, should I add an average text analyzer? So that it can calculate the overall score against the number of unique words?
"""

from collections import Counter
import statistics
import re
from collections import OrderedDict
from operator import itemgetter

def findAll(c, string):
  """Finds all indicies/instances of a character in a string 
  
     Given a string and a character c,  the method finds all instances/indicies 
     of the character and returns a list with the indicies of where the character 
     occurs.  
     
     Args:
     c: The character passed in that the method will find 
     string: The string to iterate over and find the character in 
     
     Returns:
     returns a list findList that contains the indicies of where the character occurs 
     
     Raises:
     N/A
  
  """
  
  findList = []
  ctr = 0
  stringList = list(string)
  for char in stringList:
    if c == char:
      findList.append(ctr)
      ctr += 1
    else:
      ctr += 1 
    
  return findList



def sentenceOrder(s, sentenceList):
    """Arranges sentences in a chronological order
    
        Takes in a mean value and a dictionary of sentence keys that have
        rankings/scores associated with them as values.  From this we filter out
        all of the sentneces below the mean, and arrange the sentences in a chronological
        order
    
    Args:
        mean: A mean value calculated from all of the sentence scores
        sentenceScoreDict: A dictionary with sentence/score key/value pairs
    
    Returns:
        N/A
        
    Raises:
        N/A
        
        
    """
    # TODO: What do I do if the highest score is the last item in dicitonary???
    # I think I would fail over into printing the first 3 keys
    
    return sentenceList.index(s)
    
        
    

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
    # Going through and capitalizing stopwords to potentially remove them later
    capitalizedStopWords = []
    ctr = 0
    for i in stopWords:
        capitalizedStopWords.append(stopWords[ctr].capitalize())
        ctr += 1

    
    paraString = paraString.split(" ")

    # Looping through and removing the stopwords 
    for word in stopWords:
        if word in paraString:
            indexList = findAll(word, paraString)
            for i in indexList:
                paraString[i] = ""
    
    for word in capitalizedStopWords:
       if word in paraString:
            indexList = findAll(word, paraString)
            for i in indexList:
                paraString[i] = ""
      
    # Using filter to get rid of uneccessary spaces
    paraString = list(filter(None, paraString))

    
    # Finding the most interesting/most used words in the list to score
    data = Counter(paraString)
    commonWordList = data.most_common()
    
    # This section of the code is constructed to find a good value to 
    # establish what is "interesting/relevant" in the text provided
    # To do this we calculate both the median and the mode to try and get tendencies of both
    ctr = 0
    median = 0
    medianList = []
    
    
    
    for i in commonWordList:
        val = i[1]
        medianList.append(val)
        
    # Getting the median and mode for comparative values
    median = statistics.median(medianList)
    mode = statistics.mode(medianList)

    # Filtering out the mode to prevent an akward distribution
    medianList = list(filter(lambda x: x > mode, medianList))
    median = statistics.median(medianList)   
    
    
    for i in commonWordList:
        if commonWordList[ctr][1] < median:
            commonWordList[ctr] = ""
        ctr += 1

    commonWordList = list(filter(None, commonWordList))
    
    
    commonWords = []
    for i in commonWordList:
        commonWords.append(i[0])
        
    
    
    return commonWords

def stripText(paraString):
    """Takes in a string of text and removes what we don't want/need
    
    Args:
        paraString: A paragraph brought in as a string of text
        
    Returns:
        paraString: The original paramater modified to exclude what we don't want
        
    Raises:
        N/A   
    
    """

    
    excludeList = ["(", ")", "[", "]", "U.", "S.", "U.S."]
    
    if "(" in paraString:
        x = paraString.find(excludeList[0])
        
        y = paraString.find(excludeList[1])
        
        paraString = paraString[0:x] + "" + paraString[y + 1:-1]
        
    if "[" in paraString:
        x = paraString.find(excludeList[2])
        
        y = paraString.find(excludeList[3])
        
        paraString = paraString[0:x] + "" + paraString[y + 1:-1]
        
    if "U.S." in paraString:
        x = paraString.find(excludeList[4])
        y = paraString.find(excludeList[5])
        
        paraString = paraString[0:x] + "US" + paraString[y + 2: -1]
    
    return paraString
       
    
 
def sentenceScore(interestingWords, sentenceList):
    """Scores each sentece based upon how many interesting words it has
    
    Arguments:
        interestingWords: A list of words that has been determined to be interesting
        sentenceList: A list of sentences contained in the text that was originally
                      passed in
                      
    Returns:
        Returns a summary of the text based on the score of sentences
        
    Raises:
        N/A
    """
    score = 0
    sentences = []
    scores = []

    
    for sentence in sentenceList:
        sentences.append(sentence.split(" "))
        
    for lists in sentences:
        score = 0
        for words in lists:
            if words in interestingWords:
                score += 1
        scores.append(score)

    # Taking care of anything that is a zero score in both the index and the sentence list
    scoreIndex = []
    ctr = 0
    for i in scores:
        if i == 0:
            scoreIndex.append(ctr)
        ctr += 1

    
    
    for i in scoreIndex:
        sentenceList[i] = ""
        
    sentenceList = list(filter(None, sentenceList))
    scores = list(filter(lambda x: x > 0, scores))
    
    
    mean = statistics.mean(scores)
    
    sentenceScore = list(zip(sentenceList, scores))    
    
    print(interestingWords)
    
    sentenceScore = dict(sentenceScore)
    sortedScores = OrderedDict(sorted(sentenceScore.items(), key = itemgetter(1), reverse = True))
    
    chronoList = []
    for i, k in enumerate(sortedScores):
        if i < 3:
            x = sentenceOrder(k, sentenceList)
            chronoList.append(x)

    chronoList = sorted(chronoList)
    for i in chronoList:
        print(sentenceList[i])
    """
    for k, v in sentenceScore.items():
        if v < mean:
            pass
    """
    
    
    
     
    
# Reading stopwords, putting them into a list
f = open("stopWords.txt", "r")
stopList = f.readlines()
stopList = list(map(lambda s: s.strip(), stopList))



paraString = ""

with open("dataIn.txt", "r", encoding="utf8") as dataFile:
    paraString = dataFile.read().replace("\n", " ")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
  
paraString = stripText(paraString)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
interestingWordList = paraScore(paraString, stopList)
paraString = re.sub("[?!]", ".", paraString)
sentenceList = paraString.split(". ")
sentenceScore(interestingWordList, sentenceList)
