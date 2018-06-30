# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 00:12:10 2018

@author: avengers
"""

import re
import urllib.request

arrayofStocks=['FB','GOOG','DATA','BABA']

url=url+stock

data=urllib.request.urlopen(url).read()
data1=data.decode("utf-8")

m=re.search('"meta itemprop="price"',data1)
start=m.start()
end=start + 50
newString=data1[start:end]

m=re.search('content="',newString)
start=m.end()
newString1=newString(start:)
m=re.search("/",newString1)
start=0
end=m.end()-3
final=newString1[0:end]
print('the value of stock.upper()+'is'+final)