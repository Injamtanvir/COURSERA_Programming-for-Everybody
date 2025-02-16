# InjamTanvir(INJAM UL HAQUE)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors (https)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Plese enter the URL: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the <span> tags  
tags = soup('span')  # There will be a list of Span tags

count = 0
Total = 0
for tag in tags:
    try: 
        val = int(tag.contents[0]) # OR val = int(tag.text) 
        count += 1
        Total += val

    except ValueError:
        continue 

print("Count", count)
print("Sum", Total)

# https://py4e-data.dr-chuck.net/comments_42.html
# https://py4e-data.dr-chuck.net/comments_1717173.html 