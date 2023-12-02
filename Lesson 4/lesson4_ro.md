# Booleans și Logica Booleană

## Ce sunt booleans?

În Python, booleanul este un tip de date care reprezintă una din cele două valori posibile: True (Adevărat) sau False (Fals). Booleanele sunt folosite frecvent în programare pentru a lua decizii, a controla fluxul unui program și a determina condiții.

## Operatorii de comparație în Python

Booleans sunt esențiale pentru crearea de expresii logice, care sunt expresii ce se evaluează la True (Adevărat) sau False (Fals). Aceste expresii sunt construite folosind operatori de comparație, cum ar fi `==` (egalitate), `!=` (inegalitate), `<` (mai mic decât), `>` (mai mare decât), `<=` (mai mic sau egal), și `>=` (mai mare sau egal). Acești operatori compară valorile și returnează un rezultat boolean.

De exemplu, să luăm în considerare următorul fragment de cod:

```python
x = 5
y = 10

print(x == y)  # False
print(x < y)   # True
print(x > y)   # False
```

În acest exemplu, comparăm valorile lui `x` și `y` folosind operatorul de egalitate (`==`) și operatorul de mai mic (`<`). Rezultatele sunt apoi afișate în consolă. După cum puteți observa, expresiile se evaluează fie la True, fie la False, în funcție de comparația dintre valorile lor.

## Blocurile if și else

În Python, blocurile `if` și `else` sunt structuri de control utilizate pentru a executa diferite secțiuni de cod în funcție de anumite condiții. Ele vă permit să luați decizii și să controlați fluxul programului pe baza unei valori booleane.

Să analizăm mai în detaliu cum funcționează blocurile `if` și `else` în Python.

Instrucțiunea `if` este utilizată pentru a executa un bloc de cod numai dacă o anumită condiție este adevărată. Ea urmează această sintaxă generală:

```python
if condiție:
    # Codul de executat dacă condiția este adevărată
```

Iată un exemplu care demonstrează utilizarea unei instrucțiuni `if`:

```python
x = 5

if x > 0:
    print("x este pozitiv")
```

În acest cod, condiția `x > 0` este verificată. Dacă se evaluează la True (Adevărat), codul din blocul `if` (instrucțiunea `print`) este executat. În caz contrar, dacă condiția este False (Fals), codul din blocul `if` este omis.

De asemenea, puteți include un bloc `else` împreună cu instrucțiunea `if` pentru a specifica o cale alternativă de cod atunci când condiția este falsă. Sintaxa pentru utilizarea lui `else` este următoarea:



```python
if condiție:
    # Codul de executat dacă condiția este adevărată
else:
    # Codul de executat dacă condiția este falsă
```

Să luăm în considerare următorul exemplu:

```python
x = 5

if x > 0:
    print("x este pozitiv")
else:
    print("x nu este pozitiv")
```

În acest cod, dacă `x` este mai mare decât 0, se afișează mesajul "x este pozitiv". În caz contrar, dacă `x` nu este mai mare decât 0 (adică este zero sau negativ), se afișează mesajul "x nu este pozitiv".

De asemenea, puteți combina mai multe condiții folosind instrucțiunea `elif` (prescurtare pentru "else if"). Aceasta vă permite să specificați condiții suplimentare de verificat atunci când condiția inițială este falsă. Iată un exemplu:

```python
x = 5

if x > 0:
    print("x este pozitiv")
elif x < 0:
    print("x este negativ")
else:
    print("x este zero")
```

În acest cod, dacă `x` este mai mare decât 0, se afișează mesajul "x este pozitiv". Dacă `x` nu este mai mare decât 0, se verifică următoarea condiție `x < 0`. Dacă această condiție este adevărată, se afișează mesajul "x este negativ". În cele din urmă, dacă ambele condiții sunt false, se afișează mesajul "x este zero".

Blocurile `if` și `else` oferă o modalitate puternică de a lua decizii și de a controla fluxul programului pe baza unor condiții specifice. Prin utilizarea de expresii logice și valori booleane, puteți crea structuri complexe de luare a deciziilor pentru a executa diferite căi de cod.

## Operatori logici (and, or, not)

Booleanele pot fi, de asemenea, combinate folosind operatori logici: `and`, `or` și `not`. Acești operatori vă permit să creați condiții mai complexe prin combinarea a mai multe valori booleane.

Iată un exemplu care demonstrează utilizarea operatorilor logici:

```python
x = 5
y = 10

print(x < 10 and y > 5)  # True
print(x > 10 or y > 20)  # False
print(not x == y)        # True
```

