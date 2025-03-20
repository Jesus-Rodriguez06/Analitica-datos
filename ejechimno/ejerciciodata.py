
with open("data.txt","r",encoding="utf-8") as extraccion:
    st=extraccion.readlines()
    st[0].split(",")[0]
    personas=[st]
    print(st)
    for i in st:
         personas.append(i)
    nombres = [personas ["name"] for personas in st] #ya no funciona 
    print(nombres)


