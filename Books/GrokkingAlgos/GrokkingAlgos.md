# Grokking Algorithms

### Grokking Algorithms Ch: 9 Dynamic Programming

* Dynamic programming is taking a problem, breaking it up into smaller problems, and solving those smaller problems first.

* Revisiting the knapsack problem: You have a knapsack that can hold only X weight of objects and you have multiple objects to carry, but you want to maximize the value of the things you carry as well (e.g. a kapsack that can only hold 5LBS, but you have a laptop(2LBS, $2000), stereo(4LBS, $3000), and a monitor(3LBS, $1500))

* A simple algo would have us try every possible set of goods and find the set that gives the most value, which works but is slow (O2^n)

* We can get an approximate solution with Greedy algos, but we might be able to get an even more optimal solution with dynamic programming

* For our problem above we would break it up into a grid with the items we want to fit into the knapsack along the Y and the amount of space in LBS we have UP TO AND INCLUDING THE MAX VALUE(in this case 1, 2, 3, 4, 5 would go along the X axis)

* Each row is one of the items and each column is the amount of space we have

* So for 1LBS, laptop, the max value we could put in there is nothing, since the laptop won't fit, for 2LBS, laptop we can put the laptop in there so the max value we could have is $2k, for 3LBS, laptop it again would be a max value of $2k, contine on like this for the rest of the row until you reach the end of the line, then move down to the next row of stereo, and start again.  

* When we get to the point of where we can fit multiple things in the knapsack, we now only need to look back at the previous table rows to figure out the maximum value we can fit into a limited amount of space.

* The order of the rows doesn't matter, and the value of the rows/cells can't decrease, and you can always add another row for another item.  

* With the knapsack problem you either take the item or you don't, you can't take half or a quarter of an item.  

* You can make the columns more granular to include half/quarter pounds etc... if you so choose

* Dynamic programming only works when each subproblem is unique/discrete(AKA: Dynamic programming only works when it does not depend on other subproblems)

* Dynamic programming is useful when you're trying to optimize something given a constraint.  (e.g. maximize the value of the goods stolen, constrained by the size of the knapsack)

* Some tips to come up with a dynamic programming solution:

```
- Every dynamic programming solution involves a grid

- The values in the cells are usually what you're trying to optimize(e.g. the value of the goods in the knapsack problem)

- Each cell is a subproblem, so think about how you can divide you problem into subproblems(this will help you figure out what the X/Y axis are supposed to be)

* You can also use dynamic programming to figure out the longest common substring/subsequence


* Dynamic programming is used for things like git diff and word wrap in text programs.

* Recap:

```

- Dynamic programming is useful when you're trying to optimize something given a cosntraint

- You can use dynamic programming when the problem can be broken into discrete subproblems

- Every dynamic programming solution involves a grid

- The values in the cells are usually what you're trying to optimize

- Each cell is a subproblem, so think about how you can divide you problem into subproblems

- There is no single formula for calculating a dynamic programming solution

```



### Grokking Algos Ch 10: K-nearest neighbors

* K-Nearest Neighbors(KNN) is useful for things like recomendation engines.

* KNN starts out by plotting every user on a graph, plotted by similarity so that those with similar tastes are plotted closer together.  

* Feature extraction is a unique set of characteristics of a user or node that is being graphed(e.g. how much they liked X movie, or how highly they rate X type of music)

* If we're calculating these on a graph we can use the distance formula if we have 2 x points and 2 y points, but what happens if we have a lot more x/y points(e.g. ratings)?

* For more x/y points the distance formula stays the same, but instead of distance it tells us how similar the set of numbers we plugged into the formula are.   

* The average of a set of multiple ratings is a regression

* With KNN, there are 2 basic things you'll do:

```

Classification: Categorization into a group

Regression: Predicting a response


```

* With a set of features (e.g. ratings), that we can compare to a past set of features and their outcomes we can predict(with some accuracy) what someone may like, etc...(Think econometrics).

* Another common formula used with KNN is Cosine Similarity(Outside the scope of Grokking Algos)

* Part of the magic of KNN is picking good features, e.g. those that correlate directly to the movies you're trying to recommend.  

* Good features don't have bias/minimized bias, and correlate to to the movies you're trying to recommend.

* KNN is an example that can lead to machine learning, the first step of any machine learning algo is training.  E.g taking a set of data and using an algo to determine how correct/incorrect it is on a given set of data.  

* Recap:

```

* KNN is used for classication and regression and is used for looking at the KNN.

* Classication is categorization into a group, while regression is used for prediction(like a number)

* Feature extraction means converting an item into a list of numbers/features/characteristics into a list of numbers that can be compared

```

### Grokking Algos Ch 11: Where to go Next

* Trees

```

With binary search trees for every node, the nodes on the left are smaller in value and the nodes on the right are larger in value.

On average a binary search tree is better for insertions/deletions O(log(n))

The downside(s) to a BST is that you don't get random access(e.g. no indicies), and an imbalanced tree will have bad performance.  

