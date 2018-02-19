"""

https://www.reddit.com/r/dailyprogrammer/comments/qr0hg/3102012_challenge_22_easy/

[3/10/2012] Challenge #22 [easy]

Write a program that will compare two lists, and append any elements in the second list that doesn't exist in the first.

input: ["a","b","c",1,4,], ["a", "x", 34, "4"]

output: ["a", "b", "c",1,4,"x",34, "4"]

"""

# First solution (uses sets)
a = ["a","b","c",1,4,]
b = ["a", "x", 34, "4"]

a = set(a)
b = set(b)

print(a | b)


# Second Solution (uses list comprehension)
a = ["a","b","c",1,4,]
b = ["a", "x", 34, "4"]

c = a + [item for item in b if item not in a]
print(c)

# Thrid solution (uses for loop)
d = a
for item in b:
  if item not in a:
    d.append(item)

print(d)