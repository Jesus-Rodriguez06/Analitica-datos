import csv

with open("C:\Users\Aprendiz\Desktop\Rodriguez paez\empleados\employees.csv") as empfile:
    data=csv.reader()
    print(type(data))
    emplist=list(data)
    print(type(emplist))
    print(len(emplist))
    for emp in emplist:
        print(emp)