În acest fragment de cod, utilizăm operatorii `and`, `or` și `not` pentru a combina expresii booleane. Operatorul `and` returnează True (Adevărat) dacă ambele expresii sunt True (Adevărat), operatorul `or` returnează True (Adevărat) dacă cel puțin o expresie este True (Adevărat), iar operatorul `not` negă valoarea boolean

ă.

## Valorile considerate a fi Adevărat (Truthy)

Conceptul de "valorile considerate a fi Adevărat" se referă la valorile care sunt considerate logic adevărate atunci când sunt evaluate într-un context boolean. Aceasta înseamnă că, chiar dacă o valoare nu este explicit `True` (Adevărată), poate fi tratată în continuare ca fiind adevărată în anumite situații.

În Python, următoarele valori sunt considerate "adevărate" (Truthy):

- Orice număr nenul: Orice număr care nu este egal cu zero este considerat adevărat. De exemplu, `1`, `2.5`, `-3`, și așa mai departe.

- Șiruri nevide (unele vor fi discutate mai târziu): Șiruri precum `"hello"`, liste nevide `[1, 2, 3]`, tupluri nevide `('a', 'b')`, mulțimi nevide `{1, 2, 3}` sunt considerate adevărate dacă conțin cel puțin un element.

- Mapări nevide (vor fi discutate mai târziu): Mape precum dicționarele sunt considerate adevărate dacă conțin cel puțin o pereche cheie-valoare.

Pe de altă parte, următoarele valori sunt considerate "false" (Falsy):

- Valori numerice zero: Numărul întreg `0` și numărul zecimal `0.0` sunt considerate false.

- Șiruri vide: Șiruri vide precum `""`, liste vide `[]`, tupluri vide `()`, și mulțimi vide `set()` sunt considerate false.

- `None`: Valoarea specială `None` este considerată false.

Conceptul de valori adevărate (Truthy) este adesea folosit în declarații condiționale, cum ar fi buclele `if` și `while`, în care valorile non-booleene sunt convertite implicit în booleene pentru evaluare. De exemplu:

```python
x = 5

if x:
    print("x este adevărat")
else:
    print("x este fals")
```

În acest cod, valoarea lui `x` este evaluată în contextul boolean al instrucțiunii `if`. Dacă `x` este adevărat (adică are o valoare nenulă), se va afișa mesajul "x este adevărat". În caz contrar, dacă `x` este fals (adică este zero sau o secvență vidă), se va afișa mesajul "x este fals".

Înțelegerea valorilor adevărate (Truthy) și false (Falsy) vă permite să scrieți cod mai expresiv și concis prin valorificarea comportamentului conversiei booleene implicite. Vă permite să efectuați verificări condiționale pe o gamă largă de valori, dincolo de valorile literale `True` și `False`.

## Combinarea condițiilor

Combinarea expresiilor logice și a operațiilor booleene în Python vă permite să

 creați condiții complexe prin conectarea mai multor condiții. Aveți la dispoziție următoarele operatori logici pentru a combina condiții:

- `and`: Returnează True (Adevărat) dacă ambele condiții sunt adevărate.

- `or`: Returnează True (Adevărat) dacă cel puțin una dintre condiții este adevărată.

- `not`: Returnează inversul valorii booleane a unei condiții (True devine False și False devine True).

Iată un exemplu care demonstrează combinarea condițiilor:

```python
x = 5
y = 10

if x > 0 and y > 0:
    print("Ambele numere sunt pozitive")

if x > 0 or y > 0:
    print("Cel puțin unul dintre numere este pozitiv")

if not x == y:
    print("x și y nu sunt egale")
```

În acest cod, utilizăm operatorii `and`, `or` și `not` pentru a combina condițiile. Prima instrucțiune `if` verifică dacă ambele numere sunt pozitive. Dacă ambele condiții sunt adevărate, se afișează mesajul "Ambele numere sunt pozitive". A doua instrucțiune `if` verifică dacă cel puțin unul dintre numere este pozitiv. Dacă cel puțin una dintre condiții este adevărată, se afișează mesajul "Cel puțin unul dintre numere este pozitiv". A treia instrucțiune `if` verifică dacă `x` și `y` sunt diferite. Dacă această condiție este adevărată, se afișează mesajul "x și y nu sunt egale".

Combinarea condițiilor vă permite să creați condiții complexe pentru a controla fluxul programului. Puteți realiza verificări multiple și puteți specifica cum trebuie să se îndeplinească aceste condiții pentru a executa anumite acțiuni.
