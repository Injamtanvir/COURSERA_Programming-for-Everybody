import xml.etree.ElementTree as ET

data = '''<person>
        <name>Tanvir</name>
        <phone type= "intl">
            +2 34567
        </phone>
        <email hide="yes"/>
    </person>
'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))