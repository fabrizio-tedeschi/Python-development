# FUNZIONI

def stampa_menu():
    print()
    print("----------- MENU -----------")
    print("1) Prima operazione")
    print("2) Seconda operazione")
    #Inserire qui il print di ulteriori operazioni possibili
    print("3) Esci")
    print()

# Implementazione funzioni chiamate dal menu


# PROGRAMMA PRINCIPALE

comando = 0
while comando != 3:
    stampa_menu()
    comando = int(input("Inserire un comando: "))

    if comando == 1:
        # Inserire qui le istruzioni da eseguire nel caso di operazione 1
        print()
    elif comando == 2:
        # Inserire qui le istruzioni da eseguire nel caso di operazione 2
        print()
    elif comando == 3:
        print("Sto effettuando l'uscita...")
    else:
        print("Comando non valido")

print("Uscita effettuata correttamente!")