# Obiecte

Data trecută am discutat despre funcția **type**.

Funcția **type** ne permite să returnăm clasa unui obiect.

Astăzi vom învăța cum să creăm propriile noastre clase și, la rândul lor, cum să creăm propriile noastre obiecte.

Python este un limbaj orientat pe obiect. În Python, totul este un obiect.

Să începem cu ceea ce înseamnă un obiect:

## Ce sunt obiectele?

Un obiect este un tip de date definit ca având atât **stare** cât și **comportament**.

Programarea orientată pe obiect ne permite (programatorilor) să creăm entități care reflectă reprezentări abstracte ale entităților din viața reală sau imaginate în interiorul codului nostru.

Să începem prin definirea proprietăților unui obiect: stare și comportament.

## Stare

Starea este proprietatea unui obiect de a stoca informații care "aparțin" acelui obiect.

Să luăm un exemplu de obiect.

### Un automobil

Mașinile sunt obiecte complexe, o mașină poate fi diferită de alta prin combinația de proprietăți.

O mașină poate fi, de asemenea, compusă din alte obiecte (ferestre, uși, roți etc.)

Mașinile au, de asemenea, proprietăți precum culoare, lungime, număr de roți, număr de uși, număr de ferestre etc.

De asemenea, o mașină poate avea o stare, de exemplu: în mișcare, în funcțiune, oprită, staționată, parcată.

Toate exemplele enumerate mai sus definesc **starea** obiectului care este o mașină.

### Șir (String)

Să ne uităm la un obiect pe care îl cunoaștem deja.

Șirul, după cum știm, este un obiect care conține o listă de caractere. Șirul are, de asemenea, proprietăți precum lungimea. Care se aplică în mod specific acestuia.

Împreună, conținutul și lungimea reprezintă acest șir.

## Comportament

Comportamentul definește ce poți face cu acel obiect. Comportamentele sunt "trăsături" ale acelui obiect care modifică starea sa internă sau folosesc starea sa internă pentru a genera rezultate noi.

Vedem aceasta în multe feluri în Python.

Comportamentul unui obiect este definit de "metodele" pe care le putem aplica acestor obiecte.

Am mai practicat deja folosirea metodelor pe obiecte. Un obiect de tip **list**, de exemplu, și-a putut schimba starea cu ajutorul metodelor precum **.append()**, **.extend()**, **.sort()** etc.

## Metode vs Funcții

În săptămânile anterioare, am lucrat atât cu metode, cât și cu funcții. Dar nu am învățat niciodată care este diferența dintre o metodă și o funcție.

### Funcții

Funcțiile sunt fragmente de programe pe care le putem folosi pentru a procesa informații, a modifica și a efectua operații cu argumentele funcțiilor noastre și, eventual, a returna unele rezultate.

Funcțiile lucrează numai cu date furnizate de argumentele lor sau date din alte variabile din afara domeniului lor (de exemplu, o variabilă globală sau valori importate din alte fișiere).

Exemple de funcții: **print()**, **input()**, **sum()**, **max()**

### Metode

Metodele sunt, de asemenea, funcții, dar metodele au acces la starea internă a obiectului, ceea ce înseamnă că pot procesa informații din interiorul obiectului la care aparține metoda.

O metodă face întotdeauna parte dintr-un obiect și poate fi accesată numai folosind obiectul respectiv.

Exemple de metode sunt **my_list.append()**, **my_string.replace()**, **my_string.count()**.

Unele metode pot modifica pur și simplu valoarea internă a obiectului, altele pot returna rezultate, altele pot face ambele lucruri (de exemplu, **list.pop()**).

Metodele sunt întotdeauna apelate în legătură cu un obiect, folosind **.** (punct) pentru a se conecta la acel obiect.

````python
my_list = []
my_list.append('element')  # Modifică starea lui my_list.
my_list.count('element')  # Verifică numărul de apariții în starea internă a listei.
````

Vom învăța mai târziu cum putem defini metode.

# Clase

În programare, clasele sunt ceea ce numim "scheme" pentru obiectele noastre. Clasele conțin declarația privind ce proprietăți poate avea un obiect și ce metode poate avea un obiect.

