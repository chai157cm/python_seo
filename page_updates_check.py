# Check page for updates

import requests

url = 'yoururl'
headers = requests.get(url).headers
last_mod = headers['Last-Modified']
etag = headers['Etag']

print('Etag: {}'.format(etag))
print('Last-Modified: {}'.format(last_mod))
