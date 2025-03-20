import data

def nombres(data):
    lista_nom=[]
    for key in data:
        for x in key.keys():
            if x == "name":
                lista_nom.append(key[x])
                print(lista_nom)

nombres(data.datos)
