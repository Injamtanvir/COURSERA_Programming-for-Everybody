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


