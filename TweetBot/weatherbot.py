# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 20:59:27 2018

@author: rjr



"""

import json
import requests 
import config
import tweepy
import datetime
import time



apiUrlBase = "http://api.openweathermap.org/data/2.5/weather?id="


def getInfo(apiUrlBase, weatherID="2172797"):
    apiUrl = apiUrlBase + weatherID + "&appid=" + config.weatherApiKey + "&units=imperial"
    response = requests.get(apiUrl)
    
    
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        return None
    
  
def getApi():
    auth = tweepy.OAuthHandler(config.twitterApiKey, config.twitterSecret)
    auth.set_access_token(config.twitterToken, config.twitterTokenSecret)
    return tweepy.API(auth)


#File the bot will tweet from
filename = open('weatherIDs.txt','r')
f = filename.readlines()
filename.close()


# Loops through the file constantly to get the data and update the Twitter account

while True:
    for count, data in enumerate(f):
        # Setting the variables we want
        helloString = "Hey there "
        a = datetime.datetime.now()
        timeData = ("The time is: %02d:%02d" % (a.hour, a.minute))
        indicator = ["AM", "PM"]
        meridiem = ""
        if a.hour < 12:
            meridiem = indicator[0]
        else:
            meridiem = indicator[1]
        
        # Getting the information
        weatherData = getInfo(apiUrlBase, str(data[:7]))
        weatherInfo = weatherData["main"]["temp"]
        
        # Formatting the string and sending out the tweet
        tweet = helloString + str(data[8:-1])  + ".\n" + str(timeData) + meridiem + " ,and the temperature is", str(weatherInfo), "degrees fahrenheit."
        print(" ".join(tweet))
        #api = getApi() 
        #status = api.update_status(status = " ".join(tweet))
        time.sleep(10)
    
    







"""


print(data)
print(data["main"]["temp"])


idData = listData
print(idData[0]["id"], idData[0]["name" ])
print(listData[0])


for count, element in enumerate(idData):
    print(count, idData[count]["id"], idData[count]["name"], idData[count]["main"])
    file = open("weatherIDs.txt", "a")
    file.write(str(idData[count]["id"]))
    file.write("\n")
    file.close()
"""