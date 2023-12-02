# Primii pași în Python

## Exemplu de cod

```python
name = "Marius"
hello_string = "Salut " + name
print(hello_string)
```

În acest fragment de cod, începem prin atribuirea valorii "Marius" unei variabile numită `name`. Apoi, creăm o altă variabilă numită `hello_string`, care combină șirul de caractere "Salut " cu valoarea stocată în variabila `name`. Acest lucru se realizează folosind operatorul `+` pentru concatenare (unire) a celor două șiruri de caractere.

În final, folosim funcția `print()` pentru a afișa valoarea variabilei `hello_string` pe ecran. În acest caz, se va afișa "Salut Marius" deoarece valoarea lui `name` este "Marius". Deci, atunci când codul este executat, va afișa mesajul de salut "Salut Marius" în consolă.

## Ce sunt variabilele

Desigur! În programare, o variabilă este ca un recipient care stochează o valoare. Poți să o vezi ca pe o cutie etichetată în care poți pune diferite lucruri. Fiecare variabilă are un nume pe care îl alegi, și poți atribui o valoare la ea.

De exemplu, să presupunem că ai o variabilă numită `punctaj`. Poți folosi această variabilă pentru a stoca punctajul pe care l-ai obținut într-un joc. Inițial, variabila ar putea avea o valoare de 0. Pe măsură ce joci jocul și câștigi puncte, poți actualiza valoarea variabilei `punctaj` pentru a reflecta noul tău punctaj.

Variabilele sunt utile deoarece îți permit să stochezi și să manipulezi date în programul tău. Poți efectua operații pe variabile, cum ar fi adunarea lor sau modificarea valorilor lor în funcție de anumite condiții.

## Cum să declari variabile

În Python, poți declara o variabilă urmând aceste reguli:

1. Alege un nume pentru variabila ta: Numele ar trebui să fie semnificativ și să descrie scopul variabilei. Poate conține litere (atat majuscule, cât și minuscule), cifre și underscore (_), dar trebuie să înceapă cu o literă sau un underscore. Evită utilizarea de caractere speciale sau spații în numele variabilelor.

```python
first_name = 'valid'
FIRST_NAME = 'valid'
_firt_name_ = 'valid'
__first_name = 'valid'
$amount = 'not valid'
1_name = 'not valid'
v4r_name = 'valid dar nu recomandat'
```

2. Folosește operatorul de atribuire (=) pentru a atribui o valoare variabilei: După ce ai ales numele, poți folosi operatorul de atribuire pentru a atribui o valoare variabilei. Valoarea poate fi un număr, un șir de caractere, o valoare booleană (True sau False) sau orice alt tip de date.

Iată un exemplu care declară și atribuie valori variabilelor în Python:

```python
# Declararea și atribuirea valorilor variabilelor
name = "John"  # Atribuirea unei valori de tip șir de caractere
age = 25  # Atribuirea unei valori de tip întreg
is_student = True  # Atribuirea unei valori de tip boolean

# Afișarea valorilor variabilelor
print(name)
print(age)
print(is_student)
```

În exemplul de mai sus, declarăm trei variabile: `name`, `age` și `is_student`. Atribuim șirul de caractere "John" variabilei `name`, valoarea întreagă 25 variabilei `age` și valoarea booleană True variabilei `is_student`. În final, utilizăm funcția `print()` pentru a afișa valorile variabilelor pe ecran.

Ține minte că în Python, variabilele sunt cu tipare dinamică, ceea ce înseamnă că nu trebuie să declari în mod explicit tipul unei variabile. Tipul este dedus în funcție de valoarea atribuită acesteia.

## Ce sunt constantele

În Python, constantele sunt similare cu variabilele, dar valorile lor nu pot fi modificate după ce au fost atribuite. Ele sunt folosite pentru a reprezenta valori fixe care rămân constante pe parcursul programului.

Deși Python nu are suport încorporat pentru constante, dezvoltatorii folosesc adesea convenții de denumire pentru a indica faptul că valoarea unei variabile ar trebui tratată ca o constantă și să nu fie modificată. În mod convențional, numele constantelor sunt scrise în litere majuscule, cu underscore între cuvinte, pentru a îmbunătăți lizibilitatea.

Să luăm un exemplu pentru a defini o constantă pentru valoarea lui pi (π) în programul nostru. Putem atribui o valoare unei variabile numită `PI` și să o tratăm ca o constantă:

```python
PI = 3.14159
```

