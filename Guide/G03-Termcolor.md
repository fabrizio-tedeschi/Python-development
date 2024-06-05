## Guida all'utilizzo della libreria termcolor

>Documentazione ufficiale della lbreria al [presente link](https://pypi.org/project/termcolor/).

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

### Colori

| Text colors | Text backgrounds |
|-------------|------------------|
| `black`     | `on_black`       |
| `red`       | `on_red`         |
| `green`     | `on_green`       |
| `yellow`    | `on_yellow`      |
| `blue`      | `on_blue`        |
| `magenta`   | `on_magenta`     |
| `cyan`      | `on_cyan`        |
| `white`     | `on_white`       |

### Attributi

* `bold`: grassetto
* `underline`: sottolineato
* `reverse`: inverte tutte le opzioni

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