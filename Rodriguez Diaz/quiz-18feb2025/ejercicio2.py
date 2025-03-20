#2.solicite 2 numeros del usuario
#2.imprima la serie desde el 1 ingresado hasta el 2
#2..al programa anterior añada la opcion de mostrar los multiplos de 7
print("--------------segundo ejercicio----------")
num1= int(input("DIGITE UN PRIMER NUMERO:"))
num2= int(input("DIGITE UN SEGUNDO NUMERO:"))
def serie(num1,num2):
    if num1<num2:
       while num1<num2:
         print(num1+1)
         num1+=1
       else: 
        print("ciclo ascendente finalizado")
    elif num1>num2:
       while num1>num2:
        print(num1+1)
        num1-=1
       else:
        print("ciclo descendente finalizado")

def divisores():
 print("LISTA DE MULTIPLOS DE 7 EN EL RANGO ESTABLECIDO")
 for x in range(num1,num2+1):
  if x%7==0:
    print(x)
        

serie(num1,num2)
divisores()

     