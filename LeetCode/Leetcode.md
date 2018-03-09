# Leetcode Problems in Python

### Question 1: twoSum


* Question:


Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

return [0, 1]



```Python3


    def twoSum(self, nums, target):
  
        # initialize dict
        lookup = {}

        # Loop through with a counter associated w/ each item(a num in nums)
        for counter, item in enumerate(nums):

            # If we find what we want in lookup, we can return that items key and the count 
            if target - item in lookup:
                return lookup[target-item], counter

            lookup[item] = counter 


```

* Solution Explanation/thought process:

This one was a challenge in a good way and I really liked it.  Originally I wanted to use nested for loops with a second array of [1:], but after that failed consistently, I admittedly looked up the answer after struggling with this for 45 minutes.  The answer makes sense, but was slightly non-intuitive for me as it requires using the target(AKA: solution/answer) as part of the answer in the code.  But overall this should have a runtime of O(n) and a space complexity of O(n) due to using the loop and having to store the list, but luckily dictionaries have an O(1) lookup time.  



***
