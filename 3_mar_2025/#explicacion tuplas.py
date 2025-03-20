datos={
    "gender": "female",
    "date_of_birth": "05.08.02",
    "enrollment_semester": "Summer 2022",
    "semester_number": 6,
    "major": "Data Analytics",
    "number": 22100
}

def nuevaclave(dic,clave,valor):
    for key in dic.keys( ):
        if key!=clave:
            dic[key]=valor
            print(f"key={key} clave={clave}")
        else:
            return("la clave ya existe")
        
miclave=input("ingrese una nueva clave: ")
mivalor=input("ingrese el nuevo valor: ")
nuevaclave(datos,miclave,mivalor)
print(datos)
