
# Funcții continuate

## Importarea funcțiilor din alte fișiere

Python permite importarea valorilor, funcțiilor și altor elemente din diferite fișiere.

Acest lucru este cel mai bine explicat printr-un exemplu.

Să creăm un fișier:

functions.py

```python
# functions.py
def smiley_function(text, smiley_face=':)'):
    print(f'{smiley_face} {text}')
```

În fișierul de mai sus avem o funcție pe care am putea dori să o folosim în diferite fișiere Python.

În Python, există două moduri de a importa lucruri (obiecte, variabile, funcții):

1. Importarea întregului modul folosind cuvântul cheie **import**
2. Importarea funcției/obiectului/variabilei specifice, folosind **from** _modul_ **import** _nume_funcție_

Pentru a continua, să creăm un alt fișier.

program.py (sau orice alt nume doriți)

Exemplu: Importarea întregului modul

```python
# program.py

import functions

functions.smiley_function('Rulez o funcție dintr-un fișier diferit')
```

Codul de mai sus va importa întregul modul functions.py în scriptul Python curent.

Exemplu 2: Importarea doar a funcției

```python
# program.py

from functions import smiley_function

smiley_function('Rulez o funcție dintr-un fișier diferit')
```

Exemplul de mai sus importă doar funcția **smiley_function** din modulul **functions**

### Importarea mai multor funcții din același modul.

Dacă dorim să adăugăm mai multe funcții în fișierul nostru **functions.py**, putem face acest lucru cu ușurință.

```python
# functions.py
def smiley_print_function(text, smiley_face=':)'):
    print(f'{smiley_face} {text}')


def number_input_function():
    user_input = input('Te rog introdu un număr întreg: ')
    if user_input.isnumeric():
        return int(user_input)
    else:
        return smiley_print_function('Te-am rugat să introduci un număr întreg')
```

Și dacă dorim să importăm mai mult de o funcție folosind sintaxa **from ... import**, putem face acest lucru prin separarea numelui funcțiilor prin virgulă (**,**).

```python
# program.py
from functions import smiley_print_function, number_input_function
```

### Ce este un modul

Modulele sunt pur și simplu fișiere **.py** care pot fi importate în alte fișiere **.py**. Le putem considera ca fiind biblioteci care conțin diverse funcții pe care dorim să le utilizăm în mai multe locuri (programe/scenarii)

Poți avea un întreg folder care acționează ca un modul. Aceasta este ceea ce se numește un pachet.

Pe măsură ce proiectul nostru va deveni tot mai complex, vom începe să vedem mai des sub-module/pachete.

## Declararea un

ui pachet

După cum am spus, un pachet este un folder care conține mai multe fișiere **.py** sau alte pachete.

Să spunem că avem o structură ca mai jos

````
Proiect
|---proiect_utilitare
|   |---__init__.py
|   |---utilitare_bază_date.py
|   |---utilitare_data_și_oră.py
|---servicii
|   |---__init__.py
|   |---serviciu_bază_date.py
|   |---utilitare_fișiere.py
|---main.py
````

Logica programului nostru poate fi în **main.py**

În **main.py** s-ar putea să vrem să accesăm unele dintre utilitățile și serviciile noastre

```python
# main.py

from proiect_utilitare.utilitare_bază_date import procesare_rezultat_interogare
from servicii.serviciu_bază_date import interogare_bază_date


def main():
    rezultat_interogare = interogare_bază_date(...)
    lista_rezultate = procesare_rezultat_interogare(rezultat_interogare)
```

## Fișierul __init__

Fișierul init este un fișier opțional (începând cu Python 3.6) care declară că folderul este un modul Python.

Fișierele init sunt folosite în principal pentru a oferi "scurtături" către funcții sau sub-module în cadrul modulului nostru.

De exemplu:

```python
# Project.servicii.__init__.py
# Importarea funcțiilor din modulul serviciu_bază_date în rădăcina pachetului pentru un acces mai ușor
from serviciu_bază_date import interogare_bază_date, creare_bază_date, creare_tabel, ștergere_tabel, ștergere_bază_date

```

Acum, deoarece fișierul nostru __init__ importă funcții din **serviciu_bază_date**, le putem accesa direct din modulul **servicii**.

