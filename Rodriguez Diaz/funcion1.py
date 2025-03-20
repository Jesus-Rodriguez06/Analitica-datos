import random
def llenarListaRandom(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista

vec=[]
tam=int(input("Cuantos numeros ingreso a la lista"))
vec=llenarListaRandom(vec,tam)
print(vec)