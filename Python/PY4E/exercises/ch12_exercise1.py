import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    url = input("Enter URL: ")
except:
    print("Invalid URL, try again...")
else:
    connects = re.findall('http[s]?://(.*)/.*' ,url)
    for line in connects:
        string = str(line.rstrip())
        #link = string.split('/')
    #print(string)
    mysock.connect((string, 80))
    x = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    cmd = x.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print (data.decode())
    mysock.close()
