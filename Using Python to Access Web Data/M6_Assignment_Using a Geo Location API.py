# InjamTanvir(INJAM UL HAQUE)

# Account on Geoapify.com : study.injam@gmail.com 
# My Geoapify API Key : e7ce92dfdb12441ea2da31022f2e963e
# My Geoapify API URL : https://api.geoapify.com/v1/geocode/search?text=38%20Upper%20Montagu%20Street%2C%20Westminster%20W1H%201LJ%2C%20United%20Kingdom&apiKey=e7ce92dfdb12441ea2da31022f2e963e


import urllib.request, urllib.parse
import json, ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



# Base URL and API Key MINE Geoapify API Key
'''serviceurl = 'https://api.geoapify.com/v1/geocode/search'
api_key = 'e7ce92dfdb12441ea2da31022f2e963e'

while True:
    address = input('Enter location: ')
    if len(address) < 1: 
        break

    # Prepare parameters
    parms = {
        'text': address,
        'apiKey': api_key
    }
    url = serviceurl + '?' + urllib.parse.urlencode(parms)'''


# Using Coursera(Charles Severance's API)
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: 
        break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)
    # ===================Charles Severance's API==========================


    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except json.JSONDecodeError:
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
    
    # print(json.dumps(js['features'][0], indent=4))

    plus_code = js['features'][0]['properties']['plus_code']
  
    print("Plus Code: ", plus_code)



# South Federal University --> 6FV8QPRJ+VQ
# University of Toronto --> 87M2MJ72+9V