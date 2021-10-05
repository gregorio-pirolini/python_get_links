import requests
from bs4 import BeautifulSoup

url='http://no1girl.net/'

links= []

website= requests.get(url)
website_text=website.text
soup = BeautifulSoup(website_text)
for link in soup.find_all('a'):
    links.append(link.get('href'))



f = open("demofile2.txt", "a")

for link in links:
    # print (link)
    f.write(link)
    f.write("\n")

f.close()
