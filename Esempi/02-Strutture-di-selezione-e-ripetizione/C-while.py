#Inizializzazione di N
N = 0

#Istruzioni da ripetere fino a quando N >= 0
while N >= 0:
    N = int(input("Inserisci un numero: "))
    print("Hai inserito il numero:", N)

    if N < 0:
        print("Numero negativo: uscita...")
    else:
        print("Inserire un numero negativo per terminare il programma")

    print()

print("Programma terminato.")