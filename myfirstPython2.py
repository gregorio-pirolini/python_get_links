import requests
import re 
from bs4 import BeautifulSoup

url='http://no1girl.net/js/script7.js'

website= requests.get(url)
website_text=website.text


reg = "(http.*?)['|\"]"

txt = website_text

x = re.findall(reg, txt)

# print(x)

for linx in x:
    print(linx)

print(len(x))