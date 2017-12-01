# Reddit both that explains XKCD strips in comments

from bs4 import BeautifulSoup
from urllib.parse import urlparse

import praw
import time
import re
import requests
import bs4

# Location of file where ID's of already visited comments are maintained
path = '/home/ryan-jr/Projects/explainbot/commented.txt'

# Posted along with the comic description
header = 'Explanation of this XKCD: \n'
footer = '\n THis explanation was extracted from [explainXKCD](http://www.explainxkcd.com) | Bot created by u/echo419Test \n'



def authenticate():
'''
* Authentication function
* Takes no input
* Returns reddit variable that provides the user instance to the Reddit API
'''
	print("Authenticating... \n")
	reddit = praw.Reddit('explainbot', user_agent = 'web:xkcd-explain-bot:v0.1' (by u/echo419Test))
	print("Authenticated as {}\n".format(reddit.user.me()))
	return reddit



def fetchdata(url):
'''
* Function to retrieve data
* Takes the site URL as input
* Returns data retrieved from the page
'''
	r = requests.get(url)
	soup = BeautifulSout(r.content, 'html.parser')

	tag = soup.find('p')
	data = ''
	while True:
		if isinstance(tag, bs4.element.Tag):
			if(tag.name == 'h2'):
				break
			if (tag.name == 'h3'):
				tag = tag.nextSibling
			else:
				data = data + '\n' + tag.next 
				tag = tag.nextSibling
		else:
			tag = tag.nextSibling

	return data