```python
# Acum putem face asta, deoarece pachetul servicii importă deja funcțiile din serviciu_bază_date
from servicii import interogare_bază_date
# În loc de asta
from servicii.serviciu_bază_date import interogare_bază_date
```

Fișierul init poate fi, de asemenea, folosit pentru a inițializa o anumită logică comună în pachet.

De exemplu, în fișierul init al serviciilor noastre am putea dori să verificăm dacă există un folder pentru a stoca fișierele programului și să îl creăm în caz contrar, am putea, de asemenea, să stabilim o conexiune la baza de date

```python
# Project.servicii.__init__.py

from serviciu_bază_date import *
from utilitare_fișiere import *

# Efectuăm logica de inițializare pentru pachetul nostru

# Verificăm dacă baza de date există


if not există_bază_date('BAZĂ_DATE_PREDEFINITĂ'):
    # creăm baza de date
    creare_bază_date('BAZĂ_DATE_PREDEFINITĂ')

# Verificăm dacă există folderul pentru fișiere
if not există_folder('fișiere_program'):
    # Creăm folderul
    creare_folder('fișiere_program')
```

Trebuie să fii atent la logica de inițializare pentru un pachet, deoarece aceasta va rula de fiecare dată când pachetul este importat.

### name == main

Îți amintești de ``if __name__ == '__main__': ``?

Ei bine, aici devine foarte important.

Dacă fișierul nostru functions.py conține orice cod care rulează în cadrul scriptului, acesta va fi evaluat și în timpul importului.

```python
# functions.py
def smiley_function(text, smiley_face=':)'):
    print(f'{smiley_face} {text}')


smiley_function('Testez funcția mea')
```

Dacă acum importăm modulul **functions**, apelul smiley_function **din interiorul modulului** va fi executat.

```python
import functions  # Va afișa ':) Testez funcția mea'
```

Pentru a remedia acest lucru, folosim ``__name__ == '__main__'``

Acesta va verifica dacă codul este evaluat nu ca parte a unei importări, ci ca parte a execuției scriptului.

```python
# functions.py
def smiley_function(text, smiley_face=':)'):
    print(f'{smiley_face} {text}')


if __name__ == '__main__':
    smiley_function('Testez funcția mea')
```

Acum, dacă importăm modulul functions, **smiley_function** din modulul functions nu va fi executat.

Dar dacă rulăm programul functions.py, acesta va afișa totuși **':) Testez funcția mea'**

### Importarea mai multor funcții/valori cu același nume

Să zicem că avem 2 funcții în pachete diferite care au același nume

functions.py

```python
def factorial(nr):
    pass  # Implementează factorialul aici
```

main.py

```python
from functions import factorial
from math import factorial
```

Mai sus am importat 2 funcții cu numele factorial. Aceasta înseamnă că va fi utilizată doar funcția de jos.

Dacă dorești să folosești ambele funcții separat, poți da funcției un pseudonim. Folosind cuvântul cheie **as**

```python
from functions import factorial as my_factorial
from math import factorial as math_factorial
```

### Nu te îngrijora de importuri în acest moment

Importurile sunt foarte importante în lucrul cu programe mici sau mari, dar nu trebuie să-ți faci griji, deoarece, în cea mai mare parte a timpului, IDE-ul tău te va ajuta cu ele.

# Excepții (erori)

Excepțiile sunt o parte a unui program care indică utilizatorului, sistemului și programului că ceva nu a mers bine.

Excepțiile sunt o parte esențială a trusoului dezvoltatorului, deoarece îi permite să comunice ușor că ceva neașteptat s-a întâmplat.

Excepțiile sunt o modalitate de a comunica altor părți ale programului că "S-a întâmplat ceva ce nu ar fi trebuit să se întâmple".

Dar uneori nu dorim excepții. Uneori, dorim să le ignorăm sau să le cerem utilizatorului să încerce din nou.

Am putea verifica totul peste tot cu instrucțiuni **if** pentru a evita apariția excepțiilor, dar acest lucru ar fi foarte neproductiv. În schimb, putem permite apariția excepțiilor și să le gestionăm.

### Gestionarea erorilor

În Python, erorile sunt gestionate folosind un bloc **try: except:**.

