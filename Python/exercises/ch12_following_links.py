#Follow a link, print the next link based on index
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
start_pos = int(input('Enter position: '))
count = int(input('Enter count: '))
print("Retrieving:",url)
for _ in range(count):
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve all of the anchor tags
        tags = soup('a')
        if len(tags) == 0:
             print("No links found.")
             break
        # Ensures the starting position does not exceed the length of the tags
        start_pos = start_pos % len(tags)

        # Gets the next link
        url = tags[start_pos - 1].get('href', None)
        print("Retrieving:",url)

    except Exception as e:
            print("Error fetching content:", e)
            break
