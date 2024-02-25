# A program to extract data from a JSON url
import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    address = input("Enter location: ")
    url = urllib.request.urlopen(address, context=ctx).read()
    print('Retrieving', address)
    print('Retrieved', len(url), 'characters')

    # Load the JSON file
    info = json.loads(url)
    res = info['comments']

    count_val = []
    for i in res:
        c = i['count']
        count_val.append(c)
        count = len(count_val)
    print('Count:', count)

    lst = []
    for j in count_val:
            x = int(j)
            lst.append(x)
            print(x)
            total = sum(lst)
    print('Sum:', total)

except:
    print('Not a valid URL, try again.')