Blocurile Try-Except sunt similare cu blocurile **if: else:**.

Codul din blocul **try** se va executa dacă nu apar erori, iar codul din blocul **except** se va executa doar dacă apare o eroare în blocul **try**.

Exemplu:

```python
try:
    print('Unele Text aleator' + 120)
except:
    print('A apărut o eroare, dar programul continuă să ruleze')
```

### Gestionarea erorilor preconizate

Putem declara ce fel de eroare așteptăm să apară pentru a o gestiona în mod corespunzător.

Exemplu:

```python
try:
    print(int(input('Introduceți un număr')))
except ValueError:
    print("Utilizatorul nu a introdus un număr valid")
```

Este, de asemenea, posibil să se gestioneze orice eroare. Acest lucru se face prin gestionarea excepțiilor de tipul **Exception**.

```python
try:
    print(int(input('Introduceți un număr')))
except Exception:
    print("Ceva nu a mers conform planului")
```

### Aflarea tipului de eroare

Puteți utiliza cuvântul cheie **as** pentru a păstra instanța erorii (excepției) într-o variabilă.

Pentru a utiliza **as**, **trebuie** să declarați tipul excepției.

Majoritatea excepțiilor din Python sunt derivate din clasa **Exception**. Acest lucru înseamnă că, dacă încercați să gest

ionați **Exception**, probabil veți prinde toate excepțiile.

```python
try:
    print('Unele Text aleator' + 120)
except Exception as eroare:
    print(f"Eșec cu eroarea: {str(eroare)}")
```

### Când este util acest lucru?

De exemplu, s-ar putea să aveți nevoie să utilizați un serviciu extern, a cărui calitate sau fiabilitate nu o puteți încredința niciodată.

În acest caz, s-ar putea să doriți să încercați de câteva ori sau să utilizați o soluție alternativă, sau poate să anunțați pe cineva că ceva nu a mers bine.

Exemplu simplu: Asigurarea că utilizatorul introduce o valoare de tip float

```python
def convert_to_float(string):
    try:
        return float(string)
    except ValueError:
        return None  # Utilizatorul nu a introdus un șir valid de tip float


def main():
    maybe_number = None
    while maybe_number is None:
        maybe_number = convert_to_float(input('Introduceți o valoare numerică'))
        if maybe_number is not None:
            print(f'Mulțumim pentru {maybe_number}')
        else:
            print(f'Încercați să introduceți un număr de această dată')
```

Un exemplu mai complex: Încercarea de a se conecta de mai multe ori la un serviciu extern

```python
# Acest cod este un exemplu și nu este funcțional
def get_connection_to_aws(max_retries):
    retries = 0
    connection = None
    while retries < max_retries:
        try:
            connection = connect_to_amazon_service(CONN_URL, CONN_KEY)  # Exemplu de funcție
            return connection
        except Exception as ex:
            print(f'Conexiunea a eșuat, motiv: {str(ex)}')
            retries += 1
    if connection is None:
        send_mails_to_admin(str(ex))
```

### Evitați excepțiile generale

Instrucțiunea **except** permite dezvoltatorului să specifice ce tip de excepții ar trebui să gestioneze blocul except.

Aceasta nu este doar o sugestie. Dacă declarația except este prea generală, s-ar putea să gestionați excepții care nu ar fi trebuit să fie gestionate.

Dacă nu specificați o excepție, codul va continua să ruleze chiar dacă excepția este un eveniment de sistem, de exemplu o întrerupere de la tastatură, care ar trebui să închidă orice aplicație.

```python
try:
    number = int(input('Introduceți un număr'))
    result = 10 / number
except:  # FOARTE RĂU, deoarece nu știm exact ce a eșuat
    pass  # Cod
```

```python
try:
    number = int(input('Introduceți un număr'))
    result = 10 / number
except ArithmeticError as err:  # Mult mai bine
    pass  # Cod
```

În mod norocos, IDE-ul vă va avertiza cu privire la excepțiile gener

ale, dar totuși, fiți atenți.

### Excepțiile sunt gestionate doar când apar

Acest lucru înseamnă că orice cod din interiorul blocului **try** se va executa până când întâlnește eroarea.

