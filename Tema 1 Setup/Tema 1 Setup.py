import re
import math
'''
Tema 1 _ Setup, Variabile, Tipuri de date

Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
    Raspuns:
            => un spatiu alocat in memoria calculatorului.

2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :

- string    => nume = 'Lucian'
- int       => varsta = 40
- float     => experientaInprogramare = 0.0
- bool      => vreauSaInvat = True

Observație: Valorile vor fi alese de tine după preferințe.
'''

nume = 'Lucian'
varsta = 40
experientaInprogamare = 0.0
vreauSainvat = True

'''
3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
'''
print(type(nume)) # <class 'str'>
print(type(varsta)) # <class 'int'>
print(type(experientaInprogamare)) # <class 'float'>
print(type(vreauSainvat)) # <class 'float'>

'''
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
'''
experientaInprogamare = round(0.0)
print(experientaInprogamare)

'''
- Verifică tipul acesteia.
'''
print(type(experientaInprogamare)) # <class 'int'>
'''
5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''
print(f'Ma numesc: {nume}')
print(f'Am varsta de: {varsta}')
experientaInprogamare = 0.1
print('Experienta mea in programare este aproae de ' + str(experientaInprogamare))
print('Este ' + str(vreauSainvat) + ' ca vreu sa invat testare automata si mai apoi programare :)')
'''
6. Citește de la tastatură:
- numele;
- prenumele.
'''

numele = input('Introduceti numele')  # Filip
prenumele = input('Introduceti prenumele') # Lucian
print(numele + ' ' + prenumele) # Filip Lucian
'''
Afișează: 'Numele complet are x caractere'.
'''
print('Numele complect are ' + str(len(numele + prenumele)) + ' caractere') # 11

'''
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
'''

lungimea = int(input('Lungime = '))
latimea = int(input('Litime = '))
print('Aria dreptunghiului este ' + str(lungimea * latimea))  # Aria dreptunghiului este 9

'''
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':

- citește de la tastatură un int x;
- afișează stringul fără ultimele x caractere.

ex: Dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'.
'''
numar = int(input('Dati un numar'))
operatie_string = 'Coral is either the stupidest animal or the smartest rock'
print(operatie_string[0:-numar])

'''
9. Același string:
a. declară un string nou care să fie format din primele 5 caractere + ultimele
5;
b. afișează de câte ori apare cuvântul 'the';
c. înlocuiește ‘the’ cu ‘THE’ peste tot - printează rezultatul;
d. salvează într-o variabilă și afișează indexul de start al cuvântului ‘rock’;
- hint: este o funcție care te ajută să faci asta;
folosind această variabilă + slicing, afișează tot stringul până la acest
cuvânt.

Output: 'Coral is either the stupidest animal or the smartest'
'''
string_fata = operatie_string[0:5:]
x = len(operatie_string)
string_spate = operatie_string[x:-6:-1]
string_final = string_fata + string_spate[::-1]
print(string_final) # Coral rock

cuvant = ['Coral', 'is', 'either', 'the', 'stupidest', 'animal', 'or', 'the', 'smartest', 'rock']
print(f'"the" apare de {cuvant.count("the")} ori')

string = ['Coral', 'is', 'either', 'the', 'stupidest', 'animal', 'or', 'the', 'smartest', 'rock']
for cuv in string:
    cuvant = cuv
    if cuv == 'the':
        cuvant = cuv.upper()
    print(cuvant)

text = 'Coral is either the stupidest animal or the smartest rock'
a = re.search(r'\b(rock)\b', text)
print(a.start())
index = a.start()
sliced_text = slice(index)
print(text[sliced_text])

'''
10. Exercițiu:

- citește de la tastatură un string;
- verifică dacă primul și ultimul caracter sunt la fel.
Observație: se va folosi un assert.
Atenție: se dorește că programul să fie case insensitive - 'apA' e acceptat.
'''
word = input('Scrie un string ')
size = len(word)
firstCh = word[0]
lastCh = word[size-1]
#if word[0] == word[size-1]:
#   print('da')
assert firstCh == lastCh,f'Eroare caracterele nu sunt egale'
print("Egale")

'''
11. Având stringul '0123456789':
- Afișează doar numerele pare;
- Afișează doar numerele impare;
- hint: folosește slicing, controlează din pas.
'''
numar = '0123456789'
par = slice(0, len(numar), 2)
print(numar[par])
inPar = slice(1, len(numar), 2)
print(numar[inPar])
'''
12. Utilizand stringul de la 9.d.
- folosește un assert că să verifici dacă acest string conține doar numere;
- hint: merge cu slicing? Probabil că nu... Ce mai știi atunci legat de
string? Poate găsești o funcție ajutătoare.
'''
strIng = 'rock'
print(strIng.isdecimal())

'''

Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai
nevoie de Google).

1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
'''
stringImpar = input('Scrie stringul ')  # ana are cas
mijloc = stringImpar[math.floor(len(stringImpar)/2)]
print(mijloc)  # r

'''
2. Folosind assert, verifică dacă un string este palindrom.
'''
stringPalindrom = 'uru'
assert stringPalindrom[::-1] == stringPalindrom
print("Da")

'''
3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
'''
cuvant_nou = input('Citeste cuvat nou ')
cuvant_1 = ''
cuvant_2 = ''
for i in range(len(cuvant_nou)):
    if (cuvant_nou[i] == ' '):
        cuvant_1 = cuvant_nou
        break
    if (cuvant_nou[i-1] == ' '):
        cuvant_2 = cuvant_nou
        break
print(cuvant_1 + ' ' + cuvant_2)

'''
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);

- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****

'''