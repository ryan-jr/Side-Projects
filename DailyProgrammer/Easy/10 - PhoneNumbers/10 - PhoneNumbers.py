# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:55:20 2018

@author: rjr
"""

# A mostly completed regex for 
# https://www.reddit.com/r/dailyprogrammer/comments/pv98f/2182012_challenge_10_easy/


import re




ptn = "1234567890"

ptns = ["1234567890", "123-456-7890", "123.456.7890", "(123)456-7890", "(123) 456-7890", "456-7890", "123-45-6789", "123:4567890", "123/456-7890"]


for i in ptns:
    # Forcing no matches for certain cases because, well, regex.
    
    i = i.replace(":", "XX")
    i = i.replace("/", "XX")
    try:
        regex = re.match(r"\D?(\d?\d?\d?)[?\s^\D?]?[\s?\-?\.?\)?]?(\d\d\d)\D?(\d\d\d\d)", i )
        print("Valid!", regex.groups())
    except:
        print("No match!")





