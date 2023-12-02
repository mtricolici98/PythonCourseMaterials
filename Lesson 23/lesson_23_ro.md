# Proprietăți suplimentare ale claselor

Deoarece Python este un limbaj orientat pe obiecte, clasele oferă o mulțime de capabilități variate.

Clasele sunt foarte versatile și conțin o mulțime de funcționalități, majoritatea dintre ele putând fi suprascrise.

## Metode magice

Metodele magice sunt metode care încep cu un underscore și se termină cu un underscore. Metodele magice definesc multe dintre comportamentele unui obiect și modul în care interacționează cu alte obiecte.

Deja cunoaștem câteva dintre aceste metode magice, cum ar fi metodele `__init__` și `__str__`, de exemplu.

Prima ne permite să definim modul în care un obiect este inițializat, iar cealaltă ne ajută să reprezentăm obiectul nostru sub formă de șir.

Astăzi vom descoperi mai multe din ceea ce clasele au de oferit.

### Metode magice pentru comparații

Este posibil să suprascriem comportamentul unui obiect pentru comparații.

Hai să definim un obiect **Point**, care va reprezenta un punct într-un spațiu bidimensional. Punctul va avea două proprietăți: **x** și **y**.

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point at {self.x}:{self.y}'


p1 = Point(1, 2)
print(p1)
```

Pentru a defini comportamentul obiectului în timpul comparării, trebuie să suprascriem următoarele metode magice.

* `__eq__` - egal cu
* `__gt__` - mai mare decât
* `__lt__` - mai mic decât
* `__le__` - mai mic sau egal decât
* `__ge__` - mai mare sau egal decât

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point at {self.x}:{self.y}'

    def __eq__(self, other):
        if type(other) != Point:
            return False
        if other.x == self.x and other.y == self.y:
            return True
        return False

    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x:
            if self.y > other.y:
                return True
        return False

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            if self.y < other.y:
                return True
        return False

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other


p1 = Point(1, 2)
p2 = Point(2, 2)
p3 = Point(3, 1)
print(p1 == p2)
# False
print(p1 < p2)
# True
print(p1 > p2)
# False
print(p1 > p3)
# False
print(p1 < p3)
# True
print(p1 <= p3)
# True
print(p1 <= p1)
# True
```

Acum obiectul nostru suportă comparații folosind operatorii de comparații din Python.

## Mai multe metode magice

Cele două metode magice pe care le vom defini reprezintă ceea ce se întâmplă atunci când efectuăm operații aritmetice cu obiectele noastre.

* `__add__` - Adunare
* `__sub__` - Scădere

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point at {self.x}:{self.y}'

    def __add__(self, other):
        if type(other) is not Point:
            raise Exception('Adunarea este permisă numai pentru obiecte Point')
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if type(other) is not Point:
            raise Exception('Scăderea este permisă numai pentru obiecte Point')
        return Point(self.x - other.x, self.y - other.y)


p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)
# Point at 4:6
print(p1 - p2)
# Point at -2:-2
p1 += p1
print(p1)
# Point at 2:4
```

Alte operații aritmetice sunt disponibile, dar vă voi lăsa să experimentați singuri.

| Operator | Method     |
|----------|------------|
| +  | `__add__`      |
| -  | `__sub__`      |
| *  | `__mul__`      |
| /  | `__truediv__`  |
| // | `__floordiv__` |
| %  | `__mod__`      |
| ** | `__pow__`      |
| &  | `__and__`      |
| \ | `__or__`       |

## Mai multe metode magice

Există o mulțime de metode magice. Vă voi prezenta încă două. Celelalte **descoperiți singuri ce fac**.

V-ați gândit vreodată ce se întâmplă atunci când se accesează o proprietate a obiectului folosind paranteze pătrate?

Exemplu:

```python
print(p1['x'])
print(p1['y'])
# Sau
p1['x'] = 2
p1['y'] = 2
```

Putem suprascrie codul care face acest lucru, pentru a schimba ceea ce face clasa noastră atunci când dorim să facem acest lucru.

Pentru a face acest lucru, trebuie să suprascriem următoarele metode magice:

* `__setitem__` - setează elementul folosind paranteze pătrate
* `__getitem__` - obține elementul folosind paranteze pătrate



```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point at {self.x}:{self.y}'

    def __setitem__(self, key, value):
        if key == 'x' or key == 0:
            self.x = value
        elif key == 'y' or key == 1:
            self.y = value
        else:
            raise Exception(f'Încercare de a seta o proprietate a obiectului Point care nu este disponibilă: {key}')

    def __getitem__(self, item):
        if item == 'x' or item == 0:
            return self.x
        if item == 'y' or item == 1:
            return self.y
        raise Exception(f'Încercare de a accesa un element al obiectului Point care nu este disponibil: {item}')


