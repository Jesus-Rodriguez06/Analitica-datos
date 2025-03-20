import random

def crear(cantidad):
    lista = [random.randint(5, 20) for _ in range(cantidad)]
    return lista

# Genera un tamaño aleatorio para la lista
tam = random.randint(10, 50)
vec = crear(tam)

# Crear una lista para las frecuencias
frecuencias = [0] * 16  # Ya que los números generados están entre 5 y 20, necesitamos una lista de tamaño 16

# Contar las frecuencias
for num in vec:
    frecuencias[num - 5] += 1  # Restamos 5 para usar el índice adecuado en la lista

# Sumar las frecuencias
suma_frecuencias = sum(frecuencias)

print(f"Frecuencia de cada número entre 5 y 20: {frecuencias}")
print(f"Suma total de las frecuencias: {suma_frecuencias}")
print(f"Lista generada: {vec}")