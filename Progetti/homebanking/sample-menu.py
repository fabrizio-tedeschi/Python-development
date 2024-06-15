#Implementazione funzioni del menu

def stampa_menu():
    print()
    print("----------- NEGOZIO -----------")
    print("1) Stampa elenco prodotti")
    print("2) Conta prodotti")
    print("3) Esci")
    print()

def stampa_lista(lista):
    index = 1
    for prodotto in lista:
        print(index, "-", prodotto)
        index += 1

def conta_prodotti(lista):
    prodotto = input("Inserire il nome del prodotto da contare: ")
    return lista.count(prodotto)

#Implementazione menu
prodotti = ["mela", "pera", "banana", "mela"]

comando = 0;
while(comando != 3):
    stampa_menu()
    comando = int(input("Inserire un comando: "))

    if comando == 1:
        stampa_lista(prodotti)
    elif comando == 2:
        res = conta_prodotti(prodotti)
        print("Trovate", res, "occorrenze del prodotto cercato.")
    elif comando == 3:
        print("Sto effettuando l'uscita...")
    else:
        print("Comando non valido")

print("Uscita effettuata correttamente!")