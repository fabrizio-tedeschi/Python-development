## Guida all'utilizzo della libreria termcolor

### Descrizione

La libreria `termcolor` permette di applicare colori al testo stampato su terminale.

### Installaione

Da terminale digitare la seguente linea di comando

```
pip install termcolor
```

Importare la libreria all'interno del file di lavoro

```python
import termcolor
```

### Utilizzo

La funzione `colored()` permette di ottenere "stringhe coloarate" che possono essere passate come parametri della `print()`.

```
colored(string, color, background, attrs=[att1, att2, ...])
```

### Esempio

```python
from termcolor import colored

text = colored("WARNING!", "white", "on_yellow")
print(text)

text = colored("ERROR!", "red")
print(text)

text = colored("Hello, World!", "green", attrs=["bold"])
print(text)
```