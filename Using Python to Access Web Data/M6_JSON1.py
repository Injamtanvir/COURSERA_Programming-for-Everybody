import json

data ='''{
    "name": "Tanvir",
    "phone":{ 
        "type": "intl", 
        "number": "+1 23456789"
    },
    "email": {
        "hide": "yes"
    }   
}'''

info = json.loads(data)
print('Name:', info["name"])
print('hide:', info["email"]["hide"])