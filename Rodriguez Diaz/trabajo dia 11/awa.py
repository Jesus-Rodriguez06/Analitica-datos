
# Leer el archivo de texto
with open('data.txt', 'r') as archivo:
    data = archivo.readlines()

# Extraer el valor de la clave "name"
name_value = data.txt.get("name")

# Imprimir la clave y su valor
print(f'Clave: "name", Valor: "{name_value}"')