Odată ce valoarea este atribuită variabilei `PI`, nu ar trebui să fie modificată în altă parte a codului. În mod convențional, alți programatori care lucrează cu codul ar trebui să înțeleagă că `PI` este menit să fie tratată ca o constantă și să evite modificarea ei.

Este important de menționat că Python nu impune imutabilitatea variabilelor marcate ca fiind constante. Convenția de denumire servește ca un ghid pentru programatori pentru a indica faptul că valoarea nu ar trebui să fie modificată, dar este totuși posibil să se schimbe valoarea dacă este dorit. Prin urmare, este responsabilitatea dezvoltatorilor să urmeze bune practici și să trateze aceste variabile ca și constante, să nu le modifice valorile în timpul executării programului.

## Ce sunt funcțiile

Funcțiile permit încapsularea unor bucăți de cod reutilizabile și executarea lor ori de câte ori este necesar.
La apelul unei funcții, le spui Python-ului să execute codul din interiorul funcției.

Iată principalele aspecte de înțeles despre apelul funcțiilor în Python:

1. **Numele funcției**: Pentru a apela o funcție, trebuie să știi numele acesteia. Funcțiile în Python sunt, în mod obișnuit, definite cu un nume urmat de paranteze, ca de exemplu `nume_funcție()`. Numele funcției trebuie să se potrivească cu numele folosit la definiția funcției.

2. **Paranteze**: Parantezele `()` sunt esențiale la apelul unei funcții. Ele indică faptul că vrei să execuți funcția, nu doar să faci referire la numele ei. Chiar dacă funcția nu primește niciun argument, tot trebuie să incluzi parantezele.

3. **Argumente**: Funcțiile pot accepta valori de intrare numite argumente sau parametri. La apelul unei funcții, poți furniza valori pentru aceste argumente în interiorul parantezelor. De exemplu, dacă o funcție așteaptă un număr ca argument, vei trece numărul în paranteze când apelezi funcția, ca de exemplu `nume_funcție(5)`.

4. **Valoarea de returnare**: Funcțiile pot, de asemenea, să returneze o valoare ca rezultat al execuției lor. La apelul unei funcții care returnează o valoare, poți atribui rezultatul unei variabile sau îl poți folosi direct în codul tău. De exemplu, `rezultat = nume_funcție()` sau `print(nume_funcție())`.

5. **Execuția funcției**: Când o funcție este apelată, Python-ul execută codul din interiorul funcției. Sari la definiția funcției, rulează codul din blocul funcției și apoi te întorci în locul unde a fost apelată funcția.

6. **Apeluri de funcții îmbricate**: Funcțiile pot fi apelate din alte funcții. Acest lucru îți permite să construiești programe mai complexe prin dezmembrarea sarcinilor în funcții mai mici, ușor de gestionat, și apelându-le pe măsură ce este necesar.

## Functia print

Funcția `print()` în Python este folosită pentru a afișa mesaje sau rezultate pe consolă. Este una dintre cele mai simple și frecvent utilizate funcții în Python, în special în etapele de dezvoltare și depanare a programelor. Iată câteva aspecte importante despre funcția `print()`:

- **Afișarea unui mesaj simplu**: Cel mai simplu mod de utilizare a funcției `print()` este să furnizezi un șir de caractere între parantezele rotunde. Acest șir de caractere reprezintă mesajul pe care dorești să-l afișezi. De exemplu: `print("Salut, lume!")` va afișa "Salut, lume!" pe consolă.

- **Afișarea valorilor variabile**: Poți afișa valorile variabilelor în cadrul funcției `print()` prin intermediul concatenării sau prin formatarea șirurilor de caractere. De exemplu: 

```python
nume = "Alice"
varsta = "25"
print("Nume: " + nume + ", Varsta: " + varsta)
```

Aceasta va afișa "Nume: Alice, Varsta: 25" pe consolă.

- **Afișarea mai multor elemente**: Funcția `print()` poate primi mai multe argumente separate prin virgulă. Aceste argumente vor fi afișate în ordinea în care sunt specificate, separate prin spații. De exemplu: `print("Python", "este", "grozav!")` va afișa `"Python este grozav!"` pe consolă.

