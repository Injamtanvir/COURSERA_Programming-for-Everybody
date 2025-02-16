# InjamTanvir(INJAM UL HAQUE)


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