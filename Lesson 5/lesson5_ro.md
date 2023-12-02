# Lecția 4 - Secvențe, Liste

## Ce sunt secvențele?

Până acum, am lucrat în principal cu tipuri de date de bază precum întregi, zecimale și șiruri de caractere. Aceste tipuri de date sunt excelente pentru stocarea unei singure valori. Cu toate acestea, există situații în care avem nevoie să stocăm mai multe valori într-o singură variabilă. Aici intervin secvențele. Secvențele sunt tipuri de date care ne permit să stocăm mai mult de o valoare.

## Liste

Lista este probabil cea mai folosită secvență în Python. Este exact ceea ce sună - o listă de elemente.

Elementele dintr-o listă pot fi de orice tip. De exemplu, puteți avea o listă care conține 3 numere și 2 cuvinte. Această flexibilitate nu este întotdeauna disponibilă în alte limbaje de programare.

Caracteristicile cheie ale listelor sunt:

* **Ordonate**: Liste mențin ordinea în care au fost adăugate elementele.
* **Modificabile**: Puteți modifica orice element din listă, indiferent de poziția sa.
* **Non-Unice**: O listă poate conține mai multe apariții ale aceleiași valori.

Există două moduri de a declara o listă goală: folosind constructorul de listă sau folosind paranteze pătrate ([]).

```python
my_list = list()
also_list = []
```

De asemenea, puteți crea liste nevide direct.

```python
non_empty = [1, 2, 3]
```

### O colecție pe care o cunoașteți deja

Am lucrat anterior cu șiruri de caractere și am menționat că un șir de caractere este în esență o listă de caractere și se comportă ca atare.

### Accesarea valorilor

Valorile dintr-o listă pot fi accesate folosind indexul lor, care reprezintă poziția lor în listă. Similar cu șirurile de caractere, indexul începe de la 0.

```python
my_list = ['first', 'second', 'third']
print(my_list[0])  # first
print(my_list[1])  # second
print(my_list[2])  # third
print(my_list[3])  # Eroare: index în afara intervalului
```

Indicii negativi pot fi, de asemenea, utilizați, și puteți obține subliste prin tăierea unei liste.

```python
my_list = ['one', 'two', 'three']
print(my_list[-2])  # two
print(my_list[-2:])  # ['two', 'three']
print(my_list[0:2])  # ['one', 'two']
```

### Listele sunt mutable

Listele sunt mutable, ceea ce înseamnă că puteți schimba elementele lor sau adăuga elemente noi fără a crea o nouă instanță de listă.

Pentru a schimba un element într-o listă, atribuiți o valoare nouă elementului la un anumit index.

```python
my_list = [1, 2, 3]
my_list[1] = 4
print(my_list)  # [1, 4, 3]
my_list[1] = 'two'
print(my_list)  # [1, 'two', 3]
```

### Adăugarea elementelor într-o listă

Există două modalități principale de adăugare a elementelor într-o listă:

1. Utilizând funcția **.append()**.
2. Combinați cu o altă listă (concatenarea listelor).

```python
my_list = []
# Utilizând append
my_list.append('Primul element')

# Concatenarea listelor (similar concatenării șirurilor de caractere) adaugă cele două liste împreună.
my_list = my_list + ['Al doilea element']

# SAU

my_list += ['Al doilea element']

print(my_list)  # ['Primul element', 'Al doilea element']
```

Concatenarea listelor este posibilă și utilizând funcția dedicată **.extend()**.

### Eliminarea elementelor dintr-o listă

#### Utilizând **remove()**

Puteți elimina un element dintr-o listă utilizând funcția **.remove()**. Această metodă primește valoarea elementului pe care doriți să-l eliminați ca argument.

```python
my_list = [1, 2, 3]
my_list.remove(1)
print(my_list)  # [2, 3]
```

Dacă elementul apare de mai multe ori în listă, va fi eliminată doar prima apariție. Dacă elementul nu există în listă, se va genera o eroare ValueError.

```python
my_list = [1, 2, 2, 3]
my_list.remove(2)
print(my_list)  # [1, 2, 3]
```

#### Utilizând **del**

Cuvântul cheie **del** vă permite să eliminați un element dintr-o listă utilizând indexul acestuia.

```python
my_list = [1, 2, 3]
del my_list[1]
print(my_list)  # [1, 3]
```

De asemenea, puteți elimina o secțiune a unei liste utilizând cuvântul cheie **del**.

```python
my_list = [1, 2, 3, 4, 5]
del my_list[1:3]
print(my_list)  # [1, 4, 5]
```

#### Utilizând **pop()**

Funcția **.pop()** elimină un element dintr-o listă la un anumit index și returnează valoarea elementului eliminat. Dacă nu se specifică un index, se elimină ultimul element din listă.

```python
my_list = [1, 2, 3]
item_șters = my_list.pop(1)
print(my_list)        # [1, 3]
print(item_șters)     # 2

ultimul_element = my_list.pop()
print(my_list)        # [1]
print(ultimul_element)      # 3
```

