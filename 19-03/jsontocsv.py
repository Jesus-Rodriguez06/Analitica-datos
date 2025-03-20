import csv,json

with open("customers.csv","r",newline=" ",encoding="UTF-8") as elcsv:
    readercsv=csv.DictReader(elcsv)
    
    datacsv=[fila for fila in readercsv]
    
    
