# Seturi și Tuple

## Tuplu

### Ce sunt tuplurile

În Python, un tuplu este o colecție ordonată de elemente, similară unei liste. Cu toate acestea, tuplurile sunt imutabile, ceea ce înseamnă că nu pot fi modificate după creare. Tuplurile sunt definite folosind paranteze `()` sau constructorul `tuple()`.

Iată un exemplu de creare a unui tuplu:

```python
my_tuple = (1, 2, 3)
```

Tuplurile pot conține elemente de diferite tipuri de date, cum ar fi numere, șiruri de caractere sau chiar alte tupluri.

### Tuplurile sunt imutabile

Spre deosebire de liste, tuplurile sunt imutabile, ceea ce înseamnă că elementele lor nu pot fi modificate după ce au fost atribuite. Această imutabilitate oferă anumite avantaje, cum ar fi garantarea integrității datelor și utilizarea tuplurilor pentru stocarea valorilor constante sau a datelor care nu ar trebui modificate.

```python
my_tuple = (1, 2, 3)
my_tuple[0] = 4  # Generează o eroare TypeError: 'tuple' object does not support item assignment
```

## Metode pentru tupluri

Tuplurile din Python oferă câteva metode încorporate pentru diverse operații:

- `count(element)`: Returnează numărul de apariții ale unui element specific în tuplu.
- `index(element)`: Returnează indexul primei apariții a unui element specific în tuplu.

```python
my_tuple = (1, 2, 2, 3, 3, 3)

count_2 = my_tuple.count(2)
print(count_2)  # Rezultat: 2

index_3 = my_tuple.index(3)
print(index_3)  # Rezultat: 3
```

## Operații cu tupluri (Comparație, Adunare și Înmulțire)

Tuplurile suportă mai multe operații, inclusiv comparația, adunarea și înmulțirea.

### Comparație

Tuplurile pot fi comparate folosind operatorii de comparație (`<`, `<=`, `>`, `>=`, `==`, `!=`) în funcție de valorile și ordinea elementelor lor.

```python
tuplu1 = (1, 2)
tuplu2 = (3, 4)

print(tuplu1 < tuplu2)  # Rezultat: True
print(tuplu1 == tuplu2)  # Rezultat: False
```

### Adunare

Tuplurile pot fi concatenate folosind operatorul `+`, creând un nou tuplu care combină elementele ambelor tupluri.

```python
tuplu1 = (1, 2)
tuplu2 = (3, 4)

tuplu3 = tuplu1 + tuplu2
print(tuplu3)  # Rezultat: (1, 2, 3, 4)
```

### Înmulțire

Tuplurile

 pot fi înmulțite cu un număr întreg pentru a crea un nou tuplu cu elemente repetitive.

```python
my_tuple = (1, 2)

nou_tuplu = my_tuple * 3
print(nou_tuplu)  # Rezultat: (1, 2, 1, 2, 1, 2)
```

## Segmentarea și indexarea tuplului

Similar listelor, tuplurile suportă indexarea și segmentarea pentru a accesa elemente specifice sau sub-șiruri.

```python
my_tuple = (1, 2, 3, 4, 5)

print(my_tuple[0])  # Rezultat: 1
print(my_tuple[1:4])  # Rezultat: (2, 3, 4)
print(my_tuple[-1])  # Rezultat: 5
```

Indexarea începe de la 0, unde primul element are indexul 0. Indicii negativi numără elementele de la sfârșitul tuplului.

# Seturi

## Ce este un set

Un set este o colecție neordonată de elemente unice în Python. Seturile sunt definite folosind acolade `{}` sau constructorul `set()`.

Iată un exemplu de creare a unui set:

```python
my_set = {1, 2, 3}
```

Seturile pot conține doar elemente unice, iar valorile duplicate sunt eliminate automat.

## Metode pentru seturi (adăugare și eliminare)

Seturile oferă diverse metode pentru adăugarea și eliminarea elementelor:

- `add(element)`: Adaugă un singur element în set.
- `update(iterabil)`: Adaugă mai multe elemente dintr-un obiect iterabil (cum ar fi o listă, tuplu) în set.
- `remove(element)`: Elimină un element specific din set. Generează o eroare KeyError dacă elementul nu este găsit.
- `discard(element)`: Elimină un element specific din set, dacă există. Nu generează eroare dacă elementul nu este găsit.

```python
my_set = {1, 2, 3}

my_set.add(4)
print(my_set)  # Rezultat: {1, 2, 3, 4}

my_set.remove(2)
print(my_set)  # Rezultat: {1, 3, 4}

my_set.discard(5)  # Nu se generează eroare dacă elementul nu există
```

