# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 22:27:50 2022

@author: AlexChen
"""

import requests
url = "http://m.ip138.com/ip.asp?ip="
kv = {'user-agent': 'Mozilla/ 5.0'}
try:
    r = requests.get(url+'202.204.80.112', headers=kv)
    print("Return status is", r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
	print("Scrapy failed")
    #My IP address at Ningbo: 39.188.240.63
	