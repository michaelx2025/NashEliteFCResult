import json
from bs4 import BeautifulSoup
import requests
import time

response = requests.get("https://fencingtracker.com/club/100322683/NEFC/results" , headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"} )

html  = BeautifulSoup(response.content,'html.parser')
name = html.find("div", class_="card-body").h3
results = html.find("div", class_="card-body").table.tbody

check = {
 "Name": name.get_text(),
 "Events": {
            results.tr.td.find_next_sibling('td').get_text():[{
                        "Name": results.tr.td.get_text(),
                        "Place": results.tr.find_next('td').find_next('td').find_next('td').get_text(),
                        "Earned-Rating": results.tr.find_next('td').find_next('td').find_next('td').find_next('td').get_text()
                        }],
           },            
 "Pictures":[]
 }

#print(check)
#print(results.get_text())

#while results.find_next('tbody') != None:
    #print(name.get_text())
    #print(results.get_text())
    #name = name.find_next('h3')
    #results = results.find_next('tbody')
Total = []
while results != None:   
    item = {"Name": name.get_text() , "Events" : {} , "Pictures": []}
    person = results.tr
    while(person != None):
        event = person.td.find_next_sibling('td').get_text()
        if event not in item["Events"]:
            item["Events"].update( {event : []})
        
        ind = {
        "Name": person.td.get_text(),
        "Place": person.find_next("td").find_next("td").find_next("td").get_text(),
        "Earned-Rating": results.tr.find_next('td').find_next('td').find_next('td').find_next('td').get_text()
        }
        item["Events"][event].append(ind)
        person = person.find_next_sibling('tr')
    Total.append(item)
    name = name.find_next('h3')
    results = results.find_next('tbody')


print(Total)