## Metode pentru seturi (comparație)

Seturile din Python oferă metode de comparație pentru a verifica egalitatea, apartenența la submulțime și supramulțime:

- `issubset(other_set)`: Verifică dacă setul este o submulțime a `other_set`.
- `issuperset(other_set)`: Verifică dacă setul este o supramulțime a `other_set`.
- `isdisjoint(other_set)`: Verifică dacă setul nu are elemente comune cu `other_set`.

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {4, 5, 6

}

print(set1.issubset(set2))  # Rezultat: True
print(set2.issuperset(set1))  # Rezultat: True
print(set1.isdisjoint(set3))  # Rezultat: True
```

## Metode pentru seturi (uniune, diferență, intersecție)

Seturile din Python oferă metode suplimentare pentru a efectua operații de set, cum ar fi uniunea, diferența și intersecția.

- `union(other_set)`: Returnează un nou set care conține toate elementele din ambele seturi.
- `difference(other_set)`: Returnează un nou set cu elementele care sunt în primul set, dar nu sunt în al doilea set.
- `intersection(other_set)`: Returnează un nou set care conține elementele comune dintre cele două seturi.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set_uniune = set1.union(set2)
print(set_uniune)  # Rezultat: {1, 2, 3, 4, 5}

set_diferenta = set1.difference(set2)
print(set_diferenta)  # Rezultat: {1, 2}

set_intersectie = set1.intersection(set2)
print(set_intersectie)  # Rezultat: {3}
```

Aceste metode returnează seturi noi și nu modifică seturile originale.

## Metode pentru seturi (uniune_update, diferenta_update, intersectie_update)

Seturile din Python oferă, de asemenea, metode care actualizează setul însuși pe baza operațiilor cu seturi.

- `update(other_set)`: Actualizează setul cu elementele din alt set, realizând o uniune.
- `difference_update(other_set)`: Actualizează setul, eliminând elementele care sunt prezente în celălalt set.
- `intersection_update(other_set)`: Actualizează setul, păstrând doar elementele care sunt prezente și în celălalt set.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)
print(set1)  # Rezultat: {1, 2, 3, 4, 5}

set1.difference_update(set2)
print(set1)  # Rezultat: {1, 2}

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.intersection_update(set2)
print(set1)  # Rezultat: {3}
```

Aceste metode modifică setul în loc, actualizându-l cu elementele bazate pe operația cu seturi. Setul original se schimbă după aceste operații.

Înțelegerea acestor metode ale seturilor și a comportamentului lor este crucială pentru a lucra eficient cu seturi și pentru a efectua operații cu seturi în Python.

## Operatori pentru seturi

Seturile suportă diferite operații matematice pentru seturi folosind operatori:

- Uniune (`|`): Returnează un nou set care conține toate elementele din ambele seturi.
- Intersecție (`&`): Returnează un nou set care conține elementele comune între cele două seturi.
- Diferență (`-`): Returnează un nou set cu elementele din primul set, dar nu din al doilea set.
- Diferență simetrică (`^`): Returnează un nou set cu elementele care sunt într-unul dintre seturi, dar nu în ambele.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

intersection_set = set1 & set2
print(intersection_set)  # Output: {3}

difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}

symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
```

Seturile și tuplurile sunt structuri de date valoroase în Python, fiecare având caracteristici și metode distincte. Înțelegerea caracteristicilor și utilizării acestora poate îmbunătăți în mod semnificativ capacitățile de programare.

## Concluzie

Seturile și tuplurile sunt structuri de date valoroase în Python care oferă funcționalități și caracteristici distincte.

Tuplurile, fiind imutabile, oferă o modalitate fiabilă de a stoca și accesa date atunci când trebuie să vă asigurați integritatea acestora. Cu ajutorul metodelor tuplului și a operațiilor precum secționarea și indexarea, puteți manipula și extrage informații în mod eficient.

Seturile, pe de altă parte, oferă un instrument puternic pentru lucrul cu colecții de elemente unice. Acestea vă permit să efectuați operații de set, cum ar fi uniunea, diferența și intersecția, oferind flexibilitate în manipularea datelor. Metodele și operatorii pentru seturi îmbunătățesc în continuare funcționalitatea acestora, permițându-vă să actualizați seturile și să le comparați ușor.

Prin stăpânirea conceptelor și metodelor legate de seturi și tupluri, puteți extinde repertoriul de tehnici de manipulare a datelor în Python. Înțelegerea momentului și modului de utilizare a acestor structuri vă va permite să scrieți cod mai curat, mai eficient și să rezolvați o gamă mai largă de probleme.