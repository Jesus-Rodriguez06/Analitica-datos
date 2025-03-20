import random
def crear(lista,cantidad):
    lista=[]
    for x in range (cantidad):
        x=random.randint(5,20)
        lista.append(x)
    return lista
vec=[]
tam=random.randint(10,50)
vec=crear(vec,tam)
suma=0
for i in vec:
    suma += i
print(suma)
print(vec)
def frecuencia(vec):
    frecuencia1 = []
    for x in vec:
        encontrado = False
        for y in frecuencia1:
            if y[0] == x:
                y[1] += 1
                encontrado = True
                break
        if not encontrado:
            frecuencia1.append([x, 1])
    return frecuencia1
    
resultado = frecuencia(vec)
sumafre= sum(y[1] for y in resultado)
print(resultado)
print(sumafre)

def frecurelativa(vec):
    frecuencia1 = []
    for x in vec:
        encontrado = False
        for y in frecuencia1:
            if y[0] == x:
                y[1] += 1
                encontrado = True
                break
        if not encontrado:
            frecuencia1.append([x, 1])
    
    sumafre= sum(y[1] for y in frecuencia1) 
    frecurela= [[y[0]/ sumafre] for y in frecuencia1]
    return frecurela
resultado= frecurelativa(vec)

print(resultado)