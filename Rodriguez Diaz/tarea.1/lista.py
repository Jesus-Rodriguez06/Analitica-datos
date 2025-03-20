import random
lista= [random.randint(1,100)for i in range(5,20)]
print(lista)
lista2=[1 if x<50 else 2 for x in lista]
print(lista2)

# version de la tabla de frecuencias con todas sus funciones de metodos de listas
# llenado por comprension de la lista 