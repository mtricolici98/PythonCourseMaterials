# Mai multe despre șiruri de caractere și numerice

## Recapitulare privind formatarea șirurilor de caractere

Cea mai bună modalitate de a formata șirurile de caractere în Python este utilizarea F-șirurilor.

F-șirurile oferă o modalitate concisă și expresivă de a formata șirurile de caractere în Python. Au fost introduse în Python 3.6 și versiunile ulterioare. Cu ajutorul F-șirurilor, puteți îngloba expresii și variabile direct într-un șir de caractere prin prefixarea acestuia cu litera 'f' sau 'F'.
Utilizarea F-șirurilor ar trebui făcută doar atunci când se combină cu alte variabile.
Iată un exemplu:

```python
name = "Marius" # Nu folosim F-șirul, deoarece nu îl combinăm cu alte variabile
country = "Moldova"
print(f"Sunt {name} din {country}") # Folosim F-șiruri deoarece combinăm alte variabile
```

Nu modificați niciun cod, puteți modifica comentariile codului.

## Șiruri de caractere pe mai multe linii

Șirurile de caractere pe mai multe linii în Python sunt o modalitate convenabilă de a reprezenta și stoca textul care se întinde pe mai multe linii. Ele sunt delimitate de ghilimele triple (fie simple, fie duble) și vă permit să includeți întreruperi de linie și să păstrați formatarea textului. Iată o prezentare succintă a șirurilor de caractere pe mai multe linii în Python pentru începători:

