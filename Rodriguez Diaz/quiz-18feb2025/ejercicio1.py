#1.solicite la edad al usuario
#1.muestre todos los años que a cumplido desde el año 1
print("------------PRIMER EJERCICIO------------")
edad= int(input("DIGITE SU EDAD:"))

def años(edad):
 for i in range (1,edad+1):
     print("los años que a cumplido son",i,"años")

(años(edad))


print("--------------segundo ejercicio----------")
num1= int(input("DIGITE UN PRIMER NUMERO"))
num2= int(input("DIGITE UN SEGUNDO NUMERO"))
def serie():
 for x in range(num1,num2):
     if num1>num2:
         print(num2,x,num1)
     else: num1<num2
     print(num1,x,num2)
serie()
     

    