### Metode și funcții pentru liste

Listele au mai multe metode și funcții încorporate care vă permit să le manipulați și să lucrați cu ele:

- **len()**: Returnează numărul de elemente dintr-o listă.
- **count()**: Returnează numărul de apariții ale unui element specific într-o listă.
- **index()**: Returnează indexul primei apariții a unui element specific într-o listă.
- **sort()**: Ordonează elementele într-o listă în ordine crescătoare.
- **reverse()**: Inversează ordinea elementelor într-o listă.
- **clear()**: Elimină toate elementele dintr-o listă.
- **copy()**: Creează o copie superficială a unei liste.
- **extend()**: Adaugă toate elementele dintr-o altă listă la sfârșitul listei curente.

Aceste metode pot fi apelate utilizând notația punctată pe un obiect de tip listă.

```python
my_list = [1, 2, 2, 3, 4, 5]

print(len(my_list))            # 6
print(my_list.count(2))        # 2
print(my_list.index(3))        # 3

my_list.sort()
print(my_list)                 # [1, 2, 2, 3, 4, 5]

my_list.reverse()
print(my_list)                 # [5, 4, 3, 2, 2, 1]

my_list.clear()
print(my_list)                 # []

new_list = [1, 2, 3]
copied_list = new_list.copy()
print(copied_list)             # [1, 2, 3]

other_list = [4, 5, 6]
new_list.extend(other_list)
print(new_list)                # [1, 2, 3, 4, 5, 6]
```
## Bucle **for**, iterație

Unul dintre principalele piloni ai programării este iterația. **Iterația** este procesul de a face aceeași acțiune de mai multe ori cu valori diferite.

În Python, una dintre modalitățile de a realiza iterația este prin utilizarea buclelor **for**. Buclele **for** se realizează utilizând blocuri **for ... in ...** în Python. Puteți itera prin diferite colecții cum ar fi liste și tupluri.

Iată un exemplu care demonstrează iterarea printr-o listă și afișarea fiecărui element:

```python
my_list = ['Primul', 'Al doilea', 'Al treilea']
for element in my_list:
    print(element)
# Output:
# Primul
# Al doilea
# Al treilea
```

Puteți itera prin tupluri în același mod ca și prin orice altă colecție:

```python
data = (52, 29, 39)
for el in data:
    print(el)
```

Să considerăm un exemplu mai practic. Să presupunem că dorim să calculăm suma unei liste de numere:

```python
my_numbers = [10, 20, 14, 92, 20]
numbers_sum = 0  # Inițializarea variabilei noastre colectoare
for number in my_numbers:
    numbers_sum += number  # Adăugăm la variabila noastră colectoare
print(numbers_sum)
```

În exemplul de mai sus, iterăm prin lista de numere și adăugăm fiecare număr la variabila `numbers_sum`.

## Interval (range)

Uneori, poate doriți să iterați de un anumit număr de ori fără a avea o listă specifică pentru a itera. Aici intervine funcția **range()**.

Funcția **range()** creează o secvență de numere pe baza parametrilor furnizați. Iată un exemplu care afișează numerele de la 0 la 4:

```python
for a in range(5):
    print(a)
# Output:
# 0
# 1
# 2
# 3
# 4
```

Funcția **range()** generează valori unul după altul.

Puteți personaliza funcția **range()** în mai multe moduri. De exemplu, puteți specifica punctul de plecare și punctul final al intervalului:

```python
for a in range(1, 6):
    print(a)
# Output:
# 1
# 2
# 3
# 4
# 5
```

În exemplul de mai sus, intervalul începe de la 1 și se termină la 6 (exclusiv).

De asemenea, puteți furniza o valoare de pas pentru a controla incrementarea dintre fiecare iterație. Pasul implicit este 1, dar îl puteți personaliza. De exemplu:

```python
for a in range(0, 10, 2):
    print(a)
# Output:
# 0
# 2
# 4
# 6
# 

8
```

În exemplul de mai sus, intervalul începe de la 0, se termină la 10 (neinclusiv 10) și crește cu 2.

### Intervaluri negative

Este posibil să iterați în jos către numere negative furnizând o valoare de pas negativă. Iată un exemplu:

```python
for a in range(0, -5, -1):
    print(a)
# Output:
# 0
# -1
# -2
# -3
# -4
```

### Iterarea unei liste folosind intervalul

Puteți utiliza funcția **range()** pentru a itera prin intermediul unei liste utilizând lungimea listei ca interval. Iată un exemplu:

```python
my_list = [6, 9, 4, 2, 0]
for a in range(len(my_list)):  # len(my_list) == 5
    print(f'Elementul la indexul {a} este {

my_list[a]}')
# Output:
# Elementul la indexul 0 este 6
# Elementul la indexul 1 este 9
# Elementul la indexul 2 este 4
# Elementul la indexul 3 este 2
# Elementul la indexul 4 este 0
```

În exemplul de mai sus, utilizăm funcția **range()** cu lungimea listei. Fiecare iterație a intervalului corespunde poziției indexului elementului din listă.

