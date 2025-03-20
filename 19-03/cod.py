# hacer un codigo que prmedie cada uno de los items de slario
import json

with open("employees.json","r") as archivo:
    datos=json.load(archivo)
    lista=[x for x in datos]
    sal=[int(i["SALARY"]) for i in lista[1:]] 
    
    total=0
    
    for c in sal:
        total=total+c
        prom=total/len(lista)
    print(prom)
    
    