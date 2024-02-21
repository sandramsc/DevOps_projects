#Scraping Numbers from HTML using BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
lst = []
tags = soup('span')
for tag in tags:
    tag = tag.contents[0]
    lst.append(tag)
    count = len(lst)
print('Count', count)

nlst = list()
# convert the strings to integers
for i in lst:
    c = int(i)
    # create a list of integers
    nlst.append(c)
    total = sum(nlst)
print('Sum',total)
