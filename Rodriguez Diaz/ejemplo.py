import errno
try:
    agua= open("c:/csers/aprendiz/documents/practic_git","rt")
    agua.close()
except Exception as x:
    if x.errno == errno.ENOENT:
        print("El archivo no existe.")
    elif x.errno == errno.EMFILE:
        print("Demasiados archivos abiertos.")
    else:
        print("El numero del error es:", x.errno)