p1 = Point(1, 2)
print(p1['x'])
# 1
print(p1['y'])
# 2
p1['x'] = 2
p1['y'] = 3
print(p1['x'])
# 2
print(p1['y'])
# 3
print(p1.x)
# 2
print(p1.y)
# 3
```

Putem interzice și accesul sau modificarea proprietăților noastre suprascriind metodele `__setattr__` și `__getattr__`.

Aceasta nu este recomandată, deoarece va interzice accesul la proprietățile tale chiar și în interiorul obiectelor.

Uitați-vă la exemplul de mai jos.

```python
class ImmutablePoint:
    _locked = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._locked = True

    def __str__(self):
        return f'Point at {self.x}:{self.y}'

    def __setattr__(self, key, value):
        if self._locked:
            raise Exception(f'Obiectul este imutabil, modificările nu sunt permise')
        super().__setattr__(key, value)


p1 = ImmutablePoint(1, 2)
print(p1.x)
# 2
print(p1.y)
# 3
p1.x = 1
p1.y = 1
# Exception: Obiectul este imutabil, modificările nu sunt permise
```

Folosim proprietatea _locked pentru a "bloca" obiectul împotriva modificărilor ulterioare.

Fiți atenți, deoarece trebuie să-l blocați după ce ați setat valorile inițiale. Dacă îl blocați înainte, chiar și funcția `__init__` nu va putea seta atributele acestui obiect.

## Decoratori

Decoratorii sunt funcții care înfășoară o funcție existentă.

[Puteți citi mai multe despre decoratori aici](https://www.datacamp.com/community/tutorials/decorators-python)

Vom discuta și despre decoratori într-o lecție viitoare.

Un decorator este un design pattern în Python care permite unui utilizator să adauge o nouă funcționalitate unui obiect existent, fără a modifica structura acestuia. Decoratorii sunt, de obicei, apelați înaintea definiției unei funcții pe care doriți să o decorați.

Decoratorii sunt aplicați folosind simbolul @.

Python oferă câțiva decoratori încorporați pe care îi putem folosi pentru a modifica comportamentul obiectelor noastre.

### classmethod și staticmethod

Ambele **classmethod** și **staticmethod** sunt metode pe care le putem declara în interiorul clasei și putem accesa la ele din afara clasei fără a avea nevoie de o instanță a obiectului.

Aceasta înseamnă că putem accesa aceste metode direct din clasa și nu avem acces la instanța obiectului (self).

Diferența dintre un **classmethod** și un **staticmethod** este că un **classmethod** are acces la clasa, în timp ce un **staticmethod** nu are.

```python
class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


string_date = '4-3-2022'
is_valid = Date.is_date_valid(string_date)  # Metoda staticmethod folosește clasa ca modul.
print(is_valid)
# True
date = Date.from_string(string_date)  # Metoda classmethod adaugă funcționalitate suplimentară clasei în sine.
print(date)
# <__main__.Date object at 0x0000021F9EFCFD88>
```

### property

Decoratorii de proprietăți ne permit să avem metode cu logici personalizate pentru a accesa proprietățile individuale ale obiectelor noastre.

```python
class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @property
    def full_date(self):
        return f"{self.day}-{self.month}-{self.year}"


my_date = Date(4, 3, 2022)
print(my_date.full_date)  # Accesăm full_date fără paranteze
# 4-3-2022
```

Proprietățile ne permit să definim un acces

 ușor la anumite atribute ale obiectelor noastre și să avem logica în interiorul proprietăților.

Decoratorul **property** înlocuiește **full_date**, transformându-l dintr-o metodă într-o proprietate a obiectului.

De asemenea, putem suprascrie comportamentul proprietății noastre definind funcțiile setter pentru proprietățile noastre.

```python
class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @property
    def full_date(self):
        return f"{self.day}-{self.month}-{self.year}"

    @full_date.setter
    def full_date(self, value):
        if Date.is_date_valid(value):
            self.day, self.month, self.year = map(int, value.split('-'))
        else:
            raise Exception('Data invalidă')

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


