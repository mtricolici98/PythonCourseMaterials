# Lecția 12: Funcții în Python

În această lecție, vom explora conceptul de funcții în Python și vom înțelege importanța lor în crearea de cod modular și reutilizabil. Vom acoperi diverse aspecte ale funcțiilor, inclusiv argumente de funcție, valori de returnare, efecte secundare, argumente implicite și sugestii de tip de argumente. Hai să începem!

### Ce sunt funcțiile?

Funcțiile sunt blocuri de cod care efectuează o anumită sarcină. Ele ne permit să încapsulăm un set de instrucțiuni și să le executăm apelând numele funcției. Funcțiile pot primi argumente de intrare, le pot prelucra și, opțional, pot returna o valoare.

Iată un exemplu de funcție simplă care salută o persoană:

```python
def salut(nume):
    print("Salut, " + nume + "!")

# Apelarea funcției salut()
salut("John")
```

Output:
```
Salut, John!
```

În acest exemplu, funcția `salut()` primește un argument `nume` și afișează un mesaj de salut cu numele furnizat.

### Cuvântul cheie "pass"

Cuvântul cheie "pass" este utilizat ca marcator de loc atunci când dorim să creăm o funcție sau un bloc de cod fără nicio implementare. Acesta se asigură că codul este corect din punct de vedere sintactic. Să vedem un exemplu:

```python
def functie_marcaj():
    pass

# Apelarea funcției marcator
functie_marcaj()
```

Nu va fi generat niciun rezultat din această funcție deoarece nu are nicio implementare încă. Cu toate acestea, este o funcție validă care poate fi completată mai târziu.

### Docstrings

Docstrings sunt șiruri literale utilizate pentru a documenta modulele Python, clasele, metodele și funcțiile. Ele servesc ca documentație inline, furnizând informații despre scopul, utilizarea și parametrii funcției.

Iată un exemplu de funcție cu un docstring:

```python
def aduna_numere(a, b):
    """
    Adună două numere și returnează rezultatul.
    Parametri:
    a (int): Primul număr
    b (int): Al doilea număr
    Returnează:
    int: Suma celor două numere
    """
    return a + b

# Accesarea docstring-ului
print(aduna_numere.__doc__)
```

Output:
```
Adună două numere și returnează rezultatul.
Parametri:
a (int): Primul număr
b (int): Al doilea număr
Returnează:
int: Suma celor două numere
```

Atributul `__doc__` ne permite să accesăm docstring-ul asociat funcției.

### Argumente de Funcție

Python suportă trei tipuri

 de argumente de funcție: argumente poziționale, argumente pe bază de cuvinte cheie și argumente implicite.

**Argumente poziționale**:
Aceste argumente sunt transmise în funcție de poziția lor în apelul funcției. Valorile sunt atribuite parametrilor corespunzători în definiția funcției.

```python
def salut(nume, varsta):
    print("Salut, " + nume + "! Ai " + str(varsta) + " de ani.")

# Apelarea funcției salut() cu argumente poziționale
salut("Alice", 25)
```

Output:
```
Salut, Alice! Ai 25 de ani.
```

În acest exemplu, parametrii `nume` și `varsta` sunt argumente poziționale, iar valorile le sunt atribuite în funcție de poziția lor în apelul funcției.

**Argumente pe bază de cuvinte cheie**:
Argumentele pe bază de cuvinte cheie sunt transmise împreună cu numele lor de parametri în apelul funcției. Aceasta permite o mai mare flexibilitate și lizibilitate.

```python
def salut(nume, varsta):
    print("Salut, " + nume + "! Ai " + str(varsta) + " de ani.")

# Apelarea funcției salut() cu argumente pe bază de cuvinte cheie
salut(nume="Bob", varsta=30)
```

Output:
```
Salut, Bob! Ai 30 de ani.
```

Aici, apelul funcției menționează în mod explicit numele parametrilor, ceea ce face mai ușor de înțeles valorile transmise.

**Argumente implicite**:
Argumentele implicite au valori predefinite și pot fi omise în apelul funcției. Dacă nu se furnizează nicio valoare, se utilizează valoarea implicită.

```python
def salut(nume, mesaj="Bun venit"):
    print(mesaj + ", " + nume + "!")

# Apelarea funcției salut() cu și fără argumentul mesaj
salut("Alice")
salut("Bob", "Salutări")
```

Output:
```
Bun venit, Alice!
Salutări, Bob!
```

În acest exemplu, parametrul `mesaj` are o valoare implicită de "Bun venit". Dacă argumentul nu este furnizat în apelul funcției, se utilizează valoarea implicită.

### Returnarea Valorilor din Funcții

Funcțiile pot returna valori folosind instrucțiunea `return`. Valoarea returnată poate fi de orice tip de date. Atunci când o funcție întâlnește o instrucțiune `return`, ea se încheie imediat, iar valoarea specificată este transmisă înapoi apelantului.

```python
def patrat(numar):
    return numar * numar

# Apelarea funcției patrat() și stocarea valorii returnate
rezultat = patrat(5)
print(rezultat)
```

Output:
```
25
```

Funcția `

patrat()` calculează pătratul unui număr și returnează rezultatul. Putem captura valoarea returnată și o putem utiliza în alte părți ale codului nostru.

### Efectele Secundare ale Funcțiilor

Funcțiile pot avea efecte secundare, care apar atunci când o funcție modifică ceva în afara propriului său scop. Efectele secundare includ modificarea valorii unei variabile globale, modificarea unei structuri de date sau afișarea rezultatelor la consolă.

```python
numar = 0

def incrementeaza_contor():
    global numar
    numar += 1

# Apelarea funcției incrementeaza_contor() de mai multe ori
incrementeaza_contor()
incrementeaza_contor()
incrementeaza_contor()

print(numar)
```

Output:
```
3
```

În acest exemplu, funcția `incrementeaza_contor()` modifică valoarea variabilei globale `numar`, incrementând-o. Funcția are un efect secundar asupra variabilei.

### Argumente poziționale vs. Argumente pe bază de cuvinte cheie

Python permite utilizarea atât a argumentelor poziționale, cât și a argumentelor pe bază de cuvinte cheie împreună în apelurile de funcții. Argumentele poziționale trebuie furnizate în aceeași ordine ca și parametrii din definiția funcției, în timp ce argumentele pe bază de cuvinte cheie sunt transmise cu numele parametrilor.

```python
def salut(nume, mesaj):
    print(mesaj + ", " + nume + "!")

# Apelarea funcției salut() cu o combinație de argumente poziționale și pe bază de cuvinte cheie
salut("Alice", mesaj="Salut")
salut(mesaj="Salutări", nume="Bob")
```

Output:
```
Salut, Alice!
Salutări, Bob!
```

Amestecarea ambelor tipuri de argumente oferă flexibilitate și îmbunătățește claritatea invocărilor funcțiilor.

### Sugestii de Tip de Argumente

Python suportă sugestii de tip, care ne permit să specificăm tipurile așteptate pentru argumentele și valorile de returnare ale funcțiilor. Cu toate că sugestiile de tip nu sunt impuse de interpretor, ele servesc ca documentație și pot fi verificate folosind verificatoare de tipuri statice, cum ar fi `mypy`.

```python
def aduna_numere(a: int, b: int) -> int:
    return a + b

# Apelarea funcției aduna_numere() cu tipuri de argumente incorecte
rezultat = aduna_numere("2", 3)
print(rezultat)
```

Output:
```
TypeError: can only concatenate str (not "int") to str
```

În acest exemplu, am furnizat tipuri de argumente incorecte, ceea ce a condus la o `TypeError`. Sugițiile de tip ajută la identificarea potențialelor erori

 de tip în timpul dezvoltării.

### Concluzie

Funcțiile sunt componente esențiale ale programării în Python și ne permit să încapsulăm și să reutilizăm codul. Ele pot avea argumente, valori returnate și efecte secundare. Argumentele pot fi de tipuri poziționale sau pe bază de cuvinte cheie și pot avea valori implicite. Sugestiile de tip ne ajută să documentăm și să verificăm corectitudinea tipurilor în funcții.

În această lecție, am acoperit concepte fundamentale legate de funcții în Python. Continuați să exersați și să explorați utilizarea funcțiilor în proiectele dvs., deoarece acestea sunt un instrument puternic în dezvoltarea de aplicații.