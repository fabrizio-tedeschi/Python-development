# FUNZIONI

def stampa_menu():
    print()
    print("----------- MENU -----------")
    print("1) Aggiungi un giocatore ")
    print("2) ppg di un giocatore ")
    #Inserire qui il print di ulteriori operazioni possibili
    print("3) Rimuovi giocatore ")
    print("4) Esci ")

# Implementazione funzioni chiamate dal menu
giocatori = {
    "LeBron James": 24,
    "Stephen Curry ": 22,
    "Giannis Antetokounmpo ": 32,
}


# PROGRAMMA PRINCIPALE

comando = 0
while comando != 4:
    stampa_menu()
    comando = int(input("Inserire un comando: "))

    if comando == 1:
        giocatori[input("inserire nome giocatore: ")] = 20

        for g in giocatori.keys():
            print(g + ":", giocatori[g])

    elif comando == 2:
        y = input("Inserire nome giocatore per ottenere ppg: ")

        for nome in giocatori.keys():
            if y == nome:
                print("ppg =", giocatori[nome])

    elif comando == 3:
        y = input("Inserire nome giocatore da rimuovere: ")

        trovato = False
        for nome in giocatori.keys():
            if y == nome:
                trovato = True
                break

        if trovato == True:
            giocatori.pop(y)
            print("Rimosso giocatore", y)

        else:
            a = giocatori.get("Giannis Antetokounmpo")
            print(a)

    elif comando == 4:
        print("Uscita in corso ...")

    else:
        print("Comando non valido")

print("Uscita effettuata correttamente!")