'''

Tema 4
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 4 și ia notițe în caz că ți-a scăpat ceva.
2. Vizualizează din ‘Primii pași în Programare’ video.

- Flow Control;
- Funcții.

Astfel, la întâlnirea LIVE deja va fi a 2-a oară când vei auzi conceptele și sigur ți
se vor întipări în minte mai bine.
Link: https://www.itfactory.ro/8174437-intro-in-programare/
Iterațiile sunt mai dificile deoarece necesită putină gândire algoritmică.
Te rog să scrii pe canalul de comunicare scrisă unde întâmpini dificultăți și te
ajut.
Dacă stai blocat > 30 min, cere indiciu.

Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat',
'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat',
'Trabant', 'Opel']
for i in range(len(masini)):
    if masini[i] == 'Aston Martin':
        print(f'Masina mea preferata este {masini[i]}')

for car in masini:
    if car == 'Audi':
        print(f'Masina mea preferata este {car}')

index = masini.index('BMW')
while masini:
    if 'BMW' in masini:
        print(f'Masina mea preferata este {masini[index]}')
    break
'''
2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
'''
for i in range(1,len(masini) - 1):
        masini[i] = masini[i].upper()
else:
    print(masini)
'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
'''
for i in range(len(masini)):
    if masini[i] == 'MERCEDES':
        print(F'Am gasit masina dorita de dumneavoastra')
        break
    else:
        print(f'Am gasit masina {masini[i]} mai cautam')
'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
- Printează S-ar putea să vă placă mașina x.
'''
for i in range(len(masini)):
    if masini[i] == 'TRABANT' or masini[i] == 'LASTUN':
        continue
    print(f'S-ar putea sa va placa masina {masini[i]}')
'''
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.
'''
masini_vechi = []
for i in range(len(masini)):
    if masini[i] == 'LASTUN' or masini[i] == 'TRABANT':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(f'Modele vechi {masini_vechi}')
print(f'Modele noi {masini}')
'''
6. Având dict:
'''
pret_masini = {
'Dacia': 6800,
'Lastun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
'''
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
'''
bugetClient = 15000
# keys = [k for k, v in pret_masini.items() if v <= client]
# print(f'Pentru un buget de sub 15000 euro puteti alege masina: {keys}')
for key, value in pret_masini.items():
    if value <= bugetClient:
        print(f'Pentru un buget de sub 15000 euro puteti alege masina {key}')
'''
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
contor = 0
for i in range(len(numere)):
    if numere[i] == 3:
        contor += 1
print(f'Numarul 3 apare de {contor} ori')
'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''
sumElemLista = 0
for i in range(len(numere)):
    sumElemLista += numere[i]
print(f'Suma numerelor din lista este {sumElemLista}')
'''
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
numarMaxim = 0
for i in range(len(numere)):
    if numarMaxim < numere[i]:
        numarMaxim = numere[i]
print(f'Numarul cel mai mare este {numarMaxim}')
'''
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -abs(numere[i])
print(numere)
'''
Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
1.
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
'''
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''
for i in range(len(alte_numere)):
    if alte_numere[i] % 2 == 0:
        numere_pare.append(alte_numere[i])
    if alte_numere[i] % 2 == 1:
        numere_impare.append(alte_numere[i])
    if alte_numere[i] > 0:
        numere_pozitive.append(alte_numere[i])
    if alte_numere[i] < 0:
        numere_negative.append(alte_numere[i])
print(f'Numerele pare din lista sunt: {numere_pare}')
print(f'Numerele impare din lista sunt: {numere_impare}')
print(f'Numerele pozitive din lista sunt: {numere_pozitive}')
print(f'Numerele negative din lista sunt: {numere_negative}')
'''
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
'''
aux = 0
for i in range(len(alte_numere)):
    for j in range(len(alte_numere) - 1):
        if alte_numere[j] > alte_numere[j + 1]:
            aux = alte_numere[j]
            alte_numere[j] = alte_numere[j + 1]
            alte_numere[j + 1] = aux
print(f'Lista sortata lexicografic este: {alte_numere}')
'''
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!
'''
import random

numar_secret = random.randint(1,30)
numar_ghicit = None
print(numar_secret)
user = int(input("Alegeti un numar "))
if user < 1 or user > 30:
    print("Alege un numar intre 1 si 30")
    user = int(input('Alegeti un numar'))
while user >= 1 and user <= 30:
    if numar_secret > user:
        print(f'Numar secret este mai mare [{numar_secret}], ai ales {user}')
        break
    elif numar_secret < user:
        print(f'Numar secret este mai mic [{numar_secret}], ai ales {user}')
        break
    else:
        print(f'Felicitari! Ai ghicit :)) numarul secret este {numar_secret} si ai ales {user}')
        break
'''
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''
n = int(input('Dati un numar'))
for i in range(n + 1):
    for j in range(i + 1):
        print(i, end='')
    print('\b')
'''
5.
'''
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este: {tastatura_telefon[i][j]}')
'''
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''