# InjamTanvir(INJAM UL HAQUE)


'''##################################### ===> Python Regualr Expression Example CODEs ######################################'''

import re 

inp = input("Please enter the File name(which you want to count all the numbers on the file): ")
hand = open(inp)

count = 0
sum = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)   # There a string list was create every time to store the number value on a line
    # print(x)
    for i in x:
        count = count + 1
        sum = sum + int(i)

print(f'There are {count} values with a sum={sum}')

# regex_sum_42.txt --> There are 90 values with a sum=445833
# regex_sum_1717171.txt --> There are 109 values with a sum=474216




'''##################################### ===> An HTTP Request in Python using Urllib ######################################'''

# An HTTP Request in Python
import urllib.request, urllib.parse, urllib.error

inp = input("Enter the URL: ")
fhand = urllib.request.urlopen(inp) # This will work as a file handle

for line in fhand:
    print(line.decode().strip())





'''##################################### ===> using the socket library to create a network connection and retrieve data from a web server ######################################'''

# Socket Connection
import socket
website = input('Enter the website host name: ')
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((website, 80))


# Code to GET Data from the Web Server using Link
import socket
import ssl

url = input("Please Enter the URL or Website Link: ")

try:
    # Parse the URL to extract host and path
    if url.startswith("http://"):
        url = url[7:]  # Remove 'http://'
        port = 80  # Default port for HTTP
    elif url.startswith("https://"):
        url = url[8:]  # Remove 'https://'
        port = 443  # Default port for HTTPS
    else:
        print("Unsupported URL format. Please include 'http://' or 'https://'.")
        exit()

    # Split the URL into host and path
    parts = url.split('/', 1)
    host = parts[0]
    if len(parts) > 1:
        path = '/' + parts[1] 
    else:
        path = '/'

    # Create a socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the socket with SSL for HTTPS
    if port == 443:
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        mysock = ctx.wrap_socket(mysock, server_hostname=host)

    # Connect to the server
    mysock.connect((host, port))

    # Send the HTTP GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    mysock.send(request.encode())

    # Receive and print the response
    response = b"" # Empty byte object
    while True:
        data = mysock.recv(10000)
        if not data:
            break
        response += data

    # Decode and print the response
    print(response.decode())

    # Close the socket
    mysock.close()

except Exception as e:
    print(f"An error occurred: {e}")





'''##################################### ===> An HTTP/HTTPS Request in Python using Beautifulsoup - Extract Link(anchor tag) from the input page ######################################'''

# Beautiful Soup is a Python library for pulling data out of HTML and XML files.
#Website link --> https://pypi.org/project/beautifulsoup4/ 
# In terminal paste this code and run it: pip install beautifulsoup4 or i have a folder name "BeautifulSoup4" in that folder.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors (https)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the URL: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags  # a is the tag for anchor
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))  # None is the default value 





'''##################################### ===> Extracting DATA From XML (Find all Count tags and sum up there values) ######################################'''

import urllib.request   # urllib.request --> Using this we can read data from Internet
import xml.etree.ElementTree as ET   # xml.etree.ElementTree --> Using this we can parse XML Data

url = input('Please Enter location: ')
if len(url) < 1:
    url = 'https://py4e-data.dr-chuck.net/comments_42.xml'  # Default URL for testing --> For this Answer will be: 
                                                                                            # Retrieved 4189 characters
                                                                                            # Count: 50
                                                                                            # Sum: 2553

print('Retrieving', url)

# Fetch the XML data
response = urllib.request.urlopen(url)   # Download Data from URL
data = response.read()
print('Retrieved', len(data), 'characters')

# Parse the XML data
tree = ET.fromstring(data)   # Convert XML data to element tree object for parsing

# Find all <count> tags using XPath
counts = tree.findall('.//count')

# Sum the counts
total = 0
for count in counts:
    total += int(count.text)


print('Count:', len(counts))
print('Sum:', total)

# Testing
# https://py4e-data.dr-chuck.net/comments_1717175.xml

# Answer Will be :
                    # Retrieved 4231 characters
                    # Count: 50
                    # Sum: 2318







'''##################################### ===> JSON Data Represents  ######################################'''

import json

inp = '''[         
    { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },

    { "id" : "009",
    "x" : "7",
    "name" : "Brent"
    }

]'''     # JSON represents data as nested lists and dictionaries

info = json.loads(inp)
print('User Count:', len(info))

for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x'])





'''##################################### ===> Extracting Data From JSON  ######################################'''

