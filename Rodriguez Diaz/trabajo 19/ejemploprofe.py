import json
import csv
with open('trabajo 19\employees.json','r',encoding='utf-8')as eljson:
    data=json.load(eljson)
    
headers=data[0].keys()
with open('trabajo 19/empleados.csv','w')as elcsv:
    writer=csv.DictWriter(elcsv,headers)
    writer.writeheader()
    writer.writerow(data)