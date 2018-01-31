# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:07:35 2018

@author: rjr
"""

# XKCD

import requests, os, bs4

# Start the URL and store the comics
url = "https://www.scfta.org/events/detail.aspx?id=16205"
os.makedirs("xkcd", exist_ok = True)

# Download the page
while not url.endswith("#"):
    print("Downloading... %s..." % url)
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text)
    
    # Find the URL of the comic
    comicElem = soup.select("#comic img")
    if comicElem == []:
        print("Could not find an image")
    else:
        comicUrl = "http:" + comicElem[0].get("src")
        # Download the image
        print("Downloading image %s..." % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save the image to the folder
        
        imageFile = open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb")
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    
    # Get the Prev button's URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = "http://xkcd.com" + prevLink.get("href")




print("done")