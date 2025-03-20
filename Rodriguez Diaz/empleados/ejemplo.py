#1- Salario mas alto y mas bajo
#2- Agrupar por departamento
#3- Agrupar por manager
#4- Ordenar por apellido
#5- Ordenar por código
import csv
with open ("empleados/employees.csv","r") as emple:
    data=csv.reader(emple)
    for x in data:
        parametro=(x[7])        
        print(parametro)
    for x in parametro:
        if x 

