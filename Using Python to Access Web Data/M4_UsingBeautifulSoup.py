# InjamTanvir(INJAM UL HAQUE)

# Beautiful Soup is a Python library for pulling data out of HTML and XML files.
#Website link --> https://pypi.org/project/beautifulsoup4/ 
# In terminal paste this code and run it: pip install beautifulsoup4 or i have a folder name "BeautifulSoup4" in that folder.

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