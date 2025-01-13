import json
from bs4 import BeautifulSoup
import requests
import time
import datetime

response = requests.get("https://fencingtracker.com/club/100322683/NEFC/results" , headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"} )

html  = BeautifulSoup(response.content,'html.parser')
name = html.find("div", class_="card-body").h3
results = html.find("div", class_="card-body").table.tbody

Total = {}
while results != None:   
    item = { "Events" : {} , "Pictures": [], "Date": ""}
    person = results.tr
    year = results.tr.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').get_text()[0:4]
    month = results.tr.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').get_text()[5:7]
    day = results.tr.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').get_text()[8:10]
    item["Date"] = {
        "Year": year,
        "Month": month,
        "Day":day
    }
    while(person != None):
        event = person.td.find_next_sibling('td').get_text()
        if event not in item["Events"]:
            item["Events"].update( {event : []})
        
        ind = {
        "Name": person.td.get_text(),
        "Place": person.find_next("td").find_next("td").find_next("td").get_text(),
        "Earned-Rating": person.find_next('td').find_next('td').find_next('td').find_next('td').get_text()
        }
        item["Events"][event].append(ind)
        person = person.find_next_sibling('tr')
    Total.update({name.get_text(): item})
    name = name.find_next('h3')
    results = results.find_next('tbody')


with open("mydata.json", "w") as final:
    json.dump(Total,final, indent=4)
