import json
import urllib.request

data = '''{
    "name": "Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
    },
    "email": {
        "hide": "yes"
    }
}'''

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1008615.json (Sum ends with 75)

url = input('Enter: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1008615.json'

json_data = urllib.request.urlopen(url).read()
info = json.loads(json_data)

total = 0
for comment in info['comments']:
    total = total + comment['count']

print(total)
