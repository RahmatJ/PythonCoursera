import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1: 
    quit()
data = urllib.request.urlopen(url, context=ctx).read()
parms = dict()
tree = ET.fromstring(data)
hasil = tree.find('comments').findall('comment')
jml = 0
for elem in hasil :
    no = elem.find('count').text
    nomor = int(no)
    jml += nomor
print(jml)