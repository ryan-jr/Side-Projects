# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:06:04 2018

@author: rjr
"""

import os 
import glob 


# trying to compile every word list
# 10
for filename in glob.glob("*.10"):
    if filename == "twenty.py":
        pass
    else:
        with open(filename, "r") as f, open("belowSeventy", "a") as f1:
            print(filename)
            f1.write(f.read())
  

# 20

for filename in glob.glob("*.20"):
    if filename == "twenty.py":
        pass
    else:
        with open(filename, "r") as f, open("belowSeventy", "a") as f1:
            print(filename)
            f1.write(f.read())
# 35 
for filename in glob.glob("*.35"):
    if filename == "twenty.py":
        pass
    else:
        with open(filename, "r") as f, open("belowSeventy", "a") as f1:
            print(filename)
            f1.write(f.read())


# 40
for filename in glob.glob("*.40"):
    if filename == "twenty.py":
        pass
    else:
        with open(filename, "r") as f, open("belowSeventy", "a") as f1:
            print(filename)
            f1.write(f.read())

# 50 
for filename in glob.glob("*.50"):
    if filename == "twenty.py":
        pass
    else:
        with open(filename, "r") as f, open("belowSeventy", "a") as f1:
            print(filename)
            f1.write(f.read())

# 55
for filename in glob.glob("*.55"):
    if filename == "twenty.py":
        pass
    else:
        with open(filename, "r") as f, open("belowSeventy", "a") as f1:
            print(filename)
            f1.write(f.read())

# 60      
for filename in glob.glob("*.60"):
    if filename == "twenty.py":
        pass
    else:
        with open(filename, "r") as f, open("belowSeventy", "a") as f1:
            f1.write(f.read())
