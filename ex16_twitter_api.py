import json
from urllib.request import urlopen
from twurl import augment

import ssl

tw_timeline_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
tw_friends_url = 'https://api.twitter.com/1.1/friends/list.json'


# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter account: ')
    if len(acct) < 1:
        break

    url = augment(tw_friends_url, {'screen_name': 'acct', 'count': '20'})
    connection = urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining: {}'.format(headers['x-rate-limit-remaining']))

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    # for u in js['users']:
    #     print(u['screen_name'])
    #     s = u['status']['text']
    #     print('  {}'.format(s[:50]))

