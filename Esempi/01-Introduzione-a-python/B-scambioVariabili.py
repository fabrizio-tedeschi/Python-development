#Dichiarazione di due variabili x e y
x = 3
y = 5

#Stampa dei valori su output
print("Situazione iniziale:")
print("La variabile x vale", x)
print("La variabile y vale", y)
print()

#Scambio delle variabili attraverso la variabile temporanea

tmp = x
x = y
y = tmp

print("Situazione dopo lo scambio con varibile temporanea:")
print("La variabile x vale", x)
print("La variabile y vale", y)
print()

#Scambio (errato) senza variabile temporanea

x = y
y = x

print("Situazione dopo lo scambio SBAGLIATO:")
print("La variabile x vale", x)
print("La variabile y vale", y)
print("Uno dei due valore è stato perduto per sempre!")
print()