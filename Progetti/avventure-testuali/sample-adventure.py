print("------ AVVENTURA TESTUALE ------")
print("----- Il mistero del liceo -----")
print()
print("E' lunedi' mattina, inizia una nuova settimana, e sei gia' stanco, il solo pensiero che stia per iniziare\n",
      "una nuova settimana ti affligge e vorresti solo tornare a casa sul divano."
      )
print()
print("Tuttavia quando entri a scuola noti qualcosa di strano: la porta del ripostiglio sempre chiusa e' stata lasciata aperta...")
print()
print("1) Decidi di andare in classe")
print("2) Decidi di indagare piu' a fondo")
scelta = int(input("- Inseire una scelta: "))

if scelta == 1:
    print()
    print("Inizia ad avviarti verso la classe tuttavia ti accorgi che il tuo amico Jack ha deciso di indagare e decidi di seguirlo...")
    print("Anche le tue amiche Nora e Dora vi raggiungono e iniziare l'indagine...")
elif scelta == 2:
    print()
    print("Avvisi i tuoi amici Jack, Nora e Dora ed iniziate ad indagare...")

print()
print("Attraversate la porta misteriosa, e' buio, cercate un interruttore della luce, iniziate a scendere lungo un'antica\n",
      "scala a chiocciola..."
      )
print("Arrivate nel sotterraneo segreto della scuola, anche qui niente luce...")
print()
print("1) Accendi la torcia del telefono")
print("2) Dici a tutti di cercare l'interruttore della luce")
scelta = int(input("- Inseire una scelta: "))

if scelta == 1:
    print()
    print("Accendi la torcia del telefono, intravedete un quadro elettrico, lo attivate e riuscite a scoprire che il sotterraneo segreto\n",
          "in realta' e' una discoteca riservata ai professori. Le pareti sono piene di foto abbastanza imbarazzanti. C'e' persino una\n",
          "foto del prof d informatica che balla sul tavolo..."
          )
    print()
    print("1) Decidete di attivare l'impianto e divertirvi")
    print("2) Decidete di tornare in classe a lezione")
    s2 = int(input("- Inseire una scelta: "))

    if s2 == 1:
        print()
        print("Iniziate a ballare e a divertirvi tuttavia gli imprevisti sono dietro l'angolo.")
        print("Jack è molto distratto accidentalmente colpisce il pulsante dell'allarme antincendio.")
    else:
        print()
        print("Da bravi alunni responsabili decidete di tornare in classe.")
        print("Mentre state uscendo pero' Nora colpisce con lo zaino un grosso pulsante rosso sulla parete.")
elif scelta == 2:
    print()
    print("Iniziate a cercare l'interruttore della luce ma poiche' non si vede nulla la ricerca non produce risultati.")
    print("Finalmente Dora trova un interruttore tondo e decide di premerlo...")

print("Scatta l'allarme antincendio, i dispositivi di sicurezza iniziano spruzzare acqua in tutta la scuola, il panico dilaga.")
print("Tutti gli studenti iniziano ad evaquare...")

print()
print("1) Decidete di evaquare e andare nel cortile della scuola")
print("2) Decidete di rimanere nascosti sperando di non essere scoperti")
scelta = int(input("- Inseire una scelta: "))

if scelta == 1:
    print()
    print("Approffittate della confusione per confondervi con la folla. Una volta in cortile raggiungete il vostro gruppo di classe.")
    print("Il docente effettua l'appello. Nessuno sospetta di voi. Decidete di mantenere segreta la vostra avventura.")
    print("Nessuno sapra' mai chi ha fatto scattare l'allarme antincendio.")
    print("VITTORIA :)")
elif scelta == 2:
    print()
    print("Rimanete nascosti nella speranza di non essere scoperti.")
    print("Arrivano i vigili del fuoco incaricati di spegnere l'allarme ed effettuano una ispezione in tutto l'istituoto\n",
          "per cercare la causa dell'accaduto. Ispezionano anche il sotterraneo...")
    print("Venite scoperti dai vigili del fuoco, il preside e' furioso, siete stati sospesi per una settimana.")
    print("SCONFITTA :(")