Această abordare poate fi îmbunătățită pentru a lucra în același timp cu două liste, de exemplu:

```python
list_1 = ['a', 'b', 'c']
list_2 = [97, 98, 99]
for index in range(len(list_1)):
    print(f'Litera {list_1[index]} are poziția {list_2[index]} în ASCII.')
```

Exemplul de mai sus efectuează operații pe ambele liste utilizând indexi în loc să lucreze direct cu colecțiile.

### Când este util intervalul (range)?

Funcția **range()** este utilă în următoarele scenarii:

1. Când doriți să efectuați o sarcină de un număr finit de ori.
2. Când doriți să accesați indexul unui element în timpul iterației.
3. Când doriți să cunoașteți numărul de iterații.

### Ce putem face în interiorul unei iterații (bucle **for**)?

În interiorul unei iterații, puteți face orice doriți. Iată câteva exemple:

1. Solicitarea de intrare de la utilizator:

```python
my_list = [2, 3, 4]
for a in my_list:
    print(f'Procesez {a}')
    b = int(input('Introduceți un număr: '))
    print(f'{a} * {b} = {a * b}')
```

2. Iterație în bucle imbricate:

```python
first_list = [10, 20, 30]
second_list = [90, 80, 70]
for a in first_list:
    for b in second_list:
        print(f'{a} * {b} = {a * b}')
```

3. Popularea unei alte liste:

```python
number_list = [2, 3, 4, 5]
power_two_list = []
for number in number_list:
    power_two_list.append(number ** 2)  # ridicat la puterea a doua
print(power_two_list)  # Output: [4, 9, 16, 25]
```

4. Procesare condițională:

```python
number_list = [23, 39, 48, 100]
numbers_under_50 = []
numbers_above_50 = []
for number in number_list:
    if number < 50:
        numbers_under_50.append(number)
    else:
        numbers_above_50.append(number)
```

În exemplul de mai sus, iterăm printr-o listă de numere și le separăm în două liste în funcție de o condiție.

În plus, puteți utiliza funcția `enumerate()` pentru a obține atât indexul, cât și valoarea fiecărui element în timpul iterației. Iată un exemplu:

```python
my_list = ['măr', 'banană', 'portocală']
for index, fruit in enumerate(my_list):
    print(f'Index: {index}, Fruct: {fruit}')
```

Funcția `enumerate()` returnează un iterator care furnizează perechi de index și valoare pentru fiecare element din lista. Acest lucru poate fi util atunci când aveți nevoie atât de indexul, cât și de valoarea în timpul iterației printr-o colecție.

## Mutabilitate vs Imutabilitate

În Python, conceptele de imutabilitate și mutabilitate se referă la posibilitatea de a modifica un obiect după ce a fost creat. Obiectele imutabile nu pot fi modificate odată ce au fost create, în timp ce obiectele mutable pot fi modificate.

Să discutăm despre imutabilitate și mutabilitate folosind două tipuri de date des utilizate în Python: șiruri de caractere (strings) și liste (lists).

1. Șiruri de caractere (Imutabile):
Șirurile de caractere în Python sunt obiecte imutabile. Aceasta înseamnă că odată ce un șir de caractere este creat, conținutul său nu poate fi modificat. Dacă doriți să modificați un șir de caractere, trebuie să creați un șir nou.

De exemplu:

```python
str1 = "Salut"
str2 = str1  # str2 face referire la același șir ca și str1

str1 += " Lume"
print(str1)  # Output: Salut Lume
print(str2)  # Output: Salut
```

În exemplul de mai sus, atunci când modificăm `str1` prin concatenarea " Lume" la el, se creează un șir nou cu conținutul modificat. Cu toate acestea, `str2` face în continuare referire la șirul original "Salut" și rămâne nemodificat. Această comportare demonstrează imutabilitatea șirurilor de caractere.

2. Liste (Mutabile):
Listele în Python sunt obiecte mutabile. Aceasta înseamnă că odată ce o listă este creată, elementele sale pot fi modificate, adăugate sau eliminate fără a crea o listă nouă.

De exemplu:

```python
list1 = [1, 2, 3]
list2 = list1  # list2 face referire la aceeași listă ca și list1

list1.append(4)
print(list1)  # Output: [1, 2, 3, 4]
print(list2)  # Output: [1, 2, 3, 4]
```

În exemplul de mai sus, modificăm `list1` prin adăugarea valorii 4 la el. Deoarece listele sunt mutabile, atât `list1`, cât și `list2` fac referire la aceeași listă și reflectă ambele modificări.

Distincția între mutabilitate și imutabilitate este crucială în Python. Obiectele imutabile asigură că valorile lor rămân constante, oferind beneficii precum comportamentul predictibil și posibilitatea unor optimizări. Pe de altă parte, obiectele mutabile permit mai multă flexibilitate și modificări dinamice.

Înțelegerea acestor concepte este importantă atunci când lucrați cu Python, deoarece ajută la prevenirea unui comportament neașteptat și permite utilizarea unor practici eficiente de programare.