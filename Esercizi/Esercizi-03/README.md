# Esercizi 03 - Strutture dati

## Liste

### (A) - iterazione.py

Inizializzare una tupla di 6 frutti. Stampare ogni voce della tupla seguita dal proprio indice di posizione (a partire da 0). Si utilizzi un ciclo `for` per iterare sulla tupla. Viene fornito di seguito un esempio di output.

```
In posizione 0 si trova l'elemento: Mele
In posizione 1 si trova l'elemento: Pere
...
In posizione 5 si trova l'elemento: Ciliege
```

### (B) - aggiungi-nomi.py

Scrivere un programma python che chieda in input all'utente 5 nomi e li inserisca all'interno di una lista.
Dopo l'inserimento di ciascun nome il programma stampa il messaggio "DEBUG - inserito nome in posizione x" dove x è l'indice (progressivo) di posizione di ciascun elemento.
Prima di terminare il programma stampa su `stdout` la lista generata.

### (C) - rimuovi-dispari.py

Sia data la seguente lista python con **stringhe in posizioni pari e interi in posizioni dispari**:

```python
l = ["Mario", 15, "Luigi", 16, "Bianca", 20, "Rosa", 15, "Anna", 20]
```

Scrivere un programma che rimuova dalla lista tutti i numeri interi sostituendoli con una stringa vuota e stampando per ciascuna rimozione il messaggio "DEBUG - rimosso elemento: x" dove x è ciascun valore rimosso.
Prima di terminare il programma stampa la lista "sfoltita" su `stdout` e la sua dimensione/lunghezza.

### (D) - ordinamento.py

Siano date le seguenti liste python `l1` ed `l2`:

```python
l1 = ["Mario","Luigi", "Bianca", "Rosa", "Anna"]
l2 = [5, 7, 15, 0, -12, 75, 18]
```

Scrivere un programma che ordini:

* La lista di stringhe `l1` in ordine alfabetico dalla A alla Z (ordine crescente).
* Il programma ordina la lista `l2` in ordine numerico decrescente.

> Suggerimento: NON sono necessari algoritmi di ordinamento, sono sufficienti i metodi delle liste.

### (E) - indovina-numero.py

Scrivere un programma che inserisca in una lista 20 numeri random compresi fra -50 e 50.
Terminata la creazione della lista  il programma chiede all'utente di iserire un valore numerico intero e controlla se questo valore è presente nella lista.
In caso affermativo il programma stampa un messaggio di successo e l'indice a cui si trova l'elemento nella lista. In caso negativo il programma stampa un messaggio di insuccesso.

## Dictionary