#Importazione della libreria random
import random

#Stampa di un intero casuale
rnd = random.randint(0, 50)
print("Stampo un numero casuale:", rnd)

#Scelta casuale di un carattere in una stringa
st = "HelloWorld"
randomchar = random.choice(st)
print("Scelta di un carattere casuale:", randomchar)