# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 08:06:20 2017

@author: rjr
"""


# Creating a web scraper for r/dailyprogrammer

# Step 1: Import the scraper (scrapy, BS4?, requests?)
# Step 2: Have it scrape the first page of dailyprogrammer
    #2A: Commit the text that is scraped to a file
# Step 3: Have it scrape additional pages


"""
TODO: An interesting project I came across: https://github.com/stanfordjournalism/search-script-scrape



Ok doing some quick research it looks like Scrapy is what I need, judging by:
https://stackoverflow.com/questions/19687421/difference-between-beautifulsoup-and-scrapy-crawler

"""



import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content)
titles = soup.find_all(class_ = "title")
selectors = soup.select("td.title")

#print(soup)
print(selectors)
print(soup.get_text())


url2 = "https://news.ycombinator.com/news?p=2"
r = requests.get(url2)
soup = BeautifulSoup(r.content)
titles = soup.find_all(class_ = "title")
selectors = soup.select("td.title")

#print(soup)
print(selectors)
print(soup.get_text())




  

