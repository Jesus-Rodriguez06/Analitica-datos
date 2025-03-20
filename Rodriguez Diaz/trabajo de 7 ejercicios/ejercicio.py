
lista = []
suma= 0  
for x in range (1,100+1):
        lista.append(x)
for x in lista:
    suma += x
cantD= len(lista)
maxi=max(lista) 
promedio=suma / len(lista)
menor=min(lista)
mediana= x/2
varianza=sum((x-promedio)**2 for x in range (x))/cantD
desviacion=varianza *0.5
print("el mayor es:",maxi)
print("el menor es:",menor)
print("la mediana es:",mediana)
print("la varianza es:",varianza)
print("la desviacion es:",desviacion)
print("el promedio es de:",promedio)
print(lista)
print("la suma de los numeros es:",suma)


