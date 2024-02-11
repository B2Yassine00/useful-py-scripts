import csv
import re
import requests


from bs4 import BeautifulSoup
from sys import argv

tosearch = argv[1]

f= open('csv/sneakers.csv','w')
writer = csv.writer(f)

url2 = 'https://www.nike.com/fr/w?q='+tosearch+'&vst='+tosearch

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}


response2 = requests.get(url2, headers=headers)

soup=BeautifulSoup(response2.content, "html.parser")

classes=["product-card__info disable-animations for--product","product-card__messaging accent--color","product-card__title","product-card__subtitle","product-card__product-count","product-price fr__styling is--current-price css-11s12ax"]


sneakers_list = soup.select('div[class="product-card__info disable-animations for--product"]')
for items in sneakers_list:
    rows = []
    rows.append(items.findChildren(recursive=False)[0].findChildren(recursive=False)[0].text)
    prst = items.findChildren(recursive=False)[0].findChildren(recursive=False)[1]
    
    for i in prst:
        rows.append(i.text.replace('\xa0',' '))
    rows.append(items.findChildren(recursive=False)[1].text.replace('\xa0',' '))
    rows.append(items.findChildren(recursive=False)[2].text.replace('\xa0',' '))
    writer.writerow(rows)
    print(rows)


