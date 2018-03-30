# Creating the basic outline of a task manager
import datetime 

  # TODO: Add email support
  # TODO: Add MT/ST support
  # TODO: Add editing/deleting

class Card(object):
  
  def __init__(self, time, lt = [], mt = [], st = []):
    self.time = time
    self.lt = lt
    self.mt = mt
    self.st = st
    
  def addLT(self, time, data):
    dataHolder = (time, data)
    self.lt.append(dataHolder)

  def addMT(self, time, data):
    print("Hello, the current time is:", datetime.datetime.now())
    print("*" * 100)
    print("Intermediate term tasks")
    print(self.lt)
    
  
  def addST(self, time, data):
    print("Hello, the current time is:", datetime.datetime.now())
    print("*" * 100)
    print("Short term tasks")
    print(self.st)
    
    
  def display(self):
    print("Hello, the current time is:", datetime.datetime.now())
    print("*" * 100)
    print("Long term tasks")
    print(self.lt)
    
    
    
newCard = Card(datetime.datetime.now())



while True:
  print("1.  Add a new short term Task")
  print("2.  Add a new intermediate term Task")
  print("3.  Add a new long Term Task")
  print("4.  Display your tasks for today")
  print("5.  Email your tasks for today")
  print("")
  print("6.  Quit")
  x = int(input(">>>"))

  if x == 1:
    print("OK, input your short term task:")
    x = str(datetime.datetime.now())
    data = input(">>>")
    newCard.addST(x, data)
    print("Task added!")
    continue

  if x == 2:
    print("OK, input your intermediate term task:")
    x = str(datetime.datetime.now())
    data = input(">>>")
    newCard.addMT(x, data)
    print("Task added!")
    continue

  if x == 3:
    print("OK, input your long term task:")
    x = str(datetime.datetime.now())
    data = input(">>>")
    newCard.addLT(x, data)
    print("Task added!")
    continue

  if x == 4:
    newCard.display()

  if x == 5:
    pass

  if x == 6:
    break

