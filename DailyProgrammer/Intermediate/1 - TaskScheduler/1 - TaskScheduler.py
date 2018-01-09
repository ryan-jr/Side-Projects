# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:50:16 2018

@author: rjr
"""

"""
https://www.reddit.com/r/dailyprogrammer/comments/pihtx/intermediate_challenge_1/?st=jc809oci&sh=66413241

create a program that will allow you to enter events organizable by hour. There must be menu options of some form, and you must be able to easily edit, add, and delete events without directly changing the source code.

(note that by menu i dont necessarily mean gui. as long as you can easily access the different options and receive prompts and instructions telling you how to use the program, it will probably be fine)
"""


def addEvent(events):
  print("Please enter events based on a 24 hour clock (HH:XX)")
  userHour = input("Please enter the hour that you want the event to take place:")
  userEvent = input("Please enter the event you want at that hour/time period:")
  
  if len(userHour) <= 2:
    userHour += ":00"
    print(userHour)
    
  for k, v in events.items():
    if userHour == k:
      v.append(userEvent)
      print(userEvent, "added at", k, "!")
  
  return events
  

def editEvent():
  pass

def deleteEvent():
  pass

def displayEvents(events):
  for k, v in events.items():
    if v == []:
      pass
    else:
      print(k, v)
      print()

def printMenu(menu):
  for k, v in menu.items():
    print(k, end = ":")
    print(v)
  
  
masterDict = {
  "24:00": [],
  "01:00": [],
  "02:00": [],
  "03:00": [],
  "04:00": [],
  "05:00": [],
  "06:00": [],
  "07:00": [],
  "08:00": [],
  "09:00": [],
  "10:00": [],
  "11:00": [],
  "12:00": [],
  "13:00": [],
  "14:00": [],
  "15:00": [],
  "16:00": [],
  "17:00": [],
  "18:00": [],
  "19:00": [],
  "20:00": [],
  "21:00": [],
  "22:00": [],
  "23:00": [],
}

menuDict = {
            "A": " Add an event",
            "E": " Edit an event",
            "D": " Delete an event",
            "S": " Show all events",
            "Q": " Quit the program"
}

userInput = ""

while userInput != "Q":
  print("please enter your selection...")
  printMenu(menuDict)
  print()
  userInput = input(">>>")
  if userInput == "A":
    print("Add event!")
    masterDict = addEvent(masterDict)
  elif userInput == "E":
    print("Edit event!")
    editEvent()
  elif userInput == "D":
    print("Delete event!")
    deleteEvent()
  elif userInput == "S":
    print("Showing events")
    displayEvents(masterDict)
  
  
  


