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



So this one was pretty straightforward since I have a handle on recursion, but the thing that threw me at first was returning FirstFactorial(num * num - 1), when I needed to only get the factorial of the second term.  For me, in this instance recursion feels naturaly, but it's also possible to use the iterative version of this



***
