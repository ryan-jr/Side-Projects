# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:28:35 2018

@author: rjr
"""

#! python3
# lucky.py - Opens Google search results for us

import requests, sys, webbrowser, bs4

# Display something while working
print("Googling....")

res = requests.get("http://google.com/search?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links

soup = bs4.BeautifulSoup(res.text, "lxml")

# TODO: Open a browser tab for each result

linkElems = soup.select(".r a")
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open("http://google.com" + linkElems[i].get("href"))
    
    



