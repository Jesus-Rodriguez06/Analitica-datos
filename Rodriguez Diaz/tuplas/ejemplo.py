
def conjuntos():
    conjunto1=set([1,2,3,4,5,4,4])
    conjunto2=set([1,2,3,4,5,6,7,8,9,10])
    
    print(conjunto2,conjunto1)
    conjunto1.add((6))
    conjunto2.remove(8)
    print(conjunto1)
conjuntos()
