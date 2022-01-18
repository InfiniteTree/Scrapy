# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 21:08:14 2022

@author: AlexChen
"""
import requests
import os
url = 'https://cj.jj20.com/2020/down.html?picurl=/up/allimg/1113/092919113248/1Z929113248-8.jpg'
root = 'C://Users//AlexChen//Desktop//Sp//photos//'
path = root + url.split('/')[-1]
kv = {'user-agent':'Mozilla/5.0'}


try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url,headers = kv)
        with open(path, 'wb') as f:
            write(r.content)
            f.close()
            print("File saved successfully")
    else:
        print("File existing already")
except:
    print("Scrapy Failed")
    print("The header of request is", r.request.headers)
