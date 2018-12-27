from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
jml = 0;
for tag in tags:
	tag_decode = tag.decode()
	hasil = re.findall('[0-9]+', tag_decode)
	for num in hasil:
		jml += int(num)
print(jml)