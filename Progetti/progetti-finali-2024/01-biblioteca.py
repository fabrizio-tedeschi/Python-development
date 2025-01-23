#Creazione inventario
inventario = [
	{"titolo": "IT", "stato": "disponibile"},
	{"titolo": "Shining", "stato": "in prestito"},
	{"titolo": "LOTR", "stato": "scaduto"},
	{"titolo": "Vita Nova", "stato": "disponibile"},
	{"titolo": "Le notti bianche", "stato": "in prestito"}
]

#Menu
selezione = 0
while selezione != 5:
	print()
	print("------------------------------------------------------")
	print("Seleziona l'operazione da effettuare: ")
	print("1)Aggiungi libro all'inventario")
	print("2)Effettua prestito")
	print("3)Effettua restituzione")
	print("4)Stampa lista libri scaduti ")
	print("5)Esci")
	print()

	selezione = int(input("Operazione selezionata: "))
	if selezione == 1:
		aggiunta = {"titolo": "", "stato": "disponibile"}
		aggiunta["titolo"] = input("Aggiungi libro: ")
		inventario.append(aggiunta)

		for libro in inventario:
			print(libro)

		print()

	if selezione == 2:
		print("Elenco libri disponibili:")
		for libro in inventario:
			if libro["stato"] == "disponibile":
				print(libro["titolo"])

		prestito = input("Seleziona prestito: ")
		for libro in inventario:
			if libro["stato"] == "disponibile" and libro["titolo"] == prestito:
				libro["stato"] = "in prestito"
				print("Prestito effettuato....")
				break
	print()

	if selezione == 3:
		print("Elenco libri in prestito:")

		for libro in inventario:
			if libro["stato"] == "in prestito":
				print("libri in prestito", libro["titolo"])

		restituzione = input("Seleziona restituzione:")
		for libro in inventario:
			if libro["stato"] == "in prestito" and libro["titolo"] == restituzione:
				libro["stato"] = "disponibile"
				print("Restituzione effettuata...")
				print()

	if selezione == 4:
		for libro in inventario:
			if libro["stato"] == "scaduto":
				print(libro["titolo"])

#Grazie per queste lezioni! Ci siamo divertite un sacco!!
#Eleonora e Fatima <3