# Extracting Data from XML link

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
try:
    url = input('Enter location: ')

    uh = urllib.request.urlopen(url, context=ctx).read()
    print('Retrieving', url)
    print('Retrieved', len(uh), 'characters')
    #print(uh.decode())
    tree = ET.fromstring(uh)
    res = tree.findall('.//count')

    # check if there is a text value in each count tag
    count_val = []
    for i in res:
        if i.text is not None:
            count_val.append(i.text)
            count = len(count_val)
    print("Count:", count)

    # calculate the sum
    lst = []
    for c in count_val:
        if len(c) > 0:
            x = int(c)
            lst.append(x)
            total = sum(lst)
    print("Sum:", total)
except:
    print("Not a valid URL, try again...")
