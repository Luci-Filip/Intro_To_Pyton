'''
Tema 2
Exerciții Recomandate - grad de dificultate: Ușor .
1. Revizualizează întâlnirea 2 și ia notițe în caz că ți-a scăpat ceva.
2. Vizualizează din ‘Primii pași în Programare’ video.

- Operatori și Flow Control

Astfel, la întâlnirea LIVE deja va fi a 2-a oară când vei auzi conceptele și sigur ți
se vor întipări în minte mai bine.
Link: https://www.itfactory.ro/8174437-intro-in-programare/

Exerciții obligatorii - grad de dificultate: Ușor spre Mediu .
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.
1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
else.
    - if este o structura de decizie, compusa din conditia de functionare si instructiuni,
        daca conditia din if este indeplinita atunci se executa instructiunile de cod care apartin de if
        daca conditia din if nu este indeplinita nu se mai executa instructiunile de cod care apartin de if
    - else are intotdeauna in fata un if, nu are conditie de functionare dar are instructiuni,
        daca nu se intra in if atunci sigur se intra in instructiunile din else
    - exemplu: avem doua numere si vrem sa il afisam pe cel mai mare;
        x = 1, y = 2
        if (x > y):
            print(x)
        else:
            print(y)

2. Verifică și afișează dacă x este număr natural sau nu.
'''
x = 10
if (int(x) > 0):
    print(f'{x} este numar natural')
else:
    print(f'{x} nu este numar natural')


'''
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
'''
if (x > 0):
    print(f'{x} este numar pozitiv')
elif (x < 0):
    print(f'{x} este numar negativ')
else:
    print(f'{x} este numar neutru')
'''
4. Verifică și afișează dacă x este între -2 și 13.
'''
if (x > -1 and x < 14):
    print(f'{x} este in intervalul "-2 si 13"')
else:
    print(f'{x} nu este in intervalul -2 si 13')
'''
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
'''
y = 11
if (x - y < 5):
    print(f'Diferenta dintre x si y este mai mica decat 5')
'''
6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
'''
if (not (x >= 5 and x <= 27)):
    print(f'{x} nu este in intervalul dat')
'''

7.
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.
'''
if (x == y):
    print(f'{x} este egal cu {y}')
elif (x > y):
    print(f'{x} este mai mare decat {y}')
else:
    print(f'{y} este mai mare decat {x}')
'''
8.
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
X = 5
Y = 4
Z = 4
if (X == Y and Y == Z):
    print(f'laturile {X} {Y} {Z} formeaza un triunghi echilateral')
elif ((X > Z and Y == Z) or (X == Z and Y > Z) or (X < Y and Y == Z) or (X == Y and Y > Z)):
    print(f'laturile {X} {Y} {Z} formeaza un triunghi isoscel')
elif (X == Y and Y < Z):
    print(f'laturile {X} {Y} {Z} formeaza un triunghi isoscel')
else:
    print(f'laturile {X} {Y} {Z} formeaza un triunghi oarecare')
'''

9. Citește o literă de la tastatură.

Verifică și afișează dacă este vocală sau nu
'''
ch = input('Citeste litera')
if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print(f'Litera {ch} este vocala')
elif (ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print(f'Litera {ch} este vocala')
else:
    print(f'Litera {ch} nu este vocala')
'''
10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
nota = 4.9
if (nota > 9):
    nota = 'A'
    print(nota)
elif (nota > 8 and nota < 9):
    nota = 'B'
    print(nota)
elif (nota > 7 and nota < 8):
    nota = 'C'
    print(nota)
elif (nota > 6 and nota < 7):
    nota = 'D'
    print(nota)
elif (nota > 4 and nota < 6):
    nota = 'E'
    print(nota)
elif (nota <= 4):
    nota = 'F'
    print(nota)
'''

Exerciții Opționale - grad de dificultate: Mediu spre greu - might need Google.
1.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''
number_x = 123
count = 0
if (number_x == 0):
    count = count + 1
else:
    while (number_x):
        count = count + 1
        number_x = number_x // 10
if (count >= 4):
    print(f'Numarul are minim 4 cifre')
else:
    print(f'Numarul nu are minim 4 cifre')
'''
2.Verifică dacă x are exact 6 cifre.
'''
if (count == 6):
    print(f'Numarul are {count} cifre')
'''
3.Verifică dacă x este număr par sau impar (x e int).
'''
number_x2 = 5
if (number_x2 % 2 == 0):
    print(f'Numarul {number_x2} este par')
else:
    print(f'Numarul {number_x2} este impar')
'''
4. x, y, z (int)
Afișează care este cel mai mare dintre ele?
'''
x1 = 3
y1 = 5
z1 = 5
if (x1 > y1 and x1 > z1):
    print(f'{x1} este cel mai mare numar')
elif (y1 > x1 and y1 > z1):
    print(F'{y1} este cel mai mare numar')
elif (z1 > x1 and z1 > y1):
    print(f'{z1} este cel mai mare numar')
else:
    print("Cel putin 2 numere sunt egale")
'''

5.
X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
'''
lx = 2
ly = 2
lz = 0
if (lx == 0 or ly == 0 or lz == 0):
    print('Nu este un triunghi valid')
else:
    print("Este un triunghi valid")

'''
Exerciții Bonus (may need google) .
1.Verificare îmbarcare persoane
Ține minte următoarele date:
- Vârstă;
- Însoțit de mama;
- Însoțit de tata;
- Pașaport;
- Act permisiune mama;
- Act permisiune tata.
'''
age = 18
accompanyMother = True
accompanyFather = True
passport = True
actPermissionMother = True
actPermissionFather = True
'''
Condiții de îmbarcare
- Dacă pers are vârstă peste 18 ani și are pașaport.
- Dacă pers are sub 18 ani, are pașaport și e însoțită de ambii părinți.
- Dacă pers are sub 18 ani, are pașaport, e însoțită de cel puțin un părinte
și are permisiune în scris de la celalat părinte.
● Aici vreau să testezi codul cu toate variantele posibile.
● Să generezi cazuri de test și expected result, apoi să rulezi codul și să
completezi actual results.
Ex:
Vârstă 19 ani, nu am pașaport => Nu mă pot îmbarca.
Vârstă 17 ani, am pașaport, ambii părinți => Mă pot îmbarca.
Etc
2. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random.
Ne imaginam că dăm cu zarul și salvăm acest număr în dice_roll.

Ia un număr ghicit de la utilizator.
Verifică și afișază dacă utilizatorul a ghicit 3 opțiuni:
- Ai pierdut. Ai ales un număr mai mic. Ai ales x dar a fost y.
- Ai pierdut. Ai ales un număr mai mare. Ai ales x dar a fost y.
- Ai ghicit. Felicitări? Ai ales x și zarul a fost y.
'''
import random
a = []
n = int(input("Enter number of elements: "))
for i in range(n):
    dice_roll = a.append(random.randint(0, 20))
    while(input('Alege numar: ')):
        print(f'Ai pierdut. Ai ales un număr mai mic. Ai ales {input()} dar a fost {a}')
        break
    #a.append(random.randint(0, 20))
#print('Randomised list is: ', a)

''''
b = []
utilizator = int(input("Alege un numar de ghicit: "))
for j in range(utilizator):
    dice_roll = b.append(random.randint(0, 3))
    #if (a[i] == b[j]):

print(b)
'''

