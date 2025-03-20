def crear():
    diccionario1= {
    "gender": "female",
    "date_of_birth": "05.08.02",
    "enrollment_semester": "Summer 2022",
    "semester_number": 6,
    "major": "Data Analytics",
    "number": 22100
 }
    return (diccionario1)

crear()
def agregar(dict, claven,valorn):
    flag=False
    for key in dict.keys():
        if key == claven:
            print ("la llave ya existe")
        else:
            flag=True
            return



claven1=int(input("digite la nueva clave:"))
valorn1=input("digite el nuevo valor:")
agregar(crear(), claven1, valorn1)
