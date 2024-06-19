#Apertura del file in lettura
file = open("testo.txt", "r")

for line in file:
    #Stampa di ciascuna linea eliminandone il termintore (print inserisce un nuovo \n)
    print(line.replace("\n", ""))