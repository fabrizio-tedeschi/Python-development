# # Progetto guidato - *registro elettronico*

## Obiettivo
Si vuole sviluppare una app da terminale che consenta di gestire un elenco di studenti con relativi voti e media aritmetica.
Il programma deve soddisfare le seguenti funzionalità:

* Stampare l'elenco degli studenti
* Stampare l'elenco degli studenti e la loro rispettiva media

## Progettazione e sviluppo

Prima di iniziare a scrivere codice è sempre bene progettare il software in modo da non dover sprecare il tempo riscrivendo
lo stesso codice più volte:

### 1) Scelta di rappresentazione dei dati

Per sviluppare l'app si ha la necessità di associare il nome di ciascuno studente all'elenco dei suoi voti. Ciò può essere
implementato da una struttura dati di tipo `dictionary` avente come chiavi i nomi degli studenti e come valori la lista dei loro voti:

```python
studenti_voti = {
    "Mario Rossi": [9, 8, 7],
    "Luigi Verdi": [5, 6],
    "Anna Bianchi": [],
}
```

### 2) Creazione di un menu per gestire le operazioni

Per gestire le varie operazioni che l'utente può svolgere è possibile implementare un menu che mostra le diverse scelte
che l'utente può compiere durante l'utilizzo del programma. Inoltre, visto che il programma NON deve arrestarsi finché
non riceve uno specifico comando di uscita, si pone il codice all'interno di un ciclo `while True`.

```python
# Menu principale
while True:
    #Stampa delle possibili opzioni che l'utente puo' inserire
    print("1. Stampa lista studenti")
    print("2. Stampa media studenti")
    print("3. Exit")

    #Attesa di un comando da parte dell'utente
    command = int(input("Inserire comando: "))

    # Stampa studenti
    if command == 1:
        #Qui sarà inserito il codice che stampa la lista degli studenti

    # Stampare le medie
    if command == 2:
        #Qui sarà inserito il codice che stampa la media degli studenti

    # Uscita
    if command == 3:
        print()
        print("Sto uscendo dal programma...")
        print()
        
        #Interruzione forzata del ciclo while
        break
```

### 3) Implementazione delle funzioni specifiche

Al fine di mantenere il codice ordinato, si creano delle funzioni per svolgere le varie specifiche del programma.
Per esempio, è possibile creare una funzione `stampa_studenti(lista_studenti)` che data una `lista_studenti` procede
a scorrerla e a effettuare la stampa.

```python
def stampa_studenti(lista_studenti):
    print()
    print("---------ELENCO STUDENTI---------")
    count = 0
    
    #Scorro la lista degli studenti e li stampo uno per volta
    for studente in lista_studenti:
        count = count + 1
        #Stampo il valore del contatore seguito dal nome dello studente
        print(count, studente)
    print()
```

Per eseguire la stampa degli studenti sarà sufficiente chiamare la funzione sopra implementata all'interno del menu creato
al passo precedente>

```python
    # Stampa studenti
    if command == 1:
        
        #Estraggo dal dictionary una lista con solamente i nomi degli studenti
        elenco = studenti_voti.keys()
        
        #Chiamo la funzione passando come elenco studenti la lista estratta
        stampa_studenti(elenco)
```

Si può procedere analogamente nello sviluppo della seconda specifica (stampa media studenti) come mostrato nel codice
completo del file `main.py` presente in questa cartella.