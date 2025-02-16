import socket
website = input('Enter the website host name: ')
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((website, 80))