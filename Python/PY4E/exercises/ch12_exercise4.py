#Use urllib to retrieve the total number of paragraphs
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

size = 0
tags = soup('p')
for tag in tags:
    size = size + len(tag)
print('There are,', size, 'paragraphs in this document')
