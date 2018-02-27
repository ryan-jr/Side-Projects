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