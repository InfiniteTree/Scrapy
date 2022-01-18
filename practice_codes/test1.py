# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 07:09:38 2022

@author: AlexChen
"""

import time
import requests

# INPUT: i - the number of time to get url
#        website - the url to scrape
def getHTTP(i, website):
    try:
        r = requests.get(website)
        r.raise_for_status() # checke for exception
        r.encoding = r.apparent_encoding
        return i
    except:
        return "Exception Error"

#test = 'https://www.zhihu.com/question/19717038'
test = input("Please enter an url\n")
trytime = input("Please enter the time to scrape the website\n")
trytime = int(trytime)


start_time = time.time()
for i in range(trytime):
    print("\r",getHTTP(trytime+1,test),end="")
print('\n')
end_time = time.time()
cost_time = start_time - end_time
print("The cost time is",cost_time)
        