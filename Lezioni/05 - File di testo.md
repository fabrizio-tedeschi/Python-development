# File di testo

I file di testo "contengono" al loro interno un insieme di caratteri in ordine sequenziale.

Ogni linea termina con un carattere speciale `\n` detto terminatore di linea. Diventa quindi possibile distinguere ciascuna
linea tramite tale carattere.

## Creazione e apertura di file

Per creare un file è possibile sfruttare la funzione `open()` come mostrato di seguito.

```python
#Creazione di un nuovo file alla posizione corrente e apertura in scrittura
open("nome", "w")

#Creazione di un nuovo file solo se questo non esiste già
open("nome", "x")
```

La funzione `open(percorso/nomefile, mode)` permette inoltre di aprire un file secondo la modalità specificata come parametro.
Essa restituisce un riferimento al file aperto.

### Modalità di apertura dei file

| Modalità            | Simbolo | Descrizione                                            |
|---------------------|---------|--------------------------------------------------------|
| Lettura             | `r`     | Permette di leggere dati dall'inizio di un file        |
| Scrittura           | `w`     | I dati del file vengono sovrascritti da quelli nuovi   |
| Aggiunta (append)   | `a`     | Permette di scrivere dati partendo dalla fine del file |

```python
#Apertura di un file esistente in lettura
open("documenti/prova.txt", "r")
```

## Lettura e scrittura dati da file

Per operare con i file, Python mette a disposizione i seguenti metodi:

* `.read(nchar)`: legge i `nchar` caratteri dal file e li restituisce come stringa. Se non viene specificato nessun parametro essa restituisce tutti i caratteri del file come stringa.
* `.write(str)`: inserisce la stringa `str` passata come argomento all'interno del file.
* `.readline(maxchar)`: legge una linea del file e la restituisce come stringa. In caso sia specificato `nmax` vengono letti al massimo `nmax` caratteri.
* `.readlines()`: legge tutte le linee del file e le restituisce come elementi di una lista
* `.writelines(list)`: inserisce gli elementi (stringhe) della lista `list` all'interno del file

Viene riposrtato di seguito un esempio di utilizzo delle funzioni di lettura/scrittura:

```python
#Apertura dei file
f1 = open("inputfile.txt", "r")
f2 = open("outputfile.txt", "a")

#Lettura di una linea dal primo file
linea = f1.readline()

#Scrittura della linea sul secondo file
f2.write(linea)

#Chiusura dei file
f1.close()
f2.close()
```

>[!WARNING]
> Per poter utilizzare una funzione di lettura/scrittura su un file è necessario possedere i permessi necessari
> (aver aperto il file in lettura/scrittura), in caso contrario si occorrerà in errori!

### Modifica della posizione del cursore

Durante la lettura/scrittura da file viene utilizzato una sorta di cursore detto I/O pointer (proprio come avviene per 
la scrittura di caratteri con gli editor di testo).

Per modificare la posizione dell'I/O pointer è possibile utilizzare il metodo `.seek(pos)` che sposta l'I/O pointer
a una distanza di `pos` caratteri rispetto all'inizio del file.

```python
#Apertura dei file
f = open("miofile.txt", "r")

#Lettura di alcune linee
f.readline()
f.readline()
f.readline()

#Spostamento del cursore all'inizio del file
f.seek(0)

#Chiusura dei file
f.close()
```

## Operare con le directory del file system

> TODO