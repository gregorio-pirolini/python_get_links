import requests
import re 
from bs4 import BeautifulSoup

url='http://no1girl.net/js/script7.js'

links= []

website= requests.get(url)
website_text=website.text


regex=/(http)+.*(",|',)/g


x = re.findall(regex, website_text)


f = open("demofile4.txt", "a")

for link in x:
    # print (link)
    
    f.write(link)
    f.write("\n")

f.close()