Funcția print va fi cel mai des utilizată funcție de voi, astfel e bine sa faci cunostință cu ea mai aprofundat, urmărind [acest link.](https://www.geeksforgeeks.org/python-print-function/)

## Ce sunt tipurile de date

În Python, tipurile de date se referă la clasificarea sau categoria datelor pe care o variabilă le poate stoca. Fiecare variabilă are un tip specific care determină tipul de date pe care îl poate stoca și operațiile care pot fi efectuate asupra sa. Să discutăm patru tipuri de date utilizate frecvent în Python: `str` (șir de caractere), `int` (număr întreg), `float` (număr în virgulă mobilă) și `bool` (valoare booleană).

1. **Șir de caractere (`str`)**: Un șir de caractere este o secvență de caractere închisă în ghilimele (`'` sau `"`). Este folosit pentru a reprezenta textul. De exemplu: `"Salut, lume!"` sau `'Programare în Python'`. Șirurile de caractere pot fi manipulate folosind diverse operații precum concatenarea (unirea), tăierea (extragerea de părți) și altele.

2. **Număr întreg (`int`)**: Un număr întreg reprezintă un număr întreg fără zecimale. De exemplu: `5`, `-10`, `0`. Numerele întregi sunt utilizate în calcule matematice și pot fi adunate, scăzute, înmulțite, împărțite etc.

3. **Număr real (`float`)**: Un număr în floating-point (virgulă mobilă) reprezintă un număr zecimal. Acesta conține un punct zecimal și poate avea părți fracționare. De exemplu: `3.14`, `1.5`, `-0.5`. Numerele în virgulă mobilă sunt utilizate în calcule care implică numere reale.

4. **Valoare booleană (`bool`)**: Un boolean reprezintă o valoare logică și poate avea fie valoarea `True`, fie valoarea `False`. Booleenii sunt adesea utilizați în declarații condiționale și comparații. De exemplu: `True` și `False`. Booleenii pot fi, de asemenea, rezultatul unor operații de comparație, cum ar fi `==` (egalitate), `>` (mai mare decât), `<` (mai mic decât), etc.

Iată un exemplu care demonstrează utilizarea acestor tipuri:

```python
name = "John"  # Șir de caractere
age = 25  # Număr întreg
height = 1.75  # Număr real
is_student = True  # Valoare booleană

print(name)
print(type(name)) # Ar trebui să fie str
print(age)
print(type(age)) # Ar trebui să fie int
print(height)
print(type(height)) # Ar trebui să fie float
print(is_student)
print(type(is_student)) # Ar trebui să fie bool
```

În acest exemplu, avem variabile cu diferite tipuri. `name` este un șir de caractere, `age` este un număr întreg, `height` este un număr real și `is_student` este o valoare booleană. Folosim funcția `print()` pentru a afișa valorile acestor variabile pe ecran.

## Tipare dinamice

Tipizarea dinamică este o caracteristică a limbajului Python care permite variabilelor să stocheze valori de orice tip, iar tipul unei variabile poate fi schimbat dinamic în timpul execuției unui program. În limbajele cu tipare dinamică, precum Python, nu este nevoie să declari explicit tipul unei variabile înainte de a-i atribui o valoare.

Iată cum funcționează tipizarea dinamică în Python:

1. Inferența tipului: Când atribui o valoare unei variabile, Python determină automat tipul în funcție de valoarea atribuită. De exemplu:

```python
x = 5  # x este un număr întreg (integer)
y = "Hello"  # y este un șir de caractere (string)
```

În acest exemplu, `x` este inferat ca fiind un număr întreg deoarece valoarea atribuită este un număr întreg, iar `y` este inferat ca fiind un șir de caractere deoarece valoarea atribuită este un șir de caractere.

2. Schimbare dinamică a tipului: Odată ce o variabilă primește o valoare, poți atribui ulterior o valoare de un alt tip aceleiași variabile fără probleme. Python îți permite să schimbi tipul unei variabile în timpul execuției. De exemplu:

```python
x = 5  # x este un număr întreg (integer)
x = "Hello"  # x este acum un șir de caractere (string)
```

În acest caz, `x` începe ca un număr întreg, dar tipul său devine un șir de caractere când i se atribuie o nouă valoare. Python gestionează conversia tipului automat.

```python
x = 5
y = "Hello"
rezultat = x + y  # Această operație va genera o eroare de tip (TypeError)
```

În acest exemplu, adunarea unui număr întreg (`x`) și a unui șir de caractere (`y`) va rezulta într-o eroare de tip (TypeError) deoarece aceste tipuri nu sunt compatibile pentru adunare. Python efectuează verificarea tipului în timpul execuției pentru a se asigura că operațiile sunt valide pentru tipurile implicate.

Tipizarea dinamică în Python oferă flexibilitate prin permiterea variabilelor să stocheze valori de diferite tipuri și prin facilitarea reatribuirii valorilor. Cu toate acestea, este important să ții evidența tipurilor de variabile și să fii atent la posibilele erori legate de tipuri care pot apărea dacă operațiile nu sunt compatibile cu tipul curent al unei variabile.

## Declararea șirurilor de caractere (str)

În Python, poți declara șiruri de caractere înconjurându-le fie cu ghilimele simple (`'`), fie cu ghilimele duble (`"`). Iată câteva exemple:

```python
# Declararea șirurilor de caractere folosind ghilimele simple
string1 = 'Salut, lume!'
string2 = 'Acesta este un șir de caractere.'

# Declararea șirurilor de caractere folosind ghilimele duble
string3 = "Programare în Python"
string4 = "Îmi place să codific!"

# Declararea șirurilor de caractere cu ghilimele în interior
string5 = "El a spus, 'Salut!'"
string6 = 'Ea a răspuns, "Bună ziua!"'
```

În exemplele de mai sus, `string1` și `string2` sunt declarate folosind ghilimele simple, în timp ce `string3` și `string4` sunt declarate folosind ghilimele duble. Ambele moduri sunt valide și poți alege pe care îl preferi.

Dacă ai nevoie să incluzi ghilimele în interiorul unui șir de caractere, poți folosi un tip de ghilimele pentru a înconjura întregul șir și celălalt tip de ghilimele în interiorul șirului. De exemplu, `string5` folosește ghilimele duble pentru a înconjura șirul și ghilimele simple în interior, iar `string6` face invers.

Python tratează șirurile de caractere în ghilimele simple și ghilimele duble în același mod. Poți efectua diverse operații pe șiruri de caractere, cum ar fi concatenare, extragerea unei părți din șir, calculul lungimii și altele. Șirurile de caractere sunt versatile și sunt frecvent utilizate pentru a stoca și manipula date bazate pe text în programele Python.

## Operații de bază cu șiruri de caractere - Concatenarea

În Python, poți efectua diverse operații pe șiruri de caractere pentru a le manipula și combina. Una dintre operațiile fundamentale cu șiruri de caractere este concatenarea, care îți permite să combini mai multe șiruri de caractere într-un singur șir. Iată cum funcționează concatenarea în Python:

Pentru a concatena șiruri de caractere, poți folosi operatorul `+`. Acesta adaugă pur și simplu două sau mai multe șiruri de caractere împreună. Iată un exemplu:

```python
string1 = "Salut"
string2 = "lume"
rezultat = string1 + string2
print(rezultat)
```

În exemplul de mai sus, variabilele `string1` și `string2` conțin șirurile "Salut" și "lume", respectiv. Folosind operatorul `+`, concatenăm aceste două șiruri și stocăm rezultatul în variabila `rezultat`. În cele din urmă, folosim funcția `print()` pentru a afișa șirul concatenat, care va produce rezultatul "Salutlume".

Poți, de asemenea, să concatenezi șiruri cu valori literale sau cu variabile. Iată un exemplu care demonstrează ambele cazuri:

```python
nume = "Alice"
salut = "Salut, " + nume + "!"
print(salut)
```

În acest exemplu, variabila `nume` conține șirul "Alice". Apoi, îl concatenăm cu șirurile "Salut, " și "!" pentru a crea mesajul de salut. Rezultatul este stocat în variabila `salut` și afișat folosind funcția `print()`. Output-ul va fi "Salut, Alice!".

În plus, poți concatena șiruri de caractere de mai multe ori folosind operatorul `*`. Acesta repetă de un număr specificat de ori șirul respectiv. Iată un exemplu:

```python
mesaj = "Salut! " * 3
print(mesaj)
```

În acest exemplu, șirul "Salut! " este repetat de trei ori folosind operatorul `*`. Șirul rezultat, "Salut! Salut! Salut!", este stocat în variabila `mesaj` și afișat.

Concatenarea îți permite să combini șiruri de caractere în diverse moduri, permițându-ți să creezi mesaje dinamice și personalizate în programele tale.

## Tipuri numerice

În Python, poți declara numere reale (floating-point) și numere întregi folosind simple instrucțiuni de atribuire. Iată cum poți să le declari:

1. **Numere reale (float)**:
   Pentru a declara un număr real, poți atribui direct o valoare zecimală unei variabile. De exemplu:

   ```python
   # Declara numere reale
   float_num1 = 3.14
   float_num2 = 2.5
   ```

   În exemplul de mai sus, `float_num1` și `float_num2` sunt variabile care stochează valori reale.

2. **Numere întregi (integer)**:
   Pentru a declara un număr întreg, poți atribui un număr întreg (fără zecimale) unei variabile. De exemplu:

   ```python
   # Declara numere întregi
   int_num1 = 10
   int_num2 = -5
   ```

   În exemplul de mai sus, `int_num1` și `int_num2` sunt variabile care stochează valori întregi.

Python determină automat tipul variabilei pe baza valorii atribuite acesteia. Deci, nu este nevoie să specifici explicit tipul, așa cum ai face în alte limbaje de programare.

Este important de menționat că poți efectua operații matematice atât pe numere reale, cât și pe numere întregi. Dacă efectuezi o operație între un număr întreg și un număr real, Python promovează automat numărul întreg la un număr real pentru a păstra partea zecimală în rezultat. De exemplu:

```python
x = 10  # număr întreg
y = 3.14  # număr real

rezultat = x + y  # Rezultatul va fi un număr real: 13.14
```

În exemplul de mai sus, chiar dacă `x` este un număr întreg și `y` este un număr real, operația de adunare promovează `x` la un număr real înainte de a-l aduna cu `y`.

## Operatiuni aritmetice in python

În Python, operațiile aritmetice de bază sunt efectuate folosind următorii operatori:

1. Adunare (+): Operatorul de adunare este reprezentat de simbolul plus (+). Este utilizat pentru a aduna două sau mai multe numere între ele. De exemplu:

   ```python
   a = 5
   b = 3
   rezultat = a + b  # Rezultatul este 8
   ```

2. Scădere (-): Operatorul de scădere este reprezentat de simbolul minus (-). Este utilizat pentru a scădea un număr din altul. De exemplu:

   ```python
   a = 5
   b = 3
   rezultat = a - b  # Rezultatul este 2
   ```

3. Înmulțire (*): Operatorul de înmulțire este reprezentat de simbolul asterisc (*). Este utilizat pentru a înmulți două sau mai multe numere. De exemplu:

   ```python
   a = 5
   b = 3
   rezultat = a * b  # Rezultatul este 15
   ```

4. Împărțire (/): Operatorul de împărțire este reprezentat de simbolul bară oblică (/). Este utilizat pentru a împărți un număr la altul. În mod implicit, împărțirea în Python returnează rezultatul sub formă de float. De exemplu:

   ```python
   a = 10
   b = 3
   rezultat = a / b  # Rezultatul este 3.3333333333333335
   ```

   Dacă doriți să efectuați împărțire între întregi și să obțineți câtul ca un întreg, puteți utiliza operatorul dublă bară oblică (//). De exemplu:

   ```python
   a = 10
   b = 3
   rezultat = a // b  # Rezultatul este 3
   ```

   În acest caz, partea zecimală a rezultatului împărțirii este trunchiată, iar doar câtul întreg este returnat.

Acestea sunt operațiile aritmetice de bază în Python. Ele vă permit să efectuați adunare, scădere, înmulțire și împărțire asupra valorilor numerice. În plus, Python oferă și alți operatori aritmetici, cum ar fi operatorul de modul (%) pentru obținerea restului împărțirii și operatorul de exponențiere (**) pentru ridicarea unui număr la o putere.


## Formatarea șirurilor de caractere în Python

Formatarea șirurilor de caractere în Python se referă la procesul de creare a șirurilor formatate prin încorporarea valorilor variabilelor, a expresiilor și a altor elemente într-un șir de caractere. Aceasta îți permite să creezi șiruri dinamice care pot fi personalizate în funcție de valorile variabilelor sau de alte informații. Python oferă două metode principale pentru formatarea șirurilor de caractere: f-strings (șiruri formatate) și metoda `.format()`.

1. **F-strings (șiruri formatate):**
   F-strings oferă o modalitate concisă și expresivă de a formata șirurile de caractere în Python. Au fost introduse în Python 3.6 și versiunile ulterioare. Cu ajutorul f-strings, poți îngloba expresii și variabile direct într-un șir de caractere prin prefixarea acestuia cu litera 'f' sau 'F'. Iată un exemplu:

   ```python
   name = "Alice"
   age = 25
   message = f"Numele meu este {name} și am {age} de ani."
   print(message)
   ```

   În acest exemplu, f-string-ul este definit prin prefixarea șirului cu 'f'. În interiorul acoladelor `{}`, poți include numele variabilelor sau expresiilor închise între acolade. Expresiile sunt evaluate în timpul execuției, iar valorile lor sunt inserate în șirul de caractere.

2. **Metoda `.format()`:**
   Metoda `.format()` este o modalitate versatilă și flexibilă de a formata șirurile de caractere în Python. Aceasta îți permite să specifici plasatoare într-un șir de caractere folosind acolade `{}` și să transmiți valori acestor plasatoare utilizând metoda `.format()`. Iată un exemplu:

   ```python
   name = "Alice"
   age = 25
   message = "Numele meu este {} și am {} de ani.".format(name, age)
   print(message)
   ```

   În acest exemplu, acoladele `{}` acționează ca plasatoare în șirul de caractere. Metoda `.format()` este apelată pe obiectul de tip șir de caractere și i se transmit valorile `name` și `age`. Aceste valori sunt apoi inserate în plasatoare în ordinea în care sunt transmise.

Atât f-strings, cât și metoda `.format()` oferă capacități puternice de formatare a șirurilor de caractere. Acestea îți permit să incluzi variabile, expresii și chiar să specifici opțiuni de formatare pentru valorile inserate. Alegerea între f-strings și metoda `.format()` depinde de preferințele personale și de versiunea Python pe care o utilizezi.

## None

În Python, `None` este o constantă specială care reprezintă absența unei valori sau lipsa unui obiect specific. Este adesea folosit pentru a indica faptul că o variabilă sau o expresie nu are o valoare semnificativă sau definită.

Iată câteva puncte cheie despre `None` în Python:

1. **Reprezentarea absenței**: `None` servește ca o marcă de poziție pentru a denota absența unei valori. Este folosit în mod obișnuit atunci când o variabilă sau o funcție nu returnează un rezultat specific sau când valoarea urmează să fie determinată.

2. **Inițializarea variabilelor**: `None` poate fi atribuit unei variabile ca valoare inițială atunci când doriți să indicați faptul că nu i-a fost atribuită încă o valoare specifică. Acest lucru este adesea făcut ca o marcă de poziție până când i se atribuie ulterior o valoare semnificativă.

Este important de menționat că `None` nu este același lucru cu un șir gol (`''`), zero (`0`) sau o valoare booleană precum `False`. Reprezintă în mod specific absența unei valori sau lipsa unui obiect specific în locul unei valori sau semnificații specifice.


## Funcția `input()` în Python

Funcția `input()` în Python este utilizată pentru a permite introducerea de la utilizator în timpul execuției unui program. Aceasta permite programului să se oprească și să aștepte ca utilizatorul să introducă un text sau o valoare de la tastatură. Iată o explicație de bază despre modul în care funcția `input()` funcționează:

Atunci când se apelează funcția `input()`, programul se va opri și va aștepta ca utilizatorul să introducă text. Funcția va afișa un prompt, care este șirul furnizat ca argument funcției `input()`. Utilizatorul poate apoi să tasteze intrarea lor și să apese tasta Enter.

Iată un exemplu care demonstrează utilizarea funcției `input()`:

```python
name = input("Introduceți numele dumneavoastră: ")
print("Salut, " + name + "! Bine ați venit în program.")
```

În acest exemplu, programul solicită utilizatorului să introducă numele lor prin afișarea mesajului "Introduceți numele dumneavoastră: ". Funcția `input()` este apelată cu acest mesaj ca argument. Când utilizatorul introduce numele lor și apasă Enter, programul trece la linia următoare.

Intrarea furnizată de utilizator este stocată în variabila `name`. Programul utilizează apoi numele introdus pentru a afișa un mesaj de salut personalizat utilizând concatenarea de șiruri. În cele din urmă, mesajul

 este tipărit utilizând funcția `print()`.

Este important de menționat că funcția `input()` tratează toate intrările utilizatorului ca șiruri, indiferent de ce este introdus. Dacă aveți nevoie să efectuați calculații sau comparații cu intrarea ca numere, s-ar putea să aveți nevoie să convertiți intrarea în tipul de date corespunzător utilizând funcții precum `int()` sau `float()`.

Funcția `input()` este o unealtă utilă pentru crearea de programe interactive care pot accepta intrarea de la utilizator și pot răspunde în consecință.