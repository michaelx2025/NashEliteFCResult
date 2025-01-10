import json
from bs4 import BeautifulSoup
import requests
import time

response = requests.get("https://fencingtracker.com/club/100322683/NEFC/results" , headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"} )

html  = BeautifulSoup(response.content,'html.parser')
name = html.find("div", class_="card-body").h3
results = html.find("div", class_="card-body").table.tbody

#print(name.get_text())

#print(results.get_text())
while results.find_next('tbody') != None:
    print(name.get_text())
    print(results.get_text())
    name = name.find_next('h3')
    results = results.find_next('tbody')


