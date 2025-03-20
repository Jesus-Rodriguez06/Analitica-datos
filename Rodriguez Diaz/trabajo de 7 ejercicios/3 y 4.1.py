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
maxi=max(vec) 
mini=min(vec)
print("el menor es:",mini,"el mayor es:",maxi)
print(vec)
