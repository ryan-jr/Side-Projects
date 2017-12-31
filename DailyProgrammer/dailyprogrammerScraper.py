import re

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 09:20:46 2017

@author: rjr
"""


# Creating a web scraper for r/dailyprogrammer

# Step 1: Import the scraper (scrapy, BS4?, requests?)
# Step 2: Have it scrape the first page of dailyprogrammer
    #2A: Commit the text that is scraped to a file
# Step 3: Have it scrape additional pages
    #3A: Grab the next link, pass it to the urllib
    #


"""
TODO: An interesting project I came across: https://github.com/stanfordjournalism/search-script-scrape



Ok doing some quick research it looks like Scrapy is what I need, judging by:
https://stackoverflow.com/questions/19687421/difference-between-beautifulsoup-and-scrapy-crawler


https://stackoverflow.com/questions/27652543/how-to-use-python-requests-to-fake-a-browser-visit/27652558

Grabbing all the title links
https://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautifulsoup (3rd answer: or the Python 3 version:)


Helping me grab the next link:
    https://stackoverflow.com/questions/41908426/extracting-deeply-nested-href-in-python-with-beautiful-soup
    
    
finding string partials:
    https://stackoverflow.com/questions/14849293/python-find-index-position-in-list-based-of-partial-string



Super helpful for associating the correct URL with the correct post:
https://stackoverflow.com/questions/2407398/how-to-merge-lists-into-a-list-of-tuples
https://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python

Helpful for zipping everything together:
    https://www.reddit.com/r/learnpython/comments/10kuw5/why_is_using_zip_giving_me_zip_object_at/?st=jbu5r8sm&sh=d4aa5692
    
Now finding stuff in the tuple:
    https://www.w3resource.com/python-exercises/tuple/python-tuple-exercise-14.php
    
    
I really need to use in and not in more:
    https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
    
    
data validation/scrubbing is certainly a thing...I just lost a half hour because
the right prepend wasn't in place, so it was making the zip off by one

These numbers are annoying the crap out of me right now:
    print(len(dateList))        # 144
print(len(difficultyList))  # 142
print(len(idList))          # 144
print(len(titleList))       # 144

     That's because the difficulty list is off by two for some reason....ugh
     
...Turns out I had to remove the weekly, monthly, and mini challenges...sorry :(

        
Finally got everything sorted out and put into a final list

"""



import requests
from bs4 import BeautifulSoup
import random as rand
import time

def getPage(url, headers):
    
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.content)
    f = open("dailyprogrammerOutput.txt", "a")
    
    
    dataList = ["share", "javascript: void 0;", "save", "#", "hide", "report"]
    
    for title in soup.find_all("div", class_ = "top-matter"):
        for link in title.find_all("a", href = True):
            linkText = link.get_text()
            linkHref = link["href"]
            
            if linkText in dataList:
                pass
            elif linkHref in dataList:
                pass
            else:
                f.write(linkText)
                f.write("\n")
                f.write(linkHref)
                f.write("\n")
    
    for link in soup.find_all("span", class_ = "next-button"):
        url = link.find("a")["href"]

    
    f.close()
    print(url)
    return(url)

url = "https://www.reddit.com/r/dailyprogrammer/"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}



for x in range(0, 9):
    url = getPage(url, headers)
    randomInteger = rand.randint(10, 31)
    print(randomInteger)
    time.sleep(randomInteger)
    
        









        
    
        
        








#print(soup.get_text())
#print(titles.get_text())

""""
url2 = "https://news.ycombinator.com/news?p=2"
r = requests.get(url2)
soup = BeautifulSoup(r.content)
titles = soup.find_all(class_ = "title")
selectors = soup.select("td.title")

#print(soup)
print(selectors)
print(soup.get_text())
"""


  