import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ') 
if len(url) < 1:
    url = 'https://py4e-data.dr-chuck.net/comments_42.json'   # Default URL for testing
                                                                    # Answer will be:
                                                                        #Retrieved 2711 characters
                                                                        # Count: 50
                                                                        # Sum: 2553
print('Retrieving', url)

uh = urllib.request.urlopen(url) 
data = uh.read().decode() 
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)  # Parsing JSON data
except:
    js = None



counts = list()

for item in js['comments']: 
    counts.append(int(item['count'])) 

print('Count:', len(counts)) 
print('Sum:', sum(counts)) 



# Enter location: https://py4e-data.dr-chuck.net/comments_1717176.json
# Retrieving https://py4e-data.dr-chuck.net/comments_1717176.json
# Retrieved 2741 characters
# Count: 50
# Sum: 2454





'''##################################### ===> Geocoding  ######################################'''



# =======> Find The location Latitude Longitude and Many more Data 

# Account on Geoapify.com : study.injam@gmail.com 
# My Geoapify API Key : e7ce92dfdb12441ea2da31022f2e963e
# My Geoapify API URL : https://api.geoapify.com/v1/geocode/search?text=38%20Upper%20Montagu%20Street%2C%20Westminster%20W1H%201LJ%2C%20United%20Kingdom&apiKey=e7ce92dfdb12441ea2da31022f2e963e


import urllib.request, urllib.parse
import json, ssl     # json for parsing data, ssl for ignoring SSL certificate errors

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Base URL and API Key
serviceurl = 'https://api.geoapify.com/v1/geocode/search'
api_key = 'e7ce92dfdb12441ea2da31022f2e963e'

while True:
    address = input('Enter location: ')
    if len(address) < 1: 
        break

    # Prepare parameters
    parms = {
        'text': address,
        'apiKey': api_key
    }                                                       # https://api.geoapify.com/v1/geocode/search  --> Base URL
    url = serviceurl + '?' + urllib.parse.urlencode(parms)  # ? --> এটি URL এ প্যারামিটার শুরু করার চিহ্ন। ? এর পরে প্যারামিটারগুলি যুক্ত হয়।

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)  # Downloading Data From URL
    data = uh.read().decode() # Reading Downloaded Data
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))  # Hpw many Data Downloaded and shows First 20 characters of the Data

    try:
        js = json.loads(data)  # Parrsing JSOn Data and store it in js variable
    except json.JSONDecodeError: # If JSON Data Incorrect than it will execute
        print("Error: Invalid JSON data")
        js = None

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break


# Extract latitude, longitude, and formatted address

    # print(json.dumps(js, indent=4))
    # print(json.dumps(js['features'][0], indent=4))
    # print(json.dumps(js['features'][0]['properties']['lon'], indent=4))

    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted']
    print(location)



'''
--> text প্যারামিটার:

text=ann+Arbor%2C+MI

text: এটি জিওএপিফাই API এর একটি প্যারামিটার, যেখানে আমরা ঠিকানা বা লোকেশনের নাম দিই।

ann+Arbor%2C+MI: এটি ইউজার দ্বারা ইনপুট দেওয়া ঠিকানা বা লোকেশন। এখানে:

ann+Arbor: ann Arbor (একটি শহরের নাম)। স্পেস ( ) কে + দিয়ে রিপ্লেস করা হয়েছে।

%2C: এটি একটি URL-এনকোডেড কমা (,)। URL এ কমা (,) কে %2C হিসেবে লেখা হয়।

+MI: MI (মিশিগান রাজ্যের সংক্ষিপ্ত নাম)। স্পেস ( ) কে + দিয়ে রিপ্লেস করা হয়েছে।
'''


'''
apiKey প্যারামিটার:

&apiKey=e7ce92dfdb12441ea2da31022f2e963e

&: এটি দিয়ে নতুন প্যারামিটার যুক্ত করা হয়।

apiKey: এটি জিওএপিফাই API এর অথেন্টিকেশন কী। প্রতিটি API রিকোয়েস্টে এই কীটি পাঠানো আবশ্যক।

e7ce92dfdb12441ea2da31022f2e963e: এটি আপনার API কী। এটি ইউনিক এবং আপনার অ্যাকাউন্টের সাথে লিঙ্ক করা।
'''


'''
ইনপুট:
        ann Arbor, MI

URL-এনকোডেড ফরম্যাট:
        ann+Arbor%2C+MI
লিঙ্ক:
        https://api.geoapify.com/v1/geocode/search?text=ann+Arbor%2C+MI&apiKey=e7ce92dfdb12441ea2da31022f2e963e
'''