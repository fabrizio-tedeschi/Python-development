#Apertura del file al percorso specificato
f = open("testo.txt", "w")

#Scrittura di alcune linee sul file
f.write("Prima linea\n")
f.write("Seconda linea\n")

#Scrittura di un insieme di stringhe
linea = ["Parole", " ", "della", " ", "terza", " ", "linea.\n"]
f.writelines(linea)

#Scrittura di un insieme di linee (stringhe con terminatore)
linee = ["Quarta linea\n", "Ultima linea del file creato.\n"]
f.writelines(linee)

#Chiusura del file (automatica al termine del programma)
f.close()