Trees like Red-Black trees balance themselves, another type of tree that's commonly used in databases is/are B-trees.  Other types of trees incldue Heaps, and Splay trees

```

* Inverted Indexes


```

Inverted indexes are keys in a hash table(usually words), and the values are places where those words appear(usually sites/pages).  

```

* Fourier transform

```

Fourier transforms are great for compression, and signals processing.  A foruier transform can take a whole thing(say a loaf of bread for example), and tell you the individual parts that make it up(the ingredients, and how much of each ingredient, in our example).

```

* Parallel algos

```

As there get to be more and more cores in CPUs we need to run programs/algos across multiple cores(parallelism).  

Parallel algos are tricky, and the performance/time gains aren't linear(e.g. if you have 2 cores rather than 1, it's unlikely that the algo will run twice as fast).  

The reason for non-linear performance gains are because of the overhead of managing parallel processes since splitting things up and merging them back together takes time/resources.  There's also the issue of load balancing(i.e. how do you make sure all cores are working equally hard to avoid idle time).



```

* Map reduce

```

Distributed algos are for algos that run across hundreds of cores in supercomputers etc... often using tools like Apache Hadoop

If you have a very large/"big data" table that you want to run a SQL query on.  mySQL probably won't work because it struggles after a few billion rows, this is where MapReduce comes in, or in a case where you have a long list of jobs that take ten seconds each, doing it on one machine would take a months, but spread out across a hundred machines, that job lis would take a few days.  

MapReduce as the name implies is centered around the Map function, and the Reduce function.  

The map function takes an array and applies the same function to each item in the array.  e.g.(arr1 = [1, 2, 3, 4] arr2 = (lambda x: 2 * x, arr1))

If we had a large project that used map that was resource intensive, we might want to spread this project out over a hundred machines or so

The reduce function reduces a whole list of items down to one item given a function(e.g. arr1= [1, 2, 3, 4, 5] reduce(lambda x,y: x + y, arr1) # adding all of the numbers together)

MapReduce uses the above two concepts to run queries about data across all the machines used when you have a large dataset


```

* Bloom filters and HyperLogLog


```

Suppose you want to figure out if an item is unqiue(e.g. a link posted to Reddit, or to see if you've already crawled a link before, or running a URL shortner and want to avoid liking to malicious websites that you already have in a set/list)

The above situations are a subset of the same problem, you want to check a new item against an already existing set of items.  While this could be done with a hash with a small enough dataset, if you have a HUGE dataset, this becomes an issue because of space considerations.

Bloom filters are a probablistic data structure that will give you an answer that could be wrong, but is probably correct.  Instead of a hash you check with the bloom filter, which might give you false positives(e.g. you've already crawled this site) but will NOT give you false negatives(e.g. if the filter says you haven't crawled the site, then you haven't crawled the site)

Bloom filters take up very little space for large datasets, even less than a hash table

For HyperLogLog, an algorithm, it is useful to count things like number of unique searches performed in a given set of time, or number of unique items looked at in a day(e.g. Google or Amazon).  For a normal log if the item is not in the log you add it, but for examples like Amazon/Google the logs would be massive.  

HyperLogLog approximates the number of unique elements in a set.  Like bloom filters, this will not give you an exact answer, but it comes close and only 

```
* The SHA Algos

```

Hash Functions:
If you have a key and want to put the associated value in the array, you use a hash function to tell what index to put the value in, and put the value in that index.  This concept allows you to do constant-time lookups, when you want to know the value for a key, you can use the hash function again, and it will tell you in O(1) time what slot to check.

SHA algo:
Given a string, SHA gives you a hash for that string.  Keep in mind SHA is a hash function that generates a hash(AKA: a short string).  The hash function function for hash tables went from a string to an array index, whereas SHA goes from string to string.  SHA generates a different hash for every string.

SHA is useful for file and password comparisons.  As SHA is a one way function, even if you get the SHA you can't convert it back to the original string.  

SHA is also locaility insensitive, meaning that you if you change one character/feature of the string, and generate a new hash, it's totally different.  

Simhash is a locality senstive hash algo, meaning that if you make a small change to a string, it will generate a hash that's only a little different.  (A teacher could use simhash to detect whether a student was copying an essay from the web, Google uses simhash to detect duplicates while webcrawling)

```

* Diffie Hellman Key Exchange

```

Diffie-Hellman solves the problem of "how do you encrypt a message so it can only be read by the person you send it to?"

With DHKE, both parties don't need to know the cipher, so parties don't need to meet and agree what the cipher should be, and the encrypted messages are still extremely hard to crack.  

DHKE uses a public key and a private key.  The public key is public, but the private key is one only known to you.  

DHKE is succeded by RSA.  
```

* Linear programming


```

Lienar programming is used to maximize something given constraints.  Graph problems are a subset of linear programming.  

Linear programming uses the Simplex algo(ironically enough) and is related to optimization theory.  

```

