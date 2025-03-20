print("escribir nombre de los estudiantes y su nota")
estudiante1= input("nombre:")
nota1= int(input("nota:"))
def com_not(nota1):
 if(nota1>=9 and nota1==10):
                     return    "su nota es: ",nota1," excelente"
 else:
    if(nota1<=8 and nota1>=7):
                    return"su nota es:",nota1," buena"
    else:
        if(nota1<=6 and nota1>=5):
                    return"su nota es:",nota1, " aceptable"
        else:
            if(nota1<=4 and nota1>=3):
                    return"su nota es:",nota1," insuficiente"
            else:
                if(nota1<=2 and nota1>=1):
                    return"su nota ess:",nota1,"muy baja"
                else:
                        if(nota1==0 or nota1>10):
                          return ("nota no valida")
 
print(com_not((nota1)))