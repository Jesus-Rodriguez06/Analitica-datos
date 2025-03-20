import random 

def crear(cantidad):
    lista = []  
    for _ in range(cantidad):
        lista.append(random.randint(1, 100))  
    return lista

def calcular_promedio(lista):
    suma = 0
    for num in lista:
        suma += num  
    promedio = suma / len(lista)  
    return promedio

def calcular_varianza_desviacion(lista, promedio):
    suma_diferencias = 0
    for num in lista:
        suma_diferencias += (num - promedio) ** 2  
    varianza = suma_diferencias / len(lista)  
    desviacion = varianza ** 0.5  
    return varianza, desviacion

tam = random.randint(5, 20)
vec = crear(tam)


promedio = calcular_promedio(vec)
varianza, desviacion = calcular_varianza_desviacion(vec, promedio)


print(vec)
print("Varianza:", varianza)
print("Desviación estándar:", desviacion)
