#Esempio di ciclo do-while
#L'istruzione di input viene eseguita almeno una volta

while True:
    N = int(input("Inserire un numero N (0 per terminare): "))

    if N == 0:
        break

print("Uscita dal programma...")