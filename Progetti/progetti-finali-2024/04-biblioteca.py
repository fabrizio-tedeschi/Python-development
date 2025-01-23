#Di Maria Beatrice Lupi, Sara Gozzi, Andrea Giuliani


libri = [
	{"nome": "I Malavoglia", "autore" : "Giovanni Verga", "disponibilità" : "Disponibile"}, 
	{"nome" : "I Promessi Sposi", "autore" : "Alessandro Manzoni", "disponibilità" : "Disponibile"}, 
	{"nome" : "Aminta", "autore" : "Torquato Tasso", "disponibilità" : "Disponibile"},
	{"nome" : "La Divina Commedia", "autore" : "Dante Alighieri", "disponibilità" : "Disponibile"},
	{"nome" : "Frankenstein", "autore" : "Mary Shelley", "disponibilità" : "Disponibile"},
	{"nome" : "Bucoliche", "autore" : "Publio Virgilio Marone", "disponibilità" : "Disponibile"},
	{"nome" : "De Brevitate Vitae", "autore" : "Lucio Anneo Seneca", "disponibilità" : "Disponibile"},
	{"nome" : "I Fiori del Male", "autore" : "Charles Baudelaire", "disponibilità" : "Disponibile"},
	{"nome" : "Il Rosso e il Nero", "autore" : "Stendhal", "disponibilità" : "Disponibile"},
	{"nome" : "Dr Jekyll & Mr Hyde", "autore" : "Louis Stevenson", "disponibilità" : "Disponibile"},
	{"nome" : "Il Ritratto di Dorian Gray", "autore" : "Oscar Wilde", "disponibilità" : "Disponibile"},
	{"nome" : "L'Odissea", "autore" : "Omero", "disponibilità" : "Disponibile"},
	{"nome" : "La Coscienza di Zeno", "autore" : "Italo Svevo", "disponibilità" : "Disponibile"},
	{"nome" : "Laelius De Amicitia", "autore" : "Marco Tullio Cicerone", "disponibilità" : "Disponibile"},
	{"nome" : "Lo Zibaldone", "autore" : "Giacomo Leopardi", "disponibilità" : "Disponibile"},
	{"nome" : "Madame Bovary", "autore" : "Gustave Flaubert", "disponibilità" : "Disponibile"},
	{"nome" : "Il fu Mattia Pascal", "autore" : "Luigi Pirandello", "disponibilità" : "Disponibile"},
	{"nome" : "L'Ammazzatoio", "autore" : "Emile Zola", "disponibilità" : "Disponibile"},
	{"nome" : "I Miserabili", "autore" : "Victor Hugo", "disponibilità" : "Disponibile"},
	{"nome" : "Il Candido", "autore" : "Voltaire", "disponibilità" : "Disponibile"},
	{"nome" : "L'Orlando Furioso", "autore" : "Ludovico Ariosto", "disponibilità" : "Disponibile"},
	{"nome" : "La Mandragola", "autore" : "Niccolò Machiavelli", "disponibilità" : "Disponibile"}
]

def aggiungi_elemento(libri):
	libro = {}
	libro["nome"] = input("Inserisci titolo:")
	libro["autore"] = input("Inserisci autore:")
	libro["disponibilità"] = "Disponibile"
	libri.append(libro)

def presta_libro(libri):
	titolo_inserito = input("Scrivi il titolo del libro che vuoi:")
	presente = False
	for libro in libri:
		if titolo_inserito == libro["nome"]:
			if libro["disponibilità"] == "Disponibile":
				presente = True
				libro["disponibilità"] = "In prestito"
				print(titolo_inserito, " in prestito per trenta giorni. Mi raccomando, abbine cura! :)")
			else: 
				print("Libro già in prestito, riprova tra qualche giorno!")
		
	if presente == False: 
		print("Non possediamo ancora", titolo_inserito, "ci dispiace!")


def restituisci_libro(libri):
	titolo_restituito = input("Scrivi il titolo del libro che vuoi restituire:")
	da_restituire = False
	for libro in libri:
		if titolo_restituito == libro["nome"]:
			da_restituire = True
			if libro["disponibilità"] == "In prestito":
				libro["disponibilità"] = "Disponibile"
				print(titolo_restituito, "Resitituito con successo!")
			else: 
				print("Il libro non risulta in prestito... ")
	
	if da_restituire == False: 
		print("Non abbiamo ancora", titolo_restituito, "se ce lo vuoi regalare, il comando è AGGIUNGI")	

def mostra_stato(libri):
	titolo_indagato = input("Scrivi il titolo del libro di cui vuoi conoscere la condizione: ")
	presenza = False
	for libro in libri:
		if titolo_indagato == libro["nome"]:
			if libro["disponibilità"] == "Disponibile":
				presenza = True
				print(titolo_indagato, "è disponibile!")
			elif libro["disponibilità"] == "In prestito": 
				presenza = True
				print(titolo_indagato, "è in prestito")
		
	if presenza == False: 
		print("Non possediamo ancora", titolo_indagato, "ci dispiace!")

def elenco_libri(libri):
	for n in libri:
		print(n.get("nome"), ", di", n.get("autore"))

def rimuovi_libro(libro):
	titolo_rimosso = input("Scrivi il titolo del libro che hai danneggiato, bruciato, distrutto, smarrito o fatto esplodere: ")
	presenza = False
	for libro in libri:
		if titolo_rimosso == libro["nome"]:
			if libro["disponibilità"] == "In prestito":
				presenza = True
				libri.remove(libro)
				print(titolo_rimosso, "rimosso dall'elenco della biblioteca. Dovrai provvedere con la sostituzione entro 30 giorni. La prossima volta stai più attento :(")
			elif libro["disponibilità"] == "Disponibile": 
				presenza = True
				print("Non hai mai preso in prestito", titolo_rimosso, "forse era tuo... ma cerca di avere miglior cura anche dei tuoi libri!")
		
	if presenza == False: 
		print("Non abbiamo mai avuto", titolo_rimosso, "forse era tuo... ma cerca di avere miglior cura anche dei tuoi libri!")


print("Benvenuti sul sito della biblioteca di Pecorile!")
print()

command = ""
while command != "TERMINA":

	print("Per aggiungere un libro scrivi: AGGIUNGI")
	print("Per prendere in prestito un libro scrivi: PRESTITO")
	print("Per restituire un libro scrivi: RESTITUZIONE")
	print("Per controllare lo stato di un libro scrivi: STATO")
	print("Se hai distrutto, bruciato, perso o fatto esplodere il tuo libro scrivi: RIMUOVI")
	print("Se vuoi vedere il catalogo dei libri scrivi: STAMPA CATALOGO")
	print("Se hai terminato le operazioni e vuoi uscire, scrivi: TERMINA")

	command = input("Comando:")


	if command == "AGGIUNGI":
		aggiungi_elemento(libri)
		print()

	elif command == "PRESTITO":
		presta_libro(libri)
		print()

	elif command == "RESTITUZIONE":
		restituisci_libro(libri)
		print()

	elif command == "STATO":
		mostra_stato(libri)
		print()

	elif command == "RIMUOVI":
		rimuovi_libro(libri)
		print()

	elif command == "STAMPA CATALOGO":
		elenco_libri(libri)
		print()

	elif command != "TERMINA": 
		print("Comando non trovato, riprova!!!")
		print()

if command == "TERMINA":
	print("Arrivederci! Goodbye! Au revoir! Adios!")