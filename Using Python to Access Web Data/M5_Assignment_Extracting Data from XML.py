# InjamTanvir(INJAM UL HAQUE)

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


# https://py4e-data.dr-chuck.net/comments_1717175.xml

# Answer Will be :
                    # Retrieved 4231 characters
                    # Count: 50
                    # Sum: 2318
