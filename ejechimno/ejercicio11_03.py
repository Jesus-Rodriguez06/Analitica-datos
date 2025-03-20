def buscarpalabra():   
    with open("himno.txt","r",encoding="utf-8") as busqueda:
        st=busqueda.read().lower()
        cantpa=0
        palabra=input("escribe la palabra que quieres saber si esta en el himno: ")
        frase=st.split()
        print(frase)
        for x in frase:
            if x == palabra:
                cantpa+=1
        if cantpa > 0:
                print("la palabra que ingresaste si esta en el himno y se repite",cantpa,"veces")
        else:
             print("la palabra ingresada no se encuentra en el himno")
buscarpalabra()
