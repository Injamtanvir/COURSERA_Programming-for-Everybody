# InjamTanvir(INJAM UL HAQUE)

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