# InjamTanvir(INJAM UL HAQUE)

# Beautiful Soup is a Python library for pulling data out of HTML and XML files.
#Website link --> https://pypi.org/project/beautifulsoup4/ 
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter the URL: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags  # a is the tag for anchor
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))  # None is the default value 

# http://www.dr-chuck.com/page1.htm
'''


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

# http://www.dr-chuck.com/page1.htm