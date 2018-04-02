# Notes

### Section 1

```Python3
# List comprehension notes
List comprehensions allows us to create lists programatically, but also manipulate them at the time of creation e.g. [x * 3 for x in range(5)] # 0, 3, 6, 9, 12

List comprehensions also allow us to easily include conditions on what/what not to include e.g. [x for x in range(10) if x % 2 ==  0]

We can also chain methods in list comprehensions:
  people = ["bob", "SUSAN", " gR Eg"]
  normalPeople = [person.strip().lower() for person in people] # ["bob", "susan", "greg"]
  
Keep in mind with list comprehensions the tradeoff between readability and code complexity 

```
