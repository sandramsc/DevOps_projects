#Use urllib to retrieve the total number of characters
import socket
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
url = 'http://data.pr4e.org/romeo.txt'
html = urllib.request.urlopen(url, context=ctx).read()
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(html)

size = 0
while True:
    data = mysock.recv(3000)
    if len(data) < 1: break

    size = size + len(data)
    print(size, 'total number of characters')
mysock.close()
