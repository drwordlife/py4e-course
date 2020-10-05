import xml.etree.ElementTree as Et
import urllib.request

def extract_xml():
    data = '''<person>
        <name>Chuck</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>'''

    input_xml = '''<stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>
    </stuff>'''

    tree = Et.fromstring(data)
    print('Name: {}'.format(tree.find('name').text))
    print('Attr: {}'.format(tree.find('email').get('hide')))
    print('Attr: {}'.format(tree.find('phone').get('type')))

    stuff = Et.fromstring(input_xml)
    lst = stuff.findall('users/user')
    for item in lst:
        print('Name: {}'.format(item.find('name').text))
        print('Attr: {}'.format(item.find('id').text))
        print('Attr: {}'.format(item.get('x')))

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1008614.xml (Sum ends with 55)


url = input('Enter: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1008614.xml'

xml_data = urllib.request.urlopen(url).read()
tree = Et.fromstring(xml_data)
counts = tree.findall('.//count')

total = 0
for count in counts:
    total = total + int(count.text)

print(total)



