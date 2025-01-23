def stampa_menu():
    print()
    print("--- Monteore sportivo: squadra Ariospalla---")
    print("1) Stampa giocatori")
    print("2) Aggiungi giocatore")
    print("3) Modifica dati giocatore")
    print("4) Rimuovi giocatore")
    print("5) Inserisci partita")
    print("6) Stampa partite")
    print("7) Aggiungi giocatore in partita")
    print("8) Stampa partita per giocatore selezionato")
    print("9) Esci")
    print()


giocatori = []
partite = []


comando = 0
while comando != 9:
    stampa_menu()
    comando = int(input("Inserire un comando: "))

    if comando == 1:
        for g in giocatori:
            print(g)

    elif comando == 2:
        print()
        giocatore = {} 
        giocatore["nome"] = input("Inserire nome: ")
        giocatore["cognome"] = input("Inserire cognome: ")
        giocatore["data_nascita"] = input("Inserire la data di nascita: ")
        giocatore["altezza"] = input("Inserire altezza: ")
        giocatore["classe"] = input("Inserire classe: ")

        giocatori.append(giocatore)
        print()

    elif comando == 3:
        print()
        index = 0 
        for giocatore in giocatori:
            print("Modifica giocatore in posizione:", index)
            x = int(input("Inserisci il giocatore che vuoi modificare:"))
            giocatori[x]["nome"] = input("Modifica nome: ")
            giocatori[x]["cognome"] = input("Modifica cognome: ")
            giocatori[x]["data_nascita"] = input("Modifica data di nascita: ")
            giocatori[x]["altezza"] = input("Modifica altezza: ")
            giocatori[x]["classe"] = input("Modifica classe: ")
            break 

    elif comando == 4:
        print()
        index = 0
        for giocatore in giocatori:
            print("Elimina giocatore in posizione:", index)
            x = int(input("Inserisci il giocatore che vuoi eliminare:"))
            popped = giocatori.pop(x)
            print("DEBUG - rimosso elemento:", popped)

    elif comando == 5:
        print()
        partita = {}
        partita["data"] = input("Inserire data della partita: ")
        partite.append(partita)

    elif comando == 6:
        for p in partite:
            print(p)
        
    elif comando == 7:
        print()
        x = input("inserisci il nome del giocatore che vuoi far partecipare alla partita: ")
        d = int(input("In quale data partecipa? "))
        for partita in partite:
            if partita["data"] == d:
                partita["giocatori"].append(x)

    elif comando == 8:
        print()
        index = 0
        for partita in partite:
            x = input("Inserisci il giocatore per cui desideri stampare le partite: ")
            if partita["giocatori"].count(x) >= 1:
                print(partita)

    elif comando == 9:
        print("Sto effettuando l'uscita...")
    else:
        print("Comando non valido")

print("Uscita effettuata correttamente!")
