import data, random

def nombres(data):
    ciudades = ["usa","Australia","Uk","Canada"]  
    for key in data.datos:
        key["country"]=random.choice(ciudades)
        print(key)
        
        
nombres(data)