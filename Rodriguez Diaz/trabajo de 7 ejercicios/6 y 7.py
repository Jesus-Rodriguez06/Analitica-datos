def crear():
    lista=[]
    suma=0
    for x in range (1,100+1):
        lista.append(x)
    for x in lista:
     suma += x
    cantD= len(lista)
    promedio=suma / len(lista)
    varianza=sum((x-promedio)**2 for x in range (x))/cantD
    desviacion=varianza *0.5
    print(lista)
    print("la varianza es:",varianza,",la desviacion standar es:",desviacion)
crear()
