import data, random

def Ciudades(data):
    ciudad = ["usa","Australia","Uk","Canada"]  
    for key in data.datos:
        key["country"]=random.choice(ciudad)
        for x in key.values():
            if x == "country":
                print(f"La ciudad de {key['name']} es {key[x]}")
            elif x == "usa":
                eeuu=[]
                eeuu.append(key[x])
                print(f"Las ciudades de {key['name']} estan en Estados Unidos: {eeuu}")
            
Ciudades(data)