1. Sintaxa:
   Șirurile de caractere pe mai multe linii sunt definite folosind ghilimele triple (''' sau """).
   ```python
   text = '''
   Acesta este un șir de caractere pe mai multe linii.
   Poate conține mai multe linii de text.
   '''
   ```

2. Întreruperi de linie:
   Puteți include întreruperi de linie într-un șir de caractere pe mai multe linii pur și simplu apăsând tasta Enter. Întreruperile de linie vor fi păstrate atunci când șirul este afișat sau folosit în altă parte în cod.
   ```python
   text = '''Acesta este un șir de caractere pe mai multe linii.
   Poate întinde pe mai multe linii.'''
   ```

3. Păstrarea formatației:
   Șirurile de caractere pe mai multe linii păstrează formatarea pe care o furnizați, inclusiv spațiile inițiale și indentarea. Aceasta este utilă atunci când lucrați cu exemple de cod, paragrafe sau orice text care necesită spațiere specifică.
   ```python
   exemplu_cod = '''
   def functia_mea():
       print("Salut, lume!")
   '''
   print(exemplu_cod)

   paragraf = '''
   Acesta este un paragraf lung care trebuie formatat corect.
   Poate conține mai multe propoziții și întreruperi de linie.
       Unele linii pot avea, de asemenea, indentare suplimentară.
   '''
   print(paragraf)
   ```

4. Utilizarea șirurilor de caractere pe mai multe linii:
   Șirurile de caractere pe mai multe linii pot fi atribuite variabilelor, afișate, concatenate cu alte șiruri de caractere sau folosite ca docstrings (un tip de șir folosit pentru documentarea funcțiilor, claselor sau modulelor).
   ```python
   text = '''Acesta este un șir de caractere pe mai multe linii.'''
   print(text)

   text = text + ''' Poate fi concatenat cu alte șiruri de caractere.'''
   ```

Șirurile de caractere pe mai multe linii sunt o funcționalitate utilă în Python atunci când aveți nevoie să lucrați cu blocuri mari de text sau să păstrați o formatare specifică. Ele oferă flexibilitate și lizibilitate, în special în situațiile în care e nevoie sa mentineti structura textului.

## Escaparea caracterelor

În Python, escaparea caracterelor este un mecanism care vă permite să includeți caractere speciale sau simboluri într-un șir de caractere folosind secvențe de escape. Secvențele de escape sunt combinații de caractere care reprezintă anumite caractere speciale și nu pot fi interpretate ca litere. Iată câteva secvențe de escape comune în Python:

**Notă: Utilizați `print(text)` pentru a testa fiecare situație**

1. Bara oblică inversă (\):
   Caracterul bara oblică inversă în sine poate fi escapată folosind o altă bara oblică inversă. Aceasta este utilă atunci când doriți să includeți o bara oblică inversă literală în șirul de caractere.
   ```python
   text = "Acesta este un exemplu de bara oblică inversă: \\"
   ```

2. Linie nouă (\n):
   Secvența de escape pentru linie nouă (\n) este utilizată pentru a insera o linie nouă într-un șir de caractere. Când șirul este afișat sau afișat, \n este interpretat ca o întrerupere de linie.
   ```python
   text = "Aceasta este prima linie.\nAceasta este a doua linie."
   ```

3. Tabulator (\t):
   Secvența de escape pentru tabulator (\t) introduce un tabulator orizontal într-un șir de caractere. Este utilizat în mod obișnuit pentru indentare sau aliniere text.
   ```python
   text = "Nume:\tJohn\nVârstă:\t25"
   ```

4. Apostrof simplu (\'):
   Secvența de escape pentru apostrof simplu (\') este utilizată pentru a include un apostrof simplu într-un șir de caractere care este delimitat de apostrofe simple.
   ```python
   text = 'El a spus, \'Bună!\''
   ```

5. Ghilimea dublă (\"):
   Secvența de escape pentru ghilimeaua dublă (\") este utilizată pentru a include o ghilimea dublă într-un șir de caractere care este delimitat de ghilimele duble.
   ```python
   text = "Ea a spus, \"Salut!\""
   ```

6. Backspace (\b):
   Secvența de escape pentru backspace (\b) este utilizată pentru a elimina caracterul anterior dintr-un șir de caractere.
   ```python
   text = "Hello\bWorld"  # Afișează: HellWorld
   ```

7. Carriage return (\r):
   Secvența de escape pentru carriage return (\r) mută cursorul la începutul liniei curente dintr-un șir de caractere.
   ```python
   text = "Hello\rWorld"  # Afișează: World
   ```

Acestea sunt doar câteva exemple de secvențe de escape în Python. Acestea vă permit să includeți caractere speciale, să controlați formatarea și să gestionați situați

ile în care anumite caractere trebuie reprezentate într-un șir de caractere. Utilizând secvențe de escape, puteți manipula și formata șiruri de caractere într-un mod mai flexibil.

## Șirurile de caractere ca liste de caractere

În Python, șirurile de caractere sunt, în principiu, o secvență (o listă) de caractere individuale, ceea ce înseamnă că puteți efectua diverse operații asupra lor așa cum ați face cu o listă (este important să vă amintiți acest lucru pentru momentul în care lucrăm cu liste). Iată o prezentare generală a modului în care lucrul cu șirurile de caractere ca liste de caractere poate fi benefic:

1. Lungime:
   Puteți determina lungimea unui șir de caractere, adică numărul de caractere pe care le conține, folosind funcția `len()`. Aceasta returnează numărul total de caractere din șir.
   ```python
   text = "Salut, lume!"
   lungime = len(text)
   print(lungime)  # Output: 13
   ```

2. Accesarea caracterelor folosind indici:
   Șirurile de caractere pot fi accesate caracter cu caracter folosind indici. Fiecare caracter din șir are o poziție unică de indexare, începând de la 0 pentru primul caracter. Puteți accesa un anumit caracter furnizându-i indexul între paranteze pătrate.
   ```python
   text = "Salut"
   primul_caracter = text[0]
   print(primul_caracter)  # Output: 'S'
   ```

3. Enumerarea caracterelor:
   Puteți itera peste un șir de caractere ca și cum ar fi o listă pentru a accesa și procesa fiecare caracter în mod individual. Funcția `enumerate()` poate fi utilizată pentru a obține atât indexul, cât și caracterul de la acel index.
   ```python
   text = "Salut"
   for index, caracter in enumerate(text):
       print(f"Caracterul la indexul {index}: {caracter}")
   ```
   Output:
   ```
   Caracterul la indexul 0: S
   Caracterul la indexul 1: a
   Caracterul la indexul 2: l
   Caracterul la indexul 3: u
   Caracterul la indexul 4: t
   ```

4. Segmentarea șirului de caractere (slicing):
   Segmentarea șirului de caractere vă permite să extrageți o porțiune dintr-un șir de caractere prin specificarea unei plaje de indici. Aceasta returnează un nou șir de caractere care conține caracterele selectate. Notația de segmentare utilizează formatul `[start:stop:step]`, unde `start` este indexul de început (inclusiv), `stop` este indexul de încheiere (exclusiv) și `step` este numărul de caractere care trebuie să fie trecute între fiecare caracter selectat.
   ```python
   text = "Salut, lume!"
   sub_string = text[7:12]
   print(sub_string)  # Output: "lume"
   ```

5. Indici negativi:
   Indicii negativi pot

 fi utilizați nu numai pentru a accesa caractere individuale într-un șir de caractere, ci și pentru segmentarea șirului de caractere. Iată o explicație succintă despre modul în care indicii negativi funcționează în ambele cazuri:

   1. Accesarea caracterelor individuale cu indici negativi:
   Indicii negativi vă permit să accesați caractere individuale într-un șir de caractere începând de la sfârșit. Indexul -1 reprezintă ultimul caracter, -2 reprezintă penultimul caracter și așa mai departe.
   ```python
   text = "Salut"
   ultimul_caracter = text[-1]
   print(ultimul_caracter)  # Output: 't'

   penultimul_caracter = text[-2]
   print(penultimul_caracter)  # Output: 'u'
   ```

   2. Segmentarea șirului de caractere cu indici negativi:
   Indicii negativi pot fi utilizați și în segmentarea șirului de caractere pentru a extrage o porțiune a șirului. Atunci când utilizați indici negativi în segmentare, operația de segmentare începe de la sfârșitul șirului.
   ```python
   text = "Salut, lume!"
   sub_string = text[-6:-1]
   print(sub_string)  # Output: "lume"

   string_inversat = text[::-1]
   print(string_inversat)  # Output: "!emul ,tulaS"
   ```

   În exemplul de mai sus, `text[-6:-1]` extrage subșirul "lume" din șir numărând caracterele de la sfârșit.

   Utilizarea indiciilor negative în segmentarea șirului de caractere și accesarea caracterelor individuale vă permite să lucrați în mod convenabil cu sfârșitul unui șir fără a fi nevoie să calculați pozițiile exacte pe baza lungimii sale. Această funcționalitate simplifică codul și îmbunătățește lizibilitatea, în special atunci când trebuie să accesați sau să manipulați porțiuni ale unui șir de caractere de la sfârșit.

Tratând șirurile de caractere ca liste de caractere, obțineți capacitatea de a accesa caractere individuale, de a determina pozițiile lor, de a itera asupra lor și de a extrage subșiruri folosind segmentarea. Aceasta vă permite să manipulați și să lucrați cu șiruri de caractere într-un mod mai flexibil, facilitând sarcini precum extragerea, transformarea și analiza datelor.

## Metode, metode pentru șiruri de caractere

Metodele în programare sunt funcții asociate anumitor obiecte sau tipuri de date. Acestea vă permit să efectuați operații sau manipulări asupra obiectului asupra căruia sunt apelate. Atunci când apelați o metodă pe un obiect, aceasta lucrează direct cu acel obiect și efectuează o sarcină specifică legată de acesta. În Python, șirurile de caractere sunt obiecte ale tipului de date "șir" și au diverse metode încorporate care vă permit să efectuați operații comune asupra șirurilor.

În cazul șirurilor de caractere, metodele sunt funcții care pot fi apelate pe un obiect de tip șir. Acestea vă permit să manipulați, modificați sau extrageți informații din șir. Aceste metode sunt proiectate să lucreze în mod specific cu șiruri de caractere și oferă modalități convenabile de a efectua operații comune asupra acestora.

Iată câteva exemple de metode pentru șiruri de caractere împreună cu explicațiile lor:

1. `count(subșir)`:
   Metoda `count()` returnează numărul de apariții ale unui subșir specificat într-un șir.
   ```python
   text = "Salut, salut, salut!"
   numar = text.count("salut")
   print(numar)  # Output: 3
   ```

2. `lower()` și `upper()`:
   Metoda `lower()` convertește toate caracterele unui șir la litere mici, în timp ce metoda `upper()` le convertește la litere mari.
   ```python
   text = "Salut, Lume!"
   litere_mici = text.lower()
   print(litere_mici)  # Output: "salut, lume!"

   litere_mari = text.upper()
   print(litere_mari)  # Output: "SALUT, LUME!"
   ```

3. `replace(vechi, nou)`:
   Metoda `replace()` înlocuiește toate aparițiile unui subșir specificat cu un alt subșir în cadrul unui șir.
   ```python
   text = "Salut, Lume!"
   text_nou = text.replace("Salut", "Bună")
   print(text_nou)  # Output: "Bună, Lume!"
   ```

4. `split(separator)`:
   Metoda `split()` împarte un șir într-o listă de subșiruri pe baza unui separator specificat. În mod implicit, separatorul este un spațiu.
   ```python
   text = "Salut, Lume!"
   cuvinte = text.split()
   print(cuvinte)  # Output: ["Salut,", "Lume!"]

   propoziție = "Aceasta-este-o-propoziție"
   segmente = propoziție.split("-")
   print(segmente)  # Output: ["Aceasta", "este", "o", "

propoziție"]
   ```

5. `startswith(prefix)` și `endswith(suffix)`:
   Metoda `startswith()` verifică dacă un șir începe cu un prefix specificat, în timp ce metoda `endswith()` verifică dacă se termină cu un sufix specificat. Acestea returnează o valoare Booleană care indică rezultatul.
   ```python
   text = "Salut, Lume!"
   incepe_cu_salut = text.startswith("Salut")
   print(incepe_cu_salut)  # Output: True

   se_termină_cu_lume = text.endswith("Lume")
   print(se_termină_cu_lume)  # Output: False
   ```

Prin utilizarea metodelor, puteți efectua ușor diverse operații asupra obiectelor de tip șir fără a fi nevoie să scrieți logica de la zero. Metodele oferă o modalitate de interacțiune cu obiectele și de efectuare a acțiunilor specifice tipului de date al obiectului, făcând ca codul dvs. să fie mai concis, mai lizibil și mai eficient.

Amintiți-vă că diferite tipuri de date (cum ar fi șirurile de caractere, liste sau numere) au propriul lor set de metode adaptate pentru a lucra cu ele. Deci, atunci când utilizați metode, profitați de puterea și funcționalitatea care vin odată cu obiectul cu care lucrați.

## Conversie de tipuri (Type casting)

În Python, puteți converti șiruri de caractere în tipuri de date numerice folosind un proces numit "casting" (conversie de tip). Conversia de tipuri, cunoscută și sub denumirea de conversie de tipuri, este procesul de transformare a unui tip de date în altul. Aceasta vă permite să schimbați interpretarea și comportamentul datelor, permițând compatibilitatea între diferite tipuri și facilitând operațiile care necesită reprezentări consistente ale datelor.
Conversia vă permite să convertiți un șir de caractere care reprezintă un număr într-o valoare numerică reală. Acest lucru poate fi util atunci când trebuie să efectuați operații matematice sau comparații pe date numerice bazate pe șiruri de caractere. Iată o explicație prietenoasă pentru începători despre conversia șirurilor de caractere în numere în Python:

1. Conversie în întreg:
   Puteți converti un șir de caractere într-un întreg folosind funcția `int()`. Aceasta elimină spațiile de la început și sfârșitul șirului și îl convertește într-un întreg.
   ```python
   num_str = "42"
   num = int(num_str)
   print(num)  # Output: 42
   ```

2. Conversie în număr în virgulă mobilă:
   Pentru a converti un șir de caractere într-un număr în virgulă mobilă, puteți utiliza funcția `float()`. Aceasta convertește șirul într-o valoare în virgulă mobilă, permițând și cifre zecimale și aritmetică în virgulă mobilă.
   ```python
   float_str = "3.14"
   float_num = float(float_str)
   print(float_num)  # Output: 3.14
   ```

3. Tratarea conversiilor nevalide:
   Este important să rețineți că nu toate șirurile de caractere pot fi convertite cu succes în numere. Dacă un șir de caractere nu poate fi interpretat ca un număr valid, va fi generată o excepție `ValueError`. Vom învăța ulterior cum putem gestiona astfel de erori, dar deocamdată ar trebui să încercăm să le evităm.
   ```python
   invalid_str = "Hello"
   invalid_num = int(invalid_str)
   print(invalid_num)  # Generează ValueError
   ```

4. Alte conversii numerice:
   În afară de `int()` și `float()`, există alte funcții încorporate pentru conversii specifice:
   - `complex()` convertește un șir de caractere într-un număr complex.
   - `bin()` convertește un întreg într-un șir de caractere binar.
   - `hex()` convertește un întreg într-un șir de caractere hexadecimal.
   - `oct()` converteș

te un întreg într-un șir de caractere octal.

Conversia șirurilor de caractere în numere vă permite să efectuați operații matematice, comparații sau orice alte sarcini care necesită valori numerice. Cu toate acestea, este important să vă asigurați că șirul de caractere reprezintă un număr valid sau să gestionați excepțiile corespunzător atunci când vă ocupați de eventuale erori de conversie.

Conversia de tipuri poate fi utilă atunci când dorim să realizăm mici programe care utilizează date din funcția `input()` pentru a efectua operații matematice. Vom avea multe astfel de exerciții în viitorul apropiat.

## Alte operații matematice suplimentare

Data trecută am discutat despre câteva operații matematice de bază, cum ar fi adunarea, înmulțirea, împărțirea și scăderea. De data aceasta, vom discuta despre câteva operații suplimentare, care sunt adesea utile.

1. Modulo (%):
   Operatorul modulo, reprezentat de simbolul procent (%), calculează restul unei operații de împărțire. Returnează restul când un număr este împărțit la alt număr.
   ```python
   rezultat = 15 % 4
   print(rezultat)  # Output: 3
   ```

   În exemplul de mai sus, împărțirea lui 15 la 4 rezultă 3, cu un rest de 3.

2. Exponentiere (`**`):
   Operatorul de exponentiere, reprezentat de două asteriscuri (**), ridică un număr la o putere. Realizează exponentierea, care este procesul de înmulțire a unui număr cu el însuși de un număr specificat de ori.
   ```python
   rezultat = 2 ** 3
   print(rezultat)  # Output: 8
   ```

   În exemplul de mai sus, 2 ridicat la puterea 3 este egal cu 8.

3. Împărțirea la sol (//):
   Operatorul de împărțire la sol, reprezentat de două linii oblice (//), realizează împărțirea între două numere și rotunjește rezultatul la cel mai apropiat număr întreg (număr întreg). Se elimină partea zecimală a împărțirii.
   ```python
   rezultat = 15 // 4
   print(rezultat)  # Output: 3
   ```

   În exemplul de mai sus, rezultatul împărțirii lui 15 la 4 este 3,75, dar împărțirea la sol îl rotunjește la 3.

Modulo, exponentierea și împărțirea la sol sunt operații matematice utile pe care le puteți întâlni atunci când lucrați cu numere în Python. Modulo vă poate ajuta să determinați divizibilitatea, să găsiți resturi sau să parcurgeți un model. 

Exponentierea vă permite să calculați puteri și să efectuați calculi de creștere sau descreștere exponențială.

Împărțirea la sol este utilă atunci când doriți să împărțiți numere și să obțineți numai partea întreagă a rezultatului. Înțelegerea și utilizarea acestor operatori vă poate îmbunătăți capacitatea de a manipula și efectua calculații cu numere în Python.

## Operatori de atribuire augmentați

Operatorii de atribuire augmentați în Python oferă o modalitate concisă de a efectua o operație și de a atribui rezultatul înapoi aceleiași variabile. Aceștia combină o operație aritmetică sau pe biți cu o atribuire într-o singură instrucțiune. Iată o explicație detaliată a operatorilor de atribuire augmentați:

1. `+=` (Adună și atribuie):
   Operatorul `+=` adaugă o valoare la o variabilă și atribuie rezultatul înapoi aceleiași variabile.
   ```python
   x = 5
   x += 3  # Echivalent cu x = x + 3
   print(x)  # Output: 8
   ```

2. `-=` (Scade și atribuie):
   Operatorul `-=` scade o valoare dintr-o variabilă și atribuie rezultatul înapoi aceleiași variabile.
   ```python
   x = 10
   x -= 4  # Echivalent cu x = x - 4
   print(x)  # Output: 6
   ```

3. `*=` (Înmulțește și atribuie):
   Operatorul `*=` înmulțește o variabilă cu o valoare și atribuie rezultatul înapoi aceleiași variabile.
   ```python
   x = 3
   x *= 2  # Echivalent cu x = x * 2
   print(x)  # Output: 6
   ```

4. `/=` (Împarte și atribuie):
   Operatorul `/=` împarte o variabilă la o valoare și atribuie rezultatul înapoi aceleiași variabile.
   ```python
   x = 10
   x /= 2  # Echivalent cu x = x / 2
   print(x)  # Output: 5.0
   ```

5. `%=` (Calculează modulo și atribuie):
   Operatorul `%=` calculează modulo (restul) al unei variabile împărțite la o valoare și atribuie rezultatul înapoi aceleiași variabile.
   ```python
   x = 15
   x %= 4  # Echivalent cu x = x % 4
   print(x)  # Output: 3
   ```

Operatorii de atribuire augmentați sunt o modalitate concisă de a efectua operații comune pe variabile, actualizându-le în loc. Aceștia pot face codul mai concis și mai ușor de citit, în special atunci când trebuie să modificați repetat o variabilă pe baza unei anumite operații.