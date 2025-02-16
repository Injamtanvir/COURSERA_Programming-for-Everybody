# InjamTanvir(INJAM UL HAQUE)


# An HTTP Request in Python
'''
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()  # Utf-8
mysock.send(cmd)  # In Bytes

while True:
    data = mysock.recv(1000)
    if len(data)<1:
        break
    print(data.decode())
mysock.close() 
'''


# An HTTP Request in Python
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

print("==========================================")

# An HTTP Request in Python
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
