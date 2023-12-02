Clasele și moștenirea

În ultima lecție, am învățat cum să creăm clase.

Astăzi, vom învăța cum să reutilizăm clasele și să creăm clase noi pornind de la clase vechi/existente.

Cum funcționează moștenirea

Moștenirea este procesul prin care o clasă preia proprietățile și metodele altei clase.

Acest lucru înseamnă că clasa care moștenește proprietățile (clasa copil) are acces la aceleași proprietăți ca și clasa de la care a moștenit (clasa părinte).

Moștenirea ne permite să reutilizăm și să construim pe baza obiectelor existente. Astfel, putem adăuga ușor funcționalități noi la obiecte existente fără a le modifica.

Clasele părinte și clasele copil sunt adesea numite clase de bază și clase derivate.

Exemplu

Să presupunem că avem o clasă Animal.

Clasa noastră animal are proprietăți precum nume, vârstă, specie, greutate.

Și are metode precum "mănâncă", "doarme".

Acum vrem să facem o clasă specifică pentru câini. Clasa Dog ar trebui să conțină toate proprietățile aceleași ca și clasa Animal, dar specia să fie setată automat la "câine" și să adăugăm metoda "latră".

Putem rezolva această problemă creând două clase separate și să avem proprietatea "specie" a clasei Dog să fie mereu 'câine'.

```python
class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f'{self.species} {self.name} mănâncă')

    def sleep(self):
        print(f'{self.species} {self.name} doarme')


class Dog:

    def __init__(self, name):
        self.name = name
        self.species = 'câine'

    def eat(self):
        print(f'{self.species} {self.name} mănâncă')

    def sleep(self):
        print(f'{self.species} {self.name} doarme')

    def bark(self):
        print(f'{self.species} {self.name} latră')
```

După cum poți vedea, acest proces este ineficient, mai ales când avem nevoie să adăugăm metode de obținere și setare. Deoarece va trebui să le copiem dintr-o clasă în alta, când sunt exact aceleași.

Folosirea moștenirii pentru a simplifica procesul

În programare, putem folosi "moștenirea" pentru a rezolva această situație. Putem face ca clasa Dog să moștenească toate proprietățile din clasa Animal.

Procesul de a moșteni o clasă se numește "extinderea" acelei clase.

Clasele părinte sunt declarate în interiorul parantezelor clasei copil.

```python
class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f'{self.species} {self.name} mănâncă')

    def sleep(self):
        print(f'{self.species} {self.name} doarme')


class Dog(Animal):  # Declarăm Animal ca fiind clasa părinte

    def __init__(self, name):
        self.name = name
        self.species = 'Câine'

    def bark(self):
        print(f'{self.species} {self.name} latră')


my_dog = Dog('Kuzea')
my_dog.eat()
# Câine Kuzea mănâncă
my_dog.sleep()
# Câine Kuzea doarme
my_dog.bark()
# Câine Kuzea latră
```

Nu avem nevoie să declarăm metodele .eat și .sleep pentru clasa Dog, deoarece clasa le-a moștenit automat din clasa Animal.

La ce avem acces

În interiorul claselor copil (derivate), avem acces la toate metodele și proprietățile claselor părinte (de bază).

Clasa Dog are acces atât la .eat și .sleep, dar și la .bark.

Clasele părinte au acces doar la proprietățile pe care le declară.

Clasa Animal are acces doar la metodele .eat și .sleep și nu poate accesa metoda .bark a clasei copilului său.

De exemplu, dacă avem o proprietate "rasă" în interiorul clasei Dog, clasa Animal nu are niciun mod de a accesa această proprietate.

Suprascrierea metodelor

Suprascrierea este procesul prin care implementăm o metodă a clasei părinte în interiorul clasei copil. Prin aceasta, "suprascriem" metoda părinte în clasa copil.

Suprascrierea se realizează declarând aceeași metodă ca și în clasa părinte.

```python
class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f'{self.species} {self.name} mănâncă')

    def sleep(self):
        print(f'{self.species} {self.name} doarme')


class Dog(Animal):  # Declarăm Animal ca fiind clasa părinte

    def __init__(self, name, breed):
        self.name = name
        self.species = 'Câine'
        self.breed = breed

    def eat(self):  # Suprascriem metoda eat a clasei Animal cu metoda noastră
        # Această metodă folosește rasa în locul speciei
        print(f'{self.breed} {self.name} mănâncă')

    def bark(self):
        print(f'{self.breed} {self.name} latră')
```

