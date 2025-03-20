def crear():
    lista=[]
    for x in range (1,100+1):
        lista.append(x) 
    maxi=max(lista) 
    mini=min(lista)

    print(lista)
    print("el menor es:",mini,"el mayor es:",maxi)
crear()
