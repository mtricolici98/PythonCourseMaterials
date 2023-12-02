# Instrucțiuni condiționale

## Ce sunt instrucțiunile condiționale?

Instrucțiunile condiționale reprezintă elemente fundamentale în programare, permițându-ți să iei decizii pe baza unor condiții specifice. Ele permit programului tău să execute diferite blocuri de cod în funcție de faptul dacă o anumită condiție este adevărată sau falsă. În Python, instrucțiunile condiționale includ `if`, `elif` și `else`.

## If și Else:

Instrucțiunea `if` este utilizată pentru a executa un bloc de cod doar dacă o anumită condiție este adevărată. Blocul de cod care urmează instrucțiunii `if` este executat doar dacă condiția este evaluată ca fiind adevărată. Iată un exemplu:

```python
age = 20

if age >= 18:
    print("Ești eligibil pentru a vota.")
```

Output:
```
Ești eligibil pentru a vota.
```

Instrucțiunea `else` poate fi adăugată pentru a specifica un bloc de cod care trebuie executat dacă condiția din instrucțiunea `if` este falsă. Iată un exemplu:

```python
age = 15

if age >= 18:
    print("Ești eligibil pentru a vota.")
else:
    print("Nu ai suficientă vârstă pentru a vota.")
```

Output:
```
Nu ai suficientă vârstă pentru a vota.
```

## Elif (altfel dacă):

Instrucțiunea `elif` îți permite să verifici mai multe condiții. Este utilă atunci când ai mai mult de două posibilități. Blocul de cod care urmează instrucțiunii `elif` este executat dacă condiția corespunzătoare este adevărată. Iată un exemplu:

```python
age = 15

if age >= 18:
    print("Ești eligibil pentru a vota.")
elif age == 17:
    print("Veți fi eligibil pentru a vota în anul viitor.")
else:
    print("Nu ai suficientă vârstă pentru a vota.")
```

Output:
```
Nu ai suficientă vârstă pentru a vota.
```

În acest exemplu, dacă variabila `age` este mai mare sau egală cu 18, se va afișa primul mesaj. Dacă are valoarea 17, se va afișa al doilea mesaj. În caz contrar, se va afișa al treilea mesaj.

Poți avea mai multe instrucțiuni `elif` pentru a verifica diferite condiții.

## Utilizarea operatorilor logici în comparație cu instrucțiunile `if` înlănțuite:

Iată un exemplu care demonstrează utilizarea instrucțiunilor `if` înlănțuite:

```python
age = 25
income = 50000

if age >= 18:
    if income > 30000:
        print("Ești eligibil pentru un credit.")
    else:
       

 print("Nu îndeplinești cerințele de venit.")
else:
    print("Nu ai suficientă vârstă pentru a aplica pentru un credit.")
```

Output:
```
Ești eligibil pentru un credit.
```

În acest exemplu, instrucțiunea `if` exterioară verifică dacă `age` este mai mare sau egală cu 18. Dacă această condiție este adevărată, intră în instrucțiunea `if` înlănțuită, care verifică dacă `income` este mai mare decât 30000. Dacă ambele condiții sunt adevărate, se va afișa mesajul "Ești eligibil pentru un credit".

Dacă condiția din instrucțiunea `if` exterioară este falsă (adică dacă vârsta este mai mică de 18), codul va continua cu blocul `else`, care afișează mesajul "Nu ai suficientă vârstă pentru a aplica pentru un credit."

Instrucțiunile `if` înlănțuite pot fi utile în situațiile în care trebuie să evaluezi mai multe condiții într-o manieră ierarhică, cu diferite niveluri de verificări și acțiuni în funcție de rezultatul fiecărei condiții. Cu toate acestea, pe măsură ce nivelul de înlănțuire crește, codul poate deveni mai complex și mai greu de citit și de întreținut. În astfel de cazuri, utilizarea operatorilor logici precum `and`, `or` și `not` poate duce adesea la un cod mai curat și mai ușor de citit.

Operatorii logici precum `and`, `or` și `not` pot fi utilizați pentru a combina mai multe condiții într-o singură instrucțiune. Aceștia oferă o modalitate de a exprima condiții complexe fără a utiliza instrucțiuni `if` înlănțuite.

Exemplu utilizând `and`:

```python
age = 25
income = 50000

if age >= 18 and income > 30000:
    print("Ești eligibil pentru un credit.")
else:
    print("Nu ești eligibil pentru un credit.")
```

Output:
```
Ești eligibil pentru un credit.
```

În acest exemplu, ambele condiții `age >= 18` și `income > 30000` trebuie să fie adevărate pentru ca mesajul de eligibilitate pentru credit să fie afișat.

Operatorii logici pot fi, de asemenea, combinați cu instrucțiunile `if`, `elif` și `else` pentru a crea structuri de decizie mai complexe.

Utilizarea operatorilor logici este în general preferată în comparație cu utilizarea instrucțiunilor `if` înlănțuite, deoarece face codul mai ușor de citit și de înțeles.