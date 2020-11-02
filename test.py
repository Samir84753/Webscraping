import bs4 as bs
# from bs4 import BeautifulSoup
import re
import requests
import random
r=requests.get('https://en.wikipedia.org/wiki/The_Boys_(2019_TV_series)')

soup=bs.BeautifulSoup(r.content,'html5lib')
# print(soup.prettify()
# print(soup.find_all('p'))
title=soup.find("title")
print(title.string)

t=[]
for head in soup.find_all('h2'):
    for s in head.find_all('span',attrs={"class":"mw-headline"}):
        t.append(s.text)
for text in soup.find_all('p'):
    print((text.get_text()))
    
# summary=soup.find_all('div',attrs={"id":"content"})
# # print(summary)
# for para in summary:
#     print(para.find('p').text)


# print(soup.get_text())
# fp=open('wiki.txt','w+')
# fp.write(soup.get_text())



