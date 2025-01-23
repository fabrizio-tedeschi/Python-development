# FUNZIONI
def stampa_menu():
    print()
    print("----------- MENU -----------")
    print("1) Ricerca prodotto")
    print("2) Aggiungi prodotto al catalogo")
    print("3) Prodotti in saldo")
    print("4) Verifica il numero di articoli per marca")
    print("5) Esci")
    print()


# Definizione liste
l = ["Chanel", "Dior", "Gucci", "Armani", "Carolina Herrera", "Tom Ford", "Mugler", "Valentino", "Yves Saint Laurent", "Givenchy"]
q = [29, 33, 57, 29, 34, 42, 25, 27, 39, 40]
c = []

# PROGRAMMA PRINCIPALE
comando = 0
while comando != 5:
    stampa_menu()
    comando = int(input("Inserire un comando: "))

    if comando == 1:
        n = input("inserisci la marca che stai cercando: ")
        
        if l.count(n) >= 1:
            print()
            print("prodotto disponibile nei nostri store")
            print()
            x = input("vuoi aggiungere il prodotto al carrello?: ")
            if x == "si": 
                c.append(n)
                print("prodotto aggiunto al carrello ")
                print("ecco il tuo carrello: ", c)
                index = l.index(n)
                q[index] -= 1
        else: 
            print()
            print("siamo spiacenti questo prodotto non è venduto nei nostri store")

    elif comando == 2:
        e = input("inserisci nuova marca: ")
        l.append(e)
        print()
        print("prodotto aggiunto al catalogo")
        print("ecco il catalogo aggiornato:", l)
        qt = int(input("quanti prodotti vuoi aggiungere?:"))
        q.append(qt)

    elif comando == 3: 
        print(l[0])
        print(l[4])
        print(l[6])
        print()
        m = input("inserisci la marca che vuoi aggiungere al carrello: ")

        if l.count(m) >= 1:
            c.append(m)
            print("ecco il tuo carrello:", c)
            print()
            index = l.index(m)
            q[index] -= 1
        else:
            print("Prodotto inesistente")

    elif comando == 4: 
        y = input("inserisci la marca:")

        if l.count(y) >= 1:
            index = l.index(y)
            print(q[index])

        else:
            print("Prodotto inesistente")

        print()

    elif comando == 5:
        print("Sto effettuando l'uscita...")
        print()
    
    else:
        print("Comando non valido")
        print()


print("Uscita effettuata correttamente!") 



    