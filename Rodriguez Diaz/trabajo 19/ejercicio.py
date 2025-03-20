import json
with open('trabajo 19\employees.json','r') as documento:
    contenido= json.load(documento)
    lista=[x for x in contenido]
    #for x in int("SALARY"):
        
    cont=[int(y ["SALARY"]) for y in lista[1:]]
    suma=0
    print(cont)
    for x in cont:
        suma = suma + x
        promedio= suma/len(cont)
    print(promedio)
def departamento():
    lista2=[]
    z=[int(y ["DEPARTMENT_ID"]) for y in lista[1:]]
    lista2.append(z)
    for x in lista2:
        if x == 50:
         return(x)
        else:
            return
    print(lista2)
departamento()
