# Notes Python Meetup 03/27/2018

How to Describe Relationship Data: Graph/Hypgergraph Databases(Tom Taylor is giving the talk)

### What do we mean by relationship?

* One model is a network(e.g. a graph)

* Undirected graph(Think Facebook/the internet backbone)

### What does data describing a network look like?

* Boring/Stupid(But it looks pretty!)

### For Hypergraph databases

* Network X is a nice library for this

* What do we want to use this for?

```

We can graph links on web pages
We can use it for things like pagerank


```

### Pagerank idea:

```

The algo: Update Weight w of webpage i where:
	Where webpage i is the targe of hyperlinks(ij1), (ij2), ...(ijN) from webpages j1...jN with current weights wj1...wjN where each webpage j has nJ outgoing hyperlinks including the link ij pinting at webpage i


Each webpage has weights based off of how many links point to it

```

### Graph Traversal

* You go through each node in the graph and compute it

* This is the key to how Hypergraph works

### How do you implement this?

* Graph databases (Neo4j, ArangoDB, OrientDB(OSS))

* Why: Find out influencers in Twitter/social media, Recommendation engine

### Why graph networks are not good enough(Why Hypergraphs are better)

* With a hypergrah an edge might be between multiple nodes/people in them

* Think of a graph on steroids

* A hypergraph can be compared more to a set of gemetric shapes

### Hypergraph dataases

* Hypdergraph db

* VertexProject




# Lightning Talk: Subprocess module

* NLP Engineering focuses on Traditional/Deep Learning

* Mostly solved is stuff like spam detection, Part of speech tagging, named entity recognition, making good progress is sentiment analysis, conference resolution, owrd sense disambiguation, arsing, machine translation and inforamtion extration.  Super hard stuff is Question answering, paraphrasing, summarzation, and dialog.  

### Traditional Approach

* Usually has tokenization

* The bag of words approach does not take into account the order of words

* In deep learning each word is captured via an array/integer that is associated with "meaning".  The numbers themselves don't mean anything but it allows you to find words that are close to the current word.  

* Think of Word2Vec

* I cannot put the phone in my pocket because it is too big, I cannot put the phone in my pocket because it is too small



```
Every talk should answer the question:
WHY IS THIS BEING DONE/WHAT IS THIS USEFUL FOR
```

```python3

"""


Your function should be called bestDays and take one array of integers as an input.
Daily stock values will be represented in an array of integers (arr[]) representing the stock price at the beginning or "opening bell" of each day.
You may use the following as a test array, from day 0 through day 7: {17, 11, 60, 25, 150, 75, 31, 120}. In this case, purchasing on day one and selling on day four would yield the most profit.
bestDays analyses historical data and returns when one should have bought and sold to maximize profit, it is not designed to predict the future. If you do manage to write a program that accurately predicts future stock market trends, congratulations, you'll be very very rich.
You are required to buy and sell only once.
For the sake of this exercise, you will only ever be purchasing, owning, or selling one share.
bestDays should return the day on which one should buy a share, followed by the day on which one should sell a share, as integers.

"""




def sortingAlgot(arr):
    for i in range(1, len(arr)):
        j = i-1 
        key = arr[i]
        while (arr[j] > key) and (j >= 0):
           arr[j+1] = arr[j]
           j -= 1
        arr[j+1] = key
      
    return arr
      

def bestDays(arr):
  daysArr = []
  ctr = 0
  
  for i in range(len(arr)):
    daysArr.append(ctr)
    ctr += 1 
    
  x = list(zip(arr, daysArr))
  y = sortingAlgot(x)
  return y
  
  



stockData = [17, 11, 60, 25, 150, 75, 31, 120]


info = bestDays(stockData)
infoLen = len(info) - 1
print(info[0][1])
print(info[infoLen][1])



```