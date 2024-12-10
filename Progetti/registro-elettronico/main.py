studenti_voti = {
    "Mario Rossi": [9, 8, 7],
    "Luigi Verdi": [5, 6],
    "Anna Bianchi": [],
}


# Funzione usata per calcolare la media di una lista di voti
def media(lista_voti):
    #Se lo studente non ha voti allora ha media 0
    if len(lista_voti) == 0:
        return 0

    #Calcolo dells media
    somma = 0
    for voto in lista_voti:
        somma = somma + voto

    media = somma / len(lista_voti)
    return media


#Funzione che data una lista di nomi di studenti li stampa uno per volta
def stampa_studenti(lista_studenti):
    print()
    print("---------ELENCO STUDENTI---------")
    count = 0
    for studente in lista_studenti:
        count = count + 1
        print(count, studente)
    print()


#Funzione che dato un dictionary di studenti e voti stampa la media per ogni studente
def stampa_medie(dati):
    print()
    print("---------MEDIE--------")
    for studente in dati.keys():
        # estraggo i voti dello studente
        voti = dati[studente]

        # Calcolo la media dei voti
        media_voti = media(voti)

        # Stampo il risultato
        print(studente, "--->", media_voti)
    print()


# Menu
while True:
    #Stampa delle possibili opzioni che l'utente puo' inserire
    print("1. Stampa lista studenti")
    print("2. Stampo media studente")
    print("3. Exit")

    #Attesa di un comando da parte dell'utente
    command = int(input("Inserire comando: "))

    # Stampa studenti
    if command == 1:
        stampa_studenti(studenti_voti.keys())

    # Stampare le medie
    if command == 2:
        stampa_medie(studenti_voti)

    # Uscita
    if command == 3:
        print()
        print("Sto uscendo dal programma...")
        print()
        break