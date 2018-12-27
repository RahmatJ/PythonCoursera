import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
max_iter = int(input('Max_iter - '))
locate = int(input('location - '))
iterate = 0
while True:
	if(iterate > max_iter):
		break
	html = urllib.request.urlopen(url, context=ctx).read()
	print('Retrieving:',url)
	soup = BeautifulSoup(html, 'html.parser')
	# Retrieve all of the anchor tags
	tags = soup('a')
	location = 1
	for tag in tags:
		if location == locate:
			tag_decode = tag.decode()
			url_tag = re.findall('href="(.+)"', tag_decode)
			url = url_tag[0]
			break
		location +=1
	iterate += 1
    