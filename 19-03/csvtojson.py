import csv,json

with open("employees.json","r", encoding="utf-8") as datajson:
    datos=json.load(datajson)
    
headers=datos[0].keys()
    
with open("empleados.csv","w") as elcsv:
    writer=csv.DictWriter(elcsv,headers)
    writer.writeheader()
    writer.writerows(datos)