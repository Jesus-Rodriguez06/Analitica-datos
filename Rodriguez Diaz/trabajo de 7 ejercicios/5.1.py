import random
def crear(lista,cantidad):
    lista=[]
    for x in range (cantidad):
        x=random.randint(5,20)
        lista.append(x)
    return lista
vec=[]
tam=int(input("Cuantos numeros ingreso a la lista"))
vec=crear(vec,tam)
for i in vec:
     mediana= i/2
print("la mediana es:",mediana)
print(vec)