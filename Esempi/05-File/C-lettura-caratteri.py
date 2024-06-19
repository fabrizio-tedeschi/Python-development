#Apertura del file in lettura
file = open("testo.txt", "r")

#Lettura dei primi 5 caratteri
print("I primi 5 caratteri del file sono:", file.read(5))

#Lettura di 10 caratteri per volta
for i in range(3):
    print("-- Blocco " + str(i+1) + ":", file.read(10))

