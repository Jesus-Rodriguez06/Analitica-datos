def opuesto():
    n=1
    c=0
    s=0
    prm=0
    while n!=0:
        n=int(input("ingrese numero"))
        c+=1 
        s=s+n
    c-1
    prm=(s)/c
        
    return "la suma de los numeros ingresados es:",s,"y el promedio es:",prm

print(opuesto())