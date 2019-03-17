from bs4 import BeautifulSoup
import urllib
import urllib.request
import re
import wikipedia
import time
import cv2
from GetSearchName import searchname
from basic import cleanup
def search(query):
    address = "http://www.bing.com/search?q=%s" % (urllib.parse.quote_plus(query))
    print(address)
    getRequest = urllib.request.Request(address, None, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})
    urlfile = urllib.request.urlopen(getRequest)
    htmlResult = urlfile.read(200000)
    urlfile.close()
    soup = BeautifulSoup(htmlResult,'lxml')
    [s.extract() for s in soup('span')]
    results = soup.find_all('li', { "class" : "b_algo" })
    for result in results:
        if result is not None:
            links = str(result.find('a' ).get('href'))
            print (links)
            wikilink = " "
            if 'wikipedia' in  links:
                wikilink = links
                break;
    url = wikilink
    print(url)
    url = re.split("\/" , url)
    tag = url[len(url)-1]
    print(tag)
    textdata = wikipedia.summary(tag)
    return textdata



text = searchname()
searchtext = text + "wikipedia"
textdata = search(searchtext)
print(textdata)
cleanup()
import shutil
import os
shutil.rmtree('E:\Python\Selenium\ImagetobeSearched')
os.mkdir('ImagetobeSearched')
"""image = cv2.imread('full.jpg')
image = cv2.resize(image,(800,600))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, textdata, (100,100), font, 1, (0, 255, 0), 1, cv2.LINE_AA)
cv2.imshow("IMage",image)"""
