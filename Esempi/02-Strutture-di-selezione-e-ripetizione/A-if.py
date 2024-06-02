#Input di un valore numerico
x = int(input("Inseire un valore numerico: "))

#Controllo del valore nuemerico
if x > 0:
    print("Il numero", x, "risulta POSITIVO!")
elif x < 0:
    print("Il numero", x, "risulta NEGATIVO!")
else:
    print("Il numero", x, "risulta NULLO!")