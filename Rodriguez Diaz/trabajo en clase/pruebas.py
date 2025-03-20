t=  [[3-x for x  in  range (3)]for j in range (3)]
s=0
for x in range(3):
    s+=t[x][x]
print(s)

lista= [1,2,3]
for x in range(len(lista)):
    lista.insert(1,lista[x])
print(lista)