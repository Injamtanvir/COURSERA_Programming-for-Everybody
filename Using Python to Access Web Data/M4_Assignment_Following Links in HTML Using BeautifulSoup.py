# InjamTanvir(INJAM UL HAQUE)

import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors (https)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get input from the user
url = input("Please enter the URL of the Website: ")
position = int(input("Enter the link position: "))  # Position (1-based index)
repeat = int(input("Enter how many times to repeat: "))  # Number of repetitions

print("Retrieving:", url)  # Print initial URL

for i in range(repeat):
    # Fetch and parse the HTML
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all anchor tags and store their links
    links = []
    for tag in soup('a'):
        link = tag.get('href', None)
        links.append(link)

    # Ensure the position is valid
    if len(links) < position:
        print("Not enough links on the page!")
        break

    # Move to the next URL in the chain
    url = links[position - 1]  # Adjusting for 0-based index
    print("Retrieving:", url)  # Print each visited URL

# Extract and print the final name from the last URL
name = url.split('_')[-1]  # Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
last_name = name.split('.')[0]
print("The answer to the last name of the link is:", last_name)



# https://py4e-data.dr-chuck.net/known_by_Fikret.html  3   4    # Answer Anayah
# https://py4e-data.dr-chuck.net/known_by_Jersey.html   18 7   # Answer Alber