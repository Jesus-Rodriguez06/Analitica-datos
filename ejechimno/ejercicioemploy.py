import csv 
def identificar_salario():
    with open("employees.csv","r", encoding="utf-8") as emp:
        sal=csv.reader(emp)
        salarios=[sal[7]]
        for x in salarios:
            if x > mayor:
                mayor=x
            print("el salario mayor es:", mayor)
identificar_salario()       
        