my_date = Date(4, 3, 2022)
print(my_date.full_date)
# 4-3-2022
my_date.full_date = '5-4-2022'  # Folosim setter-ul pentru full_date pentru a seta valoarea
print(my_date.full_date)
# 5-4-2022
print(my_date.day)
# 5
print(my_date.month)
# 4
print(my_date.year)
# 2022
```

## dataclass decorator

Uneori, este nevoie să creăm o clasă simplă care este folosită doar pentru a reprezenta date, fără funcționalități suplimentare.

Decoratorul dataclass ne permite să facem asta rapid.

Decoratorul dataclass este disponibil începând cu Python 3.9 și ne permite să creăm rapid clase pentru a reprezenta date.

Pentru a declara o dataclass, trebuie să definim o clasă simplă, în care definim proprietățile cu tipurile lor și să aplicăm decoratorul @dataclass pentru acea clasă.

Decoratorul dataclass va crea automat metodele `__init__` și `__str__` necesare.

```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    gender: str


a = Person('Marius', 12, 'M')
print(a)
# Person(name='Marius', age=12, gender='M')
```

Avem în continuare libertatea de a adăuga propriile noastre metode și de a suprascrie cele existente. Dar dataclass creează atributele minime necesare ale obiectelor noastre pentru a lucra cu ele în mod facil.

```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    gender: str

    def is_male(self):
        return self.gender.lower().startswith('m')

    def __str__(self):
        return f'{self.name} age {self.age} gender {self.gender}'


a = Person('Marius', 12, 'M')
print(a)
# Person(name='Marius', age=12, gender='M')
print(a.is_male())
# True
```

## Manageri de context

Managerii de context sunt o modalitate pentru dvs. de a declara o încapsulare în jurul unui bloc funcțional de cod.

Funcția managerului de context este de a prelua responsabilitatea de gestionare a resurselor de la programator și de a o muta pe managerul de context.

Managerii de context sunt accesați folosind declarația `with`.

Un exemplu de resursă care poate fi gestionată este fișierul (folosind funcția open).

```python
with open('example.txt', 'w+') as file:
    file.write("Tadaaa")
```

Managerul de context furnizat de funcția open va închide automat fișierul când codul din interiorul său este executat, adică după ce Python a ieșit din blocul managerului de context.

Aveți deja cunoștințele despre lucrul cu resurse externe (adică fișiere). Fișierele trebuie întotdeauna închise după ce ați terminat cu ele.

Ceea ce face managerul `open` este să deschidă fișierul pentru dvs., să transmită referința fișierului către dvs. (folosind cuvântul cheie as) și apoi să închidă fișierul când execuția dvs. a ieșit din blocul managerului de context.

Principiul de bază al unui manager de context este că face ceva înainte ca codul dvs. să fie executat, iar apoi poate face ceva după ce codul dvs. din interiorul managerului de context s-a oprit.

### Crearea propriilor noștri manageri de context

S-ar putea să aveți nevoie să creați un manager de context, nu vă faceți griji, este foarte ușor.

Să luăm un exemplu simplu. Doriți un manager de context care să calculeze timpul de executare a codului dvs.

Trebuie doar să definești metodele magice `__enter__` și `__exit__` pentru o clasă.

```python
import time


class benchmark_execution:

    def __init__(self):
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        time_ran = end_time - self.start_time
        print(f'Codul a fost executat timp de {time_ran} secunde')
        return True


with benchmark_execution():
    sum = 0
    for a in range(10000):
        for b in range(10000):
            sum += a + b
    print(sum)
# 999900000000
# Codul a fost executat timp de 10.640141725540161 secunde
```

Metoda exit ne permite, de asemenea, să gestionăm excepțiile care au apărut în interiorul corpului codului nostru.

Metoda exit trebuie să returneze True sau False în funcție de faptul dacă excepția (dacă există) a fost gestionată sau nu.

Dacă metoda exit returnează True, nu va opri execuția codului (excepția

 a fost gestionată), dacă returnează False, va opri execuția și va genera excepția normal.

Putem suprascrie și metoda `__init__` pentru a avea mai multe date pe care să le folosim în cadrul managerului nostru de context.

## Summary

În această lecție, am explorat proprietățile suplimentare ale claselor în Python:

* Metode magice pentru comparații: `__eq__`, `__gt__`, `__lt__`, `__le__`, `__ge__`
* Metode magice pentru operații aritmetice: `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`, `__and__`, `__or__`
* Alte metode magice: `__setitem__`, `__getitem__`, `__setattr__`, `__getattr__`
* Decoratori pentru metodele claselor: `classmethod`, `staticmethod`, `property`
* Decoratorul `dataclass` pentru crearea rapidă a claselor de date
* Manageri de context cu operatorul `with`

Toate aceste funcționalități ne permit să gestionăm mai bine comportamentul claselor noastre, să le facem mai ușor de utilizat și să adăugăm funcționalități suplimentare în mod flexibil.