Obiectele sunt create din clase folosind funcția constructor. Apelarea unei clase folosind parantezele va executa funcția constructor. Funcția constructor este ceea ce creează instanța obiectului. Ea "construiește" obiectul din "schema" care este clasa.

```python
my_list = list()  # Apelarea constructorului clasei list
```

# Definirea claselor

Cum putem crea propriile noastre clase (și, în cele din urmă, obiecte) în Python?

Deja am creat propriile noastre obiecte acum ceva timp, atunci când am discutat despre excepțiile personalizate. Excepțiile sunt, de asemenea, obiecte.

Definirea obiectelor este foarte simplă.

Trebuie să folosim cuvântul cheie **class** pentru a defini un nou tip.

```python
class MyNewClass:  # Crearea unei noi clase cu numele

 MyNewClass
    pass
```

Acum, putem crea instanțe ale acestui nou tip, acele **instanțe** sunt obiectele noastre.

Hai să creăm un obiect Animal.

````python
class Animal:
    pass


my_animal = Animal()  # Crearea unei instanțe a tipului Animal
````

Ce putem face acum cu acest animal?

Pentru a răspunde direct, sincer, nimic. Clasa noastră de animal nu are o stare definită și nici un comportament definit.

Hai să adăugăm câteva proprietăți la animalul nostru.

## Adăugarea proprietăților

Să începem prin a adăuga numele animalului nostru.

Inițializăm aceasta cu None, deoarece, atunci când creăm un animal, vrem să nu aibă nume la început.

````python
class Animal:
    name = None  # Toate animalele încep fără nume
````

Acum putem accesa această proprietate și o putem modifica în interiorul obiectului animal atunci când îl creăm.

```python
class Animal:
    name = None  # Toate animalele încep fără nume


animal_object = Animal()
print(animal_object.name)  # Va fi None, deoarece toate obiectele Animal au o valoare inițială pentru nume de None
# None
animal_object.name = 'Kuzea'  # Modificăm valoarea internă a numărului din animal
print(animal_object.name)  # Noua valoare se află în interiorul noului nostru obiect animal.
# Kuzea
```

## Adăugarea metodelor

Metodele sunt adăugate la o clasă folosind aceeași sintaxă **def**. Singura diferență dintre declararea funcțiilor și metodelor este că primul argument al unei metode este **self** (instanța obiectului pe care se apelează metoda).

**self** este întotdeauna prezent în metodele obiectului și reprezintă obiectul în sine. Când apelăm metodele, nu transmitem argumentul **self**, deoarece Python o face în locul nostru.

```python
class Animal:
    name = None

    def set_name(self, name):
        """Metodă care setează numele unei instanțe a unui obiect de tip animal."""
        self.name = name
```

Putem apela metoda nou creată la fel cum apelăm întotdeauna metodele.

```python
class Animal:
    name = None

    def set_name(self, name):
        """Metodă care setează numele unei instanțe a unui obiect de tip animal."""
        self.name = name


new_animal = Animal()
new_animal.set_name('Kuzea')
print(new_animal.name)  # Afișează valoarea modificată a numelui animalelor noastre
# Kuzea
```

Putem adăuga mai multe metode la această clasă pentru a o face mai completă.

```python
class Animal:
    name = None
    species = None

    def set_name(self, name):
        """Setează numele animalului"""
        self.name = name

    def get_name(self):
        """Returnează numele animalului"""
        return self.name

    def set_species(self, species):
        """Setează numele speciei"""
        self.species = species

    def get_species(self):
        """Returnează numele speciei"""
        return self.species

    def is_species(self, other_species):
        return self.species == other_species
```

Testăm noua noastră clasă de Animal

```python
class Animal:
    name = None
    species = None

    def set_name(self, name):
        """Setează numele animalului"""
        self.name = name

    def get_name(self):
        """Returnează numele animalului"""
        return self.name

    def set_species(self, species):
        """Setează numele speciei"""
        self.species = species

    def get_species(self):
        """Returnează numele speciei"""
        return self.species

    def is_species(self, other_species):
        return self.species == other_species


animal_1 = Animal()
animal_1.set_name('Kuzea')
animal_1.set_species('Câine')

animal_2 = Animal()
animal_2.set_name('Tuzea')
animal_2.set_species('Câine')

animal_3 = Animal()
animal_3.set_name('Kiskis')
animal_3.set_species('pisică')

print(animal_1.get_name(), animal_1.get_species())
# Kuzea Câine
print(animal_2.get_name(), animal_2.get_species())
# Tuzea Câine
print(animal_3.get_name(), animal_3.get_species())
# Kiskis Pisică

print(animal_1.is_species(animal_2.get_species()))
# True
print(animal_2.is_species(animal_3.get_species()))
# False (Câine != Pisică)
```

