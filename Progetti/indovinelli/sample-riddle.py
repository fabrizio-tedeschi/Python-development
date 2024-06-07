#Variabili per salvare punteggio e oggetti usati
oggetti_usati = 0
punti = 0

#Inizializzazione lista di oggetti
zaino = ["Bastone", "Biro", "Quaderno"]

#Intro del videogame
print()
print("BENVENUTO AL GIOCO INDOVINELLI")
input("Premi INVIO per iniziare...")

#Primo indovinello
print()
print("Sei uscito dalla classe durante una noiosa ora di matematica e srai girando per la scuola.")
print("Vuoi prendere qualcosa alle macchinette...")
print()
print("-- Sfida 1 -- Lista oggetti:", zaino)
print("La il distributore delle merendine si e' inceppata ed la confezione di taralli e' rimasta in bilico.")
print()
print("1) Acquisti una confezione di taralli per ottenerle entrambe")
print("2) Tenti di colpire il distributore con il bastone")
print("3) Rinunci e torni in classe")
azione = int(input("Inserire una azione: "))
print()

if azione == 1:
    print("Riesci ad ottenere due confezioni di taralli al prezzo di una!")
    punti += 1;

elif azione == 2:
    zaino.remove("Bastone")
    oggetti_usati += 1
    print("Il distribuore si rompe, la bidella e' furiosa e ti rispedisce in classe sequestrando il bastone.")
    punti -= 5
else:
    punti -= 1

#Secondo indovinello
print()
print("Sei in classe, la tua compagna di banco ti chiede se puoi svolgere i suoi compiti di informatica per la prossima ora.")
print("-- Sfida 2 -- Lista oggetti:", zaino)
print()
print("La domanda a scelta multipla recita il seguente testo: per calcolare la dimensione di una lista python...")
print("1) Si utilizza la funzione len(lista)")
print("2) Si utilizza il metodo .length")
print("3) Non lo sai e dici alla tua compagna di banco di arrangiarsi")
azione = int(input("Inserire una azione: "))
print()

if azione == 1:
    punti += 20
    print("La tua compagna di banco ti e' molto grata e ti presta la sua calcolatrice in segno di gratitudine.")
    zaino.append("Calcolatrice")
elif azione == 2:
    punti -= 10
    print("La tua compagan di banco e' molto dubbiosa sulla risposta ma ti presta la sua calcolatrice.")
    zaino.append("Calcolatrice")
else:
    punti -= 4

#Terzo indovinello
print()
print("Stai facendo troppa confuzione in classe: Lla prof. di matematica decide di interrogarti.")
print("-- Sfida 3 -- Lista oggetti:", zaino)
print()
n1 = int(input("Inserisci un numero intero: "))
n2 = int(input("Inserisci un numero intero <= 8: "))
print("Calcola la potenza di base", n1, "ed esponente", n2)
print()
print("1) Inserisci il risultato")
print("2) Utilizza la calcolatrice")
print("3) Rinuncia e vai a casa")
azione = int(input("Inserire una azione: "))
print()

if azione == 1:
    risultato = int(input("Inserire il risultato e premere INVIO: "))
    if risultato == n1**n2:
        punti += 10
    else:
        punti -= 4
elif azione == 2:
    if zaino.count("Calcolatrice") > 0:
        oggetti_usati += 1
        zaino.remove("Calcolatrice")
        print("Utilizzando la calcolatrice ottieni", n1**n2, "e superi l'interrogazione.")
        punti += 6
    else:
        print("Non hai la calcolatrice nello zaino, non fare il furbetto...")
        punti -= -5
else:
    punti -= 6

#Stampa statistiche finali
print()
print()
print("GIOCO TERMINATO")
print("\t - Punti accumulati:", punti)
print("\t - Oggetti usati:", oggetti_usati)
print("\t - Oggetti rimasti nello zaino:", len(zaino))