```python
try:
    print('Tipăresc ceva')
    print('Tipăresc altceva')
    print(10 / 0)
    print('Tipăresc la sfârșit')
except ZeroDivisionError:
    print('Excepție gestionată')
# Tipăresc ceva
# Tipăresc altceva
# Excepție gestionată
```

Codul din blocul **try** se va executa numai până când întâlnește eroarea.

### În cele din urmă

Fundamental, blocurile **try: except** funcționează similar cu acesta:

```
# Rulează codul
if eroare:
    # Rulează blocul except
```

Dar ele oferă și un bloc **finally**. Pentru ce este folosit?

```python
def convert_to_float():
    value = None
    try:
        value = float(input('Introduceți un float'))
    except ValueError as ex:
        print(f"Input nevalid de la utilizator: {str(ex)}")
    finally:
        return value
```

În blocul **finally**, programatorii de obicei fac "curățenie". Deci înlătură tot ce a mai rămas după o execuție **try: except** de succes sau eșuată.

Exemplu:

```python
try:
    make_database_query(database, query)  # Încercarea de a face o interogare în această bază de date
except Exception as ex:
    print(f"Baza de date a avut o problemă: {str(ex)}")  # Baza de date nu a reușit să facă interogarea
finally:
    close_database_connection(database)  # Închideți conexiunea la baza de date, chiar dacă interogarea a eșuat
```

### Ridicarea excepțiilor

Ridicarea (sau crearea) unei excepții poate fi realizată utilizând cuvântul cheie **raise** și ne permite să creăm erori oriunde în codul nostru.

Toate excepțiile au un corp standard care poate conține mesajul.

```python
def find_index(list_to_lookup, item_to_find):
    for index in range(len(list_to_lookup)):
        if list_to_lookup[index] == item_to_find:
            return index
    raise Exception('Elementul nu a fost găsit')


try:
    find_index([1, 2, 3], 4)
except Exception as ex:
    print(str(ex))  # Oups, ceva nu a mers bine...
```

### Tipuri de excepții.

Toate excepțiile extind clasa **BaseException**. Deci, dacă încercați să prindeți **BaseException**, veți _prinde toate excepțiile_.

Aceasta nu este niciodată o situație bună, dar totuși sunteți capabil să extindeți și să creați propriile excepții.

Dar este recomandat să extindeți clasa **Exception**.

```python
class MyCustomException(Exception):
    pass  # Nu avem nevoie de un corp
```

### Ridicarea excepțiilor personalizate

```python
class ItemNotFoundError(Exception):
    pass  # Nu avem nevoie de un corp


def find_index(list_to_lookup, item_to_find):
    for index in range(len(list_to_lookup)):
        if list_to_lookup[index] == item_to_find:
            return index
    raise ItemNotFoundError('Elementul nu a fost găsit')


try:
    find_index([1, 2, 3], 4)
except ItemNotFoundError as ex:
    print('Elementul nu a fost găsit')
```

### Prinderea mai multor excepții

Puteți prinde mai multe excepții, nu doar una, și acest lucru poate fi realizat în două moduri, grupându-le într-un singur bloc **except** sau având un bloc **except** separat pentru fiecare.

```python
try:
    a = int(input('a'))
    b = int(input('b'))
    print(a / b)
except ZeroDivisionError as ex:
    print('Nu ai fost la școală')
except ArithmeticError as ex:
    print('Acele numere nu au sens')
except ValueError as ex:
    print('Unul dintre valorile furnizate nu este un număr')
except Exception as ex:
    print('Nu știu ce s-a întâmplat, dar știu că este rău...')
```

Exemplul **de mai sus** va executa un bloc **except** specific, în funcție de tipul excepției care a fost ridicată.

```python
try:
    a = int(input('a'))
    b = int(input('b'))
    print(a / b)
except (ZeroDivisionError, ArithmeticError) as ex:
    print('Acele numere nu au sens')
except Exception as ex:
    print('Nu știu ce s-a întâmplat, dar știu că este rău...')
```

De asemenea, puteți furniza o tuplă de clase de excepții, pe care un singur bloc **except** le va prinde.

#### Notă: Ordinea excepțiilor contează, la fel ca în cazul blocurilor **elif**.