Acum s-ar putea să aveți o întrebare: dacă pot accesa direct proprietățile acestui obiect, de ce trebuie să folosesc metode?

### De ce să folosim metode

Accesarea proprietăților în interiorul unui obiect este întotdeauna posibilă în Python, dar ca programator ați putea dori să aveți logici suplimentare în metodele dvs. pentru a efectua anumite verificări sau validări.

```python
class Animal:
    name = None
    species = None

    def set_species(self, species):
        if self.species is not None:  # Nu permitem schimbarea speciei animalului nostru
            raise Exception('Nu se poate schimba specia unui animal după ce a fost atribuită')
        if type(species) != str:  # Nu permitem să setăm specia la altceva decât șiruri
            raise Exception('Specia trebuie să fie un șir')
        self.species = species  # Nu am eșuat mai sus, deci putem seta specia noastră 

    def get_species(self):
        return self.species

    def set_name(self, name):
        if self.name is not None:
            raise Exception('Nu se poate seta numele, deoarece acest animal are deja un nume, folosiți metoda rename()')
        self.name = name

    def get_name(self):
        return self.name



    def rename(self, new_name):
        self.name = new_name


my_animal = Animal()
my_animal.set_name('Kuzea')
my_animal.set_species(123)  # Va genera eroare
my_animal.set_species('Câine')
my_animal.set_name('Tuzea')  # Va genera eroare
my_animal.set_species('pisică')  # Va genera eroare
my_animal.rename('Tuzea')  # Va funcționa
my_animal.species = 'pisică'
# Linia de mai sus va funcționa, dar nu e bine să facem asta,
# deoarece evităm verificările care ar fi trebuit să ne împiedice să facem asta.
```

## Crearea de obiecte cu valori inițiale (Funcții constructor)

Putem, de asemenea, să declarăm clase într-un mod în care obiectele ar trebui să aibă o valoare inițială, pentru aceasta, trebuie să implementăm funcția constructor (sau metoda de inițializare).

Pentru aceasta, trebuie să implementăm metoda `__init__` a Python (vezi mai jos).

```python
class Animal:

    def __init__(self):
        pass
```

Metoda `__init__` este ceea ce folosim pentru a "inițializa" obiectul. Și are acces la obiectul nostru.

````python
class Animal:
    name = None
    species = None

    def __init__(self, name, species):
        self.name = name
        self.species = species
````

Acum putem apela funcțiile noastre constructor într-un mod diferit, cu argumente pentru nume și specii

````python
class Animal:
    name = None
    species = None

    def __init__(self, name, species):
        self.name = name
        self.species = species


my_animal = Animal('Kuzea', 'Câine')
print(my_animal.species)
# Câine
print(my_animal.name)
# Kuzea
````

Putem avea, de asemenea, argumente implicite în declarația clasei noastre, de exemplu

```python
class Animal:
    name = None
    species = None

    def __init__(self, name, species=None):
        self.name = name
        if not species:
            print('Animal inițializat fără specie')
        self.species = species


my_animal = Animal('Kuzea')
```

Și putem face, de asemenea, verificări corecte dacă dorim, de asemenea, în interiorul clasei noastre.

Exemplul de mai jos creează un obiect animal

```python
class Animal:
    name = None
    species = None

    def __init__(self, name, species):
        self.set_name(name)
        self.set_species(species)

    def validate_name(self, name):
        if self.name is not None:
            raise Exception('Nu se poate seta numele, deoarece acest animal are deja un nume, folosiți metoda rename()')
        if not name:
            raise Exception('Numele trebuie să aibă o valoare')

    def validate_species(self, species):
        if self.species is not None:  # Nu permitem schimbarea speciei animalului nostru
            raise Exception('Nu se poate schimba specia unui animal după ce a fost atribuită')
        if type(species) != str:  # Nu permitem să setăm specia la altceva decât șiruri
            raise Exception('Specia trebuie să fie un șir')

    def set_species(self, species):
        self.validate_species(species)
        self.species = species  # Nu am eșuat mai sus, deci putem seta specia noastră 

    def get_species(self):
        return self.species

    def set_name(self, name):
        self.validate_name(name)
        self.name = name

    def get_name(self):
        return self.name

    def rename(self, new_name):
        self.name = new_name


my_animal = Animal(None, None)  # eroare
my_animal_2 = Animal('Kuzea', 'Câine')
```

## Reprezentări de șiruri ale unui obiect.

Dacă încercăm să tipărim unul dintre obiectele noastre personalizate, vom observa că ceva nu e în regulă. Acest lucru se datorează faptului că toate obiectele au o reprezentare "implicită" a lor în formă de șir, dar aceasta nu este întotdeauna "citibilă de către om".

Exemplu:

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


my_animal = Animal('Kuzea', 'Câine')
print(my_animal)
# <__main__.Animal object at 0x0000013EF782AEC8> 
```

Exemplul de mai sus arată că modul în care Python afișează acest obiect ca șir este cu unele informații generale despre obiect.

Putem schimba acest comportament prin implementarea metodei `__str__` a obiectului nostru.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f'Animal cu numele {self.name} și specia {self.species}'


my_animal = Animal('Kuzea', 'Câine')
print(my_animal)
# Animal cu numele Kuzea și specia Câine
```

Ce tocmai am făcut este să "suprascriem" reprezentarea sub formă de șir a acestui obiect. Vom învăța mai multe despre suprascrieri în următoarea lecție.

## O modalitate mai bună de a defini clase.

Acum că știm despre `__init__`, să vorbim despre importanța sa. `__init__` este (și ar trebui să fie) locul în care declarăm toate valorile specifice obiectului. Trebuie să facem acest lucru pentru a ne asigura că clasa noastră nu poate fi modificată din exterior.

```python
class ExampleBad:
    value_a = None  # Acestea sunt valori legate de clasă, care sunt de asemenea disponibile pentru obiect
    value_b = None


class ExampleGood:

    def __init__(self):


        self.value_a = None
        self.value_b = None
```

Aveți idee de ce ar fi prima implementare o idee mai slabă?

Răspunsul se datorează faptului că Python este un limbaj "dinamic" și valorile unei clase pot fi modificate după ce a fost definită clasa. Am văzut acest lucru în exemplul nostru cu obiectul Animal:

```python
my_animal = Animal('Kuzea', 'Câine')
my_animal.species = 'girafă'  # Funcționează, dar poate fi o problemă în proiectele mai mari
```

La fel de bine, putem schimba valorile noastre legate de clasă după definirea clasei.

```python
ExampleBad.value_a = 10
print(ExampleBad.value_a)
# 10
```

Prin implementarea lui `__init__` avem mai mult control asupra valorilor obiectelor noastre și asupra ceea ce se întâmplă atunci când acestea sunt inițializate.

Astfel, în general, este mai bine să folosim `__init__` în loc să definim valorile legate de clasă în mod direct. (Pentru referințe, valorile legate de clasă nu au întotdeauna aceleași valori pentru toate obiectele care sunt instanțe ale clasei.)

## În concluzie

În această lecție am învățat despre clase și obiecte în Python.

### Obiecte:

- Obiectele sunt instanțe ale claselor.
- Clasele sunt "scheme" pentru obiecte.
- Obiectele au stare și comportament.

### Clase:

- Clasele se definesc cu cuvântul cheie `class`.
- Clasele pot avea proprietăți (variabile) și metode (funcții) definite în interiorul lor.
- Metodele au întotdeauna primul argument `self`, care face referire la obiectul însuși pe care apelăm metoda.
- Metodele pot fi folosite pentru a accesa și modifica starea obiectului.
- Metoda `__init__` este constructorul nostru de obiecte și se apelează atunci când se creează o nouă instanță a clasei.
- Putem suprascrie metoda `__str__` pentru a obține o reprezentare mai ușor de citit a obiectelor noastre.

În următoarea lecție, vom învăța despre suprascrierea operațiilor și alte metode speciale ale clasei, precum și despre moștenire și abstracție.