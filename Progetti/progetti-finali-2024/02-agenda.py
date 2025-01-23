#FUNZIONI
def stampa_menu():
    print()
    print("--------- MENU AGENDA ---------")
    print("1) Inserire evento")
    print("2) Rimuovere evento")
    print("3) Mostra tutti gli eventi")
    print("4) Rimuovi tutti gli eventi")
    print("5) Esci")
    print()

#liste/dictionary
eventi = []

# PROGRAMMA PRINCIPALE
comando = 0
while comando != 5:
    stampa_menu()
    comando = int(input("Inserire un comando: "))

    if comando == 1:
        e = {}
        e["titolo"] = input("Inserire il titolo dell'evento:")
        e["mese"] = input("Inserire il mese dell'evento:")
        e["giorno"] = input("Inserire il giorno dell'evento:")
        e["orario"] = input("Inserire l'orario dell'evento:")
        eventi.append(e)
        print()

    elif comando == 2:
        c = 0
        for ev in eventi:
            print(c, ev)
            c += 1
        print()

        eventi.pop(int(input("Inserire la posizione dell'evento da rimuovere:")))
        print()

        d = 0
        for ev in eventi:
            print(d, ev)
            d += 1

        print()
        print("L'evento è stato rimosso dall'agenda.")
        print()

    elif comando == 3:
        f = 0

        for ev in eventi:
            print(f, ev)
            f += 1

        if f == 0:
            print("Nessun evento.")

        print()

    elif comando == 4:
        eventi.clear()
        print("Tutti gli eventi sono stati rimossi.")
        print()

    elif comando == 5:
        print("Sto effettuando l'uscita...")

    else:
        print("Comando non valido.")

print("Uscita effettuata correttamente!")