În exemplul de mai sus, am suprascris metoda .eat pentru clasa Dog. Această nouă metodă este disponibilă numai pentru clasa Dog. Metoda originală din clasa Animal rămâne neschimbată.

```python
animal = Animal('Patrick', 'ste

a')
animal.eat()
# stea Patrick mănâncă
dog = Dog('Tuzea', 'pudel')
dog.eat()
# pudel Tuzea mănâncă
```

Accesarea metodelor părinte

Uneori, dorim să adăugăm funcționalitate peste funcționalitatea existentă. Va fi, de asemenea, foarte ineficient să reimplementăm funcționalitatea clasei părinte pentru a o îmbunătăți.

De aceea, avem posibilitatea să accesăm metodele părinților noștri din metodele noastre ale copiilor.

Acest lucru se face utilizând funcția **super()**. Funcția super va returna instanța clasei părinte.

```python
class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        return f'{self.name} mănâncă'


class Dog(Animal):

    def __init__(self, name, breed):
        # Transmitem argumentele către funcția noastră init a clasei părinte în loc să
        # declarăm proprietățile aici
        super().__init__(name, 'câine')
        # Declarăm proprietățile suplimentare aici
        self.breed = breed

    def eat(self):
        # Returnăm valoarea din metoda noastră eat, folosind o altă metodă din clasa părinte
        return f"Câine " + super().eat()


my_dog = Dog('Kuzea', 'puddle')
print(my_dog.eat())
# Câine Kuzea mănâncă

my_animal = Animal('Kuzea', 'Câine')
print(my_animal.eat())
# Kuzea mănâncă
```

Dacă vrei un alt exemplu de lucru cu moștenire, să aruncăm o privire asupra acestuia.

```python
class Venit:

    def __init__(self, bani):
        self.bani = bani

    def valoare(self):
        return self.bani


class VenitCuTaxe(Venit):

    def __init__(self, bani, procent_taxe):
        super().__init__(bani)
        self.procent_taxe = procent_taxe

    def total_taxe(self):
        return super().valoare() * self.procent_taxe / 100

    def valoare(self):
        return super().valoare() - self.total_taxe()


print(Venit(1000).valoare())
# 1000
print(VenitCuTaxe(1000, 20).valoare())
# 800.0
```

Moștenire multiplă

În Python, putem moșteni din mai multe clase în același timp.

Când facem acest lucru, obiectul va moșteni toate proprietățile din ambele clase părinte.

Acest lucru introduce o mică problemă de care trebuie să fim conștienți. Doar una dintre proprietățile comune din ambele clase părinte va fi aplicată clasei noastre copil.

Haide să-ți arăt un exemplu.

```python
class Animal:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Animal {self.name}'


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(f'{self.name} latră')

    def __str__(self):
        return f'Câine {self.name}'


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        print(f'{self.name} miaună')

    def __str__(self):
        return f'Pisică {self.name}'


class CatDog(Cat, Dog):

    def __init__(self, name):
        super().__init__(name)


catdog = CatDog('Meowdog')
print(catdog)
# Pisică Meowdog - Metoda __str__ din clasa Cat a fost folosită.
catdog.meow()
# Meowdog miaună
catdog.bark()
# Meowdog latră
```

După cum poți vedea mai sus, putem folosi atât metodele din clasa Cat, cât și din clasa Dog în interiorul clasei CatDog. Dar metoda `__str__` este folosită doar dintr-una dintre clasele părinte.

Acest lucru se datorează faptului că Python are o anumită ordine pentru cum ar trebui apelate funcțiile.

Se numește Ordinea de Rezoluție Multiplă (MRO). MRO-ul este ceea ce decide care metode sunt utilizate în cazul în care mai mult de una dintre clasele din ierarhie au declarat aceeași metodă.

```python
print(CatDog.mro())
# [<class '__main__.CatDog'>, <class '__main__.Cat'>, <class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>]
```

Lista afișată mai sus arată ordinea în care Python va încerca să apeleze o metodă/proprietate.

Python va încerca să găsească proprietatea în ordinea din fiecare dintre clase și, dacă nu o găsește, va trece la următoarea clasă.

Cum putem specifica explicit care să fie utilizată?

Cu toate că nu ar trebui să o facem, putem face acest lucru într-un mod foarte ciudat.

Putem apela manual metoda în interiorul funcției noastre, ignorând moștenirea.

De exemplu:

```python
class Foo:
    def funct(self, arg):
        print(f'Foo {arg}')


class Bar:
    def funct(self, arg):
        print(f'Bar {arg}')


class FooBar(Foo, Bar):

    def funct_foo(self, arg):
        Foo.funct(self, arg)

    def funct_bar(self, arg):
        Bar.funct(self, arg)


foo_bar = FooBar()
foo_bar.funct_bar('Test')
# Bar Test
foo_bar.funct_foo('Test')
# Foo Test
print(FooBar.mro())
# [<class '__main__.FooBar'>, <class '__main__.Foo'>, <class '__main__.Bar'>, <class 'object'>]
foo

_bar.funct('Test')
# Foo Test
```

Verificarea părintelui unui obiect

Am descoperit **type** care ne permite să știm care este tipul direct al unui obiect. Cum putem afla dacă un obiect face parte dintr-o ierarhie?

Există 2 metode:

`isinstance` - Verifică dacă un obiect este o instanță a unei clase
`issubclass` - Verifică dacă o clasă este o clasă derivată a altei clase

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass


instanță_c = C()

print(isinstance(instanță_c, C))
# True
print(isinstance(instanță_c, B))
# True
print(isinstance(instanță_c, A))
# True

# Verifică dacă C este o clasă derivată a lui A
print(issubclass(C, A))
# True

# Verifică dacă A este o clasă derivată a lui C
print(issubclass(A, C))
# False

```

Cele mai bune practici pentru moștenire multiplă

Moștenirea multiplă nu este comună în multe limbi de programare, și acest lucru are o bună explicație. Așa cum am văzut mai sus, apar multe "întrebări" atunci când permiți unei clase să moștenească din mai multe locuri.

Cel mai bine este să nu folosești moștenire multiplă decât dacă ai nevoie cu adevărat de ea.

Când o folosești, este foarte important să fii conștient de proprietățile obiectelor tale și să eviți situațiile în care ambii părinți au în comun proprietăți sau metode. Deoarece acest lucru poate și va crea probleme.

Exemplu moștenire multiplă

Îți amintești de temele pe care le-am avut pentru lecția anterioară? Hai să le actualizăm pentru a folosi moștenirea.

Vom crea o clasă Pet (Animal de companie) și o clasă Human (Om), iar apoi vom crea clasele PetOwner (Stăpân de animale) și HumanWithPet (Om cu animal de companie).

```python
class Pet:

    def __init__(self, name, type, fav_food):
        self.name = name
        self.type = type
        self.fav_food = fav_food

    def __str__(self):
        return f"{self.type.capitalize()} numit {self.name} care îi place să mănânce {self.fav_food}"


class Human:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.get_full_name()}, vârsta {self.age}"


class PetOwner:

    def __init__(self, list_of_pets=None):
        self.list_of_pets = list_of_pets or []

    def adopt_pet(self, pet: Pet):
        self.list_of_pets.append(pet)

    def give_away_pet(self, pet: Pet):
        self.list_of_pets.remove(pet)


class HumanWithPet(Human, PetOwner):

    def __init__(self, first_name, last_name, age, initial_pets):
        super().__init__(first_name, last_name, age)
        PetOwner.__init__(self, initial_pets)

    def __str__(self):
        pet_count = len(self.list_of_pets)
        pet_string = "fără animale de companie."
        if pet_count > 1:
            pet_string = f"{pet_count} animale de companie:"
        elif pet_count == 1:
            pet_string = f"{pet_count} animal de companie:"
        pet_list = ", ".join([str(pet) for pet in self.list_of_pets])
        return f"{super().__str__()} are {pet_string} {pet_list}"


pet_1 = Pet('Garfield', "pisică", "lasagna")
pet_2 = Pet('Winnie', "urs", "miere")
human = HumanWithPet('Marius', 'Tricolici', 21, [pet_1, pet_2])
print(pet_1)
# Pisică numită Garfield care îi place să mănânce lasagna
print(pet_2)
# Urs numit Winnie care îi place să mănânce miere
print(human)
# Marius Tricolici, vârsta 21 are 2 animale de companie: Pisică numită Garfield care îi place să mănânce lasagna, Urs numit Winnie care îi place să mănânce miere
```