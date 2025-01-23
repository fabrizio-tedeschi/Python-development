#progetto: concessionario di auto e moto
print('Benvenuto al concessionario Prestige Motors ')
print('''Con Prestige Motors guiderai il tuo sogno ogni giorno ;)''')
print('''un nostro operatore ti aiuterà nella scelta.''')

print('le auto disponibili sono:')
auto = [
    {"marca": "BMW", "modello": "X3"},
    {"marca": "BMW", "modello": "x5"},
    {'marca':'mercedes','modello':'AMG GT'},
    {'marca':'mercedes','modello':'Classe S'},
    {'marca':'porsche','modello':'911 GT3 RS'},
    {'marca':'porsche','modello':'carrera s'}
]

#Stampa auto
for a in auto:
    print(a)

#CHIEDO MARCA E MODELLO
m = input("Inserisci marca da acquistare: ")
mod = input("Inserisci modello da acquistare: ")
trovata = False

for a in auto:
    if a["marca"].lower() == m.lower() and a["modello"].lower() == mod.lower():
        trovata = True

#SE MARCA E MODELLO ESISTONO CHIEDO CONFERMA ACQUISTO
if trovata == True:
    print('il modello scelto è disponibile')
    desiderio = input('''desidera acquistare l'auto?''') 

    if desiderio.lower() == 'si':
        print('''il prezzo dell'auto è 200.000 euro ''')
        print('complimenti, ottima scelta')
        print('''grazie per aver scelto Prestige Motors.
              Arrivederci''')

    elif desiderio.lower() == 'no':
        print('Acquisto annullato')
else:
    print("Non possediamo questo modello di auto")