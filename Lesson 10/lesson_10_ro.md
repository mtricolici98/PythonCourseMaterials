## dicționar

Dicționarul - prescurtat `dict` - este un alt tip de colecție. **Cea mai mare diferență față de o listă constă în faptul că într-un dicționar valorile nu sunt accesate prin index, ci printr-o "cheie".** Acest lucru înseamnă că în loc să folosim un index numeric pentru a accesa o valoare, utilizăm o cheie specifică asociată acelei valori.

Poți gândi un dicționar ca pe o colecție de perechi cheie-valoare. Fiecare pereche constă într-o **cheie** și o **valoare**. Cheia servește ca identificator unic pentru valoarea corespunzătoare.

Cheile dicționarului pot fi de orice tip imutabil, cum ar fi șiruri de caractere, numere sau tuple. Pe de altă parte, valorile dicționarului pot fi de orice tip, inclusiv dicționare în sine. Această flexibilitate permite dicționarelor să reprezinte structuri de date complexe și ierarhice.

Dicționarele sunt deosebit de utile pentru stocarea și recuperarea datelor, deoarece garantează că o anumită valoare va fi întotdeauna accesibilă la o anumită cheie. Acest lucru face ca căutarea în dicționar să fie foarte eficientă, mai ales atunci când știi cheia pe care o cauți.

### Cum se definește un dicționar

Dicționarele pot fi definite în două moduri.

1. Prin apelarea constructorului `dict()`. Poți crea un dicționar gol folosind constructorul sau poți furniza perechi cheie-valoare pentru a crea un dicționar ne-gol.

   ```python
   my_dict = dict()  # Dicționar gol creat cu ajutorul constructorului
   my_not_empty_dict = dict(my_key='Valoarea mea')  # Dicționar ne-gol creat cu ajutorul constructorului
   ```

2. Prin utilizarea acoladelor `{}` (similar cu mulțimile) și separând cheia de valoare cu două puncte `:`.

   ```python
   my_dict = {'cheia_mea': 'Valoarea mea'}
   ```

### De ce să utilizăm dicționarele

Dicționarele oferă o modalitate convenabilă de a stoca date dinamice. De exemplu, poți utiliza un dicționar pentru a stoca informații despre o persoană, cum ar fi numele, vârsta, profesia și hobby-urile.

```python
eu = {
    'nume': "Numele meu",
    'varsta': 20,
    'profesie': 'Polițist',
    'hobby-uri': ['Muzică', 'Citește cărți sportive', 'Găsirea scopului în viață']
}
```

Utilizarea dicționarelor îți permite să organizezi și să accesezi ușor mai multe informații

, fie că este vorba despre programul tău sau despre stocarea datelor într-un fișier sau o bază de date. Dicționarele acționează ca obiecte dinamice care pot fi modificate și extinse în timpul execuției, oferind o flexibilitate mare.

### Lucrul cu dicționarele

Dicționarele se comportă ca o combinație de mulțimi și liste.

Valorile din mulțimi pot fi parcurse, au o lungime și pot fi accesate folosind paranteze pătrate, la fel ca o listă. Similar, dicționarele au o lungime care reprezintă numărul de perechi cheie-valoare pe care le conțin.

```python
my_dict = {1: 'A', 'doi': 'DOI', 'a': 3}
len(my_dict)  # 3
```

#### Ce poate fi în interiorul unui dicționar?

**Valorile** dicționarului pot fi de orice tip, inclusiv alte dicționare. Acest lucru îți permite să creezi structuri de date complexe prin includerea de dicționare în dicționare.

**Cheile** dicționarului ar trebui să fie de tip de date imutabil pentru a te asigura că pot fi utilizate ca identificatori unici.

#### Accesarea valorilor

Accesarea valorilor într-un dicționar se face specificând cheia asociată valorii dorite. Dacă cheia nu există în dicționar, va fi generată o eroare.

```python
my_dict = {'cheia_mea': 'Valoarea mea'}
print(my_dict['cheia_mea'])  # Valoarea mea
```

#### Adăugarea/Modificarea valorilor

Pentru a adăuga sau modifica valorile într-un dicționar, poți atribui o valoare unei noi chei pentru a adăuga o nouă pereche cheie-valoare, sau poți atribui o valoare unei chei existente pentru a actualiza valoarea acesteia. Dacă o cheie nu există la momentul atribuirii, ea va fi creată.

```python
my_dict = {'cheia_mea': 'Valoarea mea'}
my_dict['cheia_mealalta'] = 'Valoarea mea alta'
print(my_dict['cheia_mealalta'])  # Valoarea mea alta
```

Este important de menționat că valorile dintr-un dicționar pot fi transmise direct sau ca referințe la obiecte.

## Referințe la obiecte

În Python, atribuirea valorii unei variabile **mutabile** altei variabile va crea o altă referință la aceeași valoare. Aceasta înseamnă că modificările efectuate într-o variabilă vor afecta și cealaltă variabilă.

```python
o_lista = [1, 2, 3]
o_alta_lista = o_lista
```

În exemplul de mai sus, atât `o_lista` cât și `o_alta_lista` se referă acum la același obiect de tip listă. Dacă modifici lista folos

ind oricare dintre variabile, lista însăși va fi actualizată.

```python
o_lista = [1, 2, 3]
o_alta_lista = o_lista
o_alta_lista.append(4)
print(o_lista)  # [1, 2, 3, 4]
```

Pentru a evita modificările neintenționate, trebuie să gestionezi cu atenție referințele la obiecte, în special atunci când lucrezi cu obiecte mutabile, cum ar fi liste și dicționare.

### Clonarea

Tipurile de date imutabile sunt clonate în mod implicit atunci când sunt atribuite unei noi variabile. Acest lucru înseamnă că se creează o copie a valorii, iar modificarea unei variabile nu afectează cealaltă.

Dacă dorești să faci o clonare a unui tip de date mutabil (de exemplu, o listă), poți utiliza constructorul listei `list()` sau metoda `.copy()` a listei.

```python
o_lista = [1, 2, 3]
o_lista_clonata = list(o_lista)
alta_clona = o_lista.copy()
o_lista_clonata.append(4)
print(o_lista)  # [1, 2, 3]
print(o_lista_clonata)  # [1, 2, 3, 4]
print(alta_clona)  # [1, 2, 3]
```

Prin crearea unei clone, poți lucra cu o copie separată a obiectului mutabil și o poți modifica independent.

## Iterație

Iterarea printr-un dicționar este posibilă și returnează cheile dicționarului. Poți utiliza cheile pentru a accesa valorile corespunzătoare.

```python
my_dict = {'prima': 1, 'a_doua': '2', 'a_treia': [1, 2, 3]}
for cheie in my_dict:
    print(my_dict[cheie])
# 1
# 2
# [1, 2, 3]
```

#### Doar valorile sau cheile

Este posibil să iterezi doar prin chei sau prin valorile unui dicționar folosind metodele `.keys()` și `.values()`.

```python
my_dict = {1: 'unu', 2: 'doi', 3: 'trei'}
for cheie in my_dict.keys():
    print(cheie)
# 1
# 2
# 3
for valoare in my_dict.values():
    print(valoare)
# unu
# doi
# trei
```

### Dicționarele pot fi încadrate

Da, poți avea un dicționar în interiorul altui dicționar, pe cât de multe niveluri ai nevoie. Acest lucru este util atunci când dorești să creezi structuri de date flexibile care pot fi adaptate cerințelor în schimbare.

```python
zboruri = {
    'Air Moldova': {
        'Sosiri': [dict(numar='AA1110', sursa='Frankfurt, DE', destinatie='Chișinău, MD')],
        'Plecări': [dict(num

ar='AA1111', sursa='Chișinău, MD', destinatie='Frankfurt, DE')]
    },
    'Ryanair': {
        'Sosiri': [dict(numar='FR231', sursa='Milano, IT', destinatie='Chișinău, MD')],
        'Plecări': [dict(numar='FR232', sursa='Chișinău, MD', destinatie='Milano, IT')]
    }
}
```

În acest exemplu, avem un dicționar care stochează informații despre zboruri de la diferite companii aeriene. Fiecare companie aeriană are propriile categorii de sosiri și plecări, reprezentate de liste de dicționare.

# Items

```python
my_dict = {1: 'one', 2: 'two', 3: 'three'}
for key, value in my_dict.items():
    print(f'Key: {key}, Value: {value}')
# Key: 1, Value: one
# Key: 2, Value: two
# Key: 3, Value: three
```

Metoda `.items()` este utilă atunci când dorești să lucrezi atât cu cheile, cât și cu valorile într-un buclă.

## Despachetarea (Unpacking)

**Despachetarea** în Python se referă la procesul de extragere a valorilor individuale dintr-o colecție. Aceasta îți permite să atribui mai multe variabile într-o singură linie de cod.

Să încercăm mai întâi despachetarea pe tupluri.

Tuplurile sunt ideale pentru despachetare deoarece au o dimensiune fixă, astfel încât știi întotdeauna câte elemente să aștepți. Cu toate acestea, poți utiliza despachetarea și cu liste, cu condiția ca numărul de variabile să se potrivească cu dimensiunea listei.

```python
my_tuple = (10, 20)
# Despachetează tuplul în variabilele a și b
a, b = my_tuple
print(a)  # 10
print(b)  # 20
```

Iată un exemplu de despachetare a mai multor valori:

```python
some_tuple = (10, 30, 'Da')
width, height, condition = some_tuple
```

Este important de remarcat că încercarea de a despacheta un număr diferit de valori decât dimensiunea tuplului sau listei va genera o eroare.

```python
tup = (10, 12)
a, b, c = tup  # Generează o eroare
```

Despachetarea poate fi realizată pe colecții de orice dimensiune, dar trebuie să fii atent la lizibilitatea și întreținerea codului când despachetezi colecții mari.

## Cuvântul cheie `in`: Verificarea apartenenței într-o colecție

În cazul dicționarelor, cuvântul cheie `in` verifică în mod implicit apartenența printre chei.

```python
my_dict = dict(a=1, b=2, c=3)
print('d' in my_dict)  # False
print('c' in my_dict)  # True
print(3 in my_dict)  # False
print(3 in my_dict.values())  # True
```

Poți utiliza cuvântul cheie `in` pentru a verifica dacă o anumită cheie există într-un dicționar. În plus, poți utiliza cuvântul cheie `in` împreună cu metoda `values()` pentru a verifica prezența unei valori în dicționar.

### Concluzie

Dicționarele sunt o modalitate flexibilă și puternică de a organiza și accesa datele în Python. Poți utiliza chei unice pentru a accesa și actualiza valorile asociate, permițându-ți să construiești structuri de date complexe și ierarhice. Dicționarele sunt utile într-o varietate de situații și oferă un mijloc eficient de a stoca și manipula informații.