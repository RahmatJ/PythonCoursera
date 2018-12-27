import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
data = urllib.request.urlopen(url).read()
info = json.loads(data)
jml = 0
for element in info['comments']:
  counts = int(element['count'])
  jml += counts
print(jml)
