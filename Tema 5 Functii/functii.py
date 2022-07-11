'''
Tema 5 - Funcții
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 5 și ia notițe în caz că ți-a scăpat ceva.
2. Vizualizează din ‘Primii pași în Programare’ video.

- OOP;

Astfel, la întâlnirea LIVE deja va fi a 2-a oară când vei auzi conceptele și sigur ți
se vor întipări în minte mai bine.
Link: https://www.itfactory.ro/8174437-intro-in-programare/
Pentru toate exercițiile. Apelați funcția de cel puțin 2 ori cu valori diferite
pentru a testa. Daca functia are return, printati raspunsul
Te rog să scrii pe canalul de comunicare scrisă unde întâmpini dificultăți și te
ajut.
Dacă stai blocat > 30 min, cere indiciu.
Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
1.Funcție care să calculeze și să returneze suma a două numere
'''
def suma_numerelor(a, b):
    return a + b

#x = int(input("Dati un numar "))
#y = int(input("Dati al doilea numar "))
x = 12
y = 3
rez = suma_numerelor(x, y)
print(rez)  # 15
'''
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
'''
def numarPar_impar(a):
    if a % 2 == 0:
        return True
    return False

#nrPar_impar = int(input("Dati numarul "))
nrPar_impar = 8
print(numarPar_impar(nrPar_impar))  # True
'''
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
'''
def numarCaractere(nume, nume_mijlociu, prenume):
    nume_complect = nume + nume_mijlociu + prenume
    result = 0
    for char in nume_complect:
        result += 1
    return result

numeDEfamilie = 'Filip'
prenume_1 = 'Lucian'
prenume_2 = 'Dorin'
print(numarCaractere(numeDEfamilie, prenume_1, prenume_2))  # 11

'''
4. Funcție care returnează aria dreptunghiului
'''
def ariaDreptunghiului(lungime, latime):
    return lungime * latime

lungimeTriunghi = 10
latimeTriunghi = 4
print(ariaDreptunghiului(lungimeTriunghi, latimeTriunghi))  # 40
'''
5. Funcție care returnează aria cercului
'''
def ariaCercului(raza):
    pi = 3.14159
    arie = pi * raza * raza
    return arie

razaCerc = 3
print(ariaCercului(razaCerc))   # 28.27430999999996
'''

6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și Talse dacă nu găsește.
'''
def gasireCaractere(string, char):
    for i in range(len(string)):
        if string[i] == char:
            return True
    return False

string = "It factory"
char = 'I'
print(gasireCaractere(string, char))    # True
'''
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
'''
def functieFaraReturn(string):
    lowerCase = 0
    upperCase = 0
    for a in string:
        if a.islower() == True:
            lowerCase += 1
        elif a.isupper() == True:
            upperCase += 1
    print(f'Nr de caractere lower case este: {lowerCase}')  # 7
    print(f'Nr de caractere upper case este: {upperCase}')  # 3

strings = 'Ana aRe merE'
functieFaraReturn(strings)
'''
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
'''

def lista(numere):
    listaNumerePoz = []
    for i in numere:
        if i > 0:
            listaNumerePoz.append(i)
    return listaNumerePoz

listaNumere = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10]
print(lista(listaNumere))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
'''
def crescatorDescrescatorEgale(x, y):
    if x > y:
        print(f'Primul număr {x} este mai mare decat al doilea nr {y}') # 12 > 5
    elif x < y:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else:
        print("Numerele sunt egale")

primulNumar = 12
aldoileaNumar = 5
crescatorDescrescatorEgale(primulNumar,aldoileaNumar)
'''
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
'''
def functieSet(unNumar, setDeNumere):
    ok = False
    for i in setDeNumere:
        if i == unNumar:
            ok = True

    if ok == True:
        print(f'Nu am adaugat numarul {unNumar} in set Acesta aexista deja')  # 'Nu am adaugat numarul 1 Acesta exista deja
        return False

    print(f'Am adaugat numarul {unNumar} in set')
    return True

setCuNumere = {1, 2, 3, 4, 5, 6, 7}
nrDeAdaugat = 1
print(functieSet(nrDeAdaugat,setCuNumere))  # False
'''

Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
1. Funcție care primește o lună din an și returnează câte zile are acea luna
'''
def lunaAn(luna):
    nrZile = 0
    if luna == 'Februarie':
        nrZile = 28
        return nrZile
    elif luna == 'Ianuarie' or luna == 'Martie' or luna == 'Mai' or luna == 'Iulie' or \
            luna == 'August' or luna == 'Octombrie' or luna == 'Decembrie':
        nrZile = 31
        return nrZile
    elif luna == 'Aprilie' or luna == 'Iunie' or luna == 'Septembrie' or luna == 'Noiembbrie':
        nrZile = 30
        return nrZile

lunaAnului = 'Iunie'
print(f'Luna {lunaAnului} are {lunaAn(lunaAnului)} de zile')   # Luna Iunie are 30 de zile
'''
2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)
● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)
'''
def calculator(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d

a, b, c, d = calculator(10, 2)
print(f'Suma, diferenta, Inmultirea, Imppartirea: {calculator(10, 2)}')    # (12, 8, 20, 5.0)
'''
3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''
from collections import Counter

def listReturnDict(listaCif):
    aparitii = Counter(listaCif)
    return aparitii

listaDeCifre = [1, 3, 1, 5, 9, 7, 7, 5, 5]
print(f'Am obtinut dictionarul: {listReturnDict(listaDeCifre)}')  # Counter({5: 3, 1: 2, 7: 2, 3: 1, 9: 1})
'''
4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
'''
def numarMaxim(x, y, z):
    if (x >= y and x >= z):
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z >= y:
        return z

nr_1 = 2
nr_2 = 11
nr_3 = 11
print(f'Numarul maxim este: {numarMaxim(nr_1, nr_2, nr_3)}') # 11
'''
5. Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
'''
def sumaNumar(nr):
    r = 0
    for i in range(nr + 1):
        r += i
    return r

n = 6
print(f'Suma numerelor = {sumaNumar(n)}') # 21
'''
Exerciții Opționale - Bonus
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune
Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
'''
def douaListe(list_1, list_2):
    list_3 = []
    for element in list_1:
        if element in list_2:
            list_3.append(element)
    return list_3

list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
print(F'Numerele comune sunt: {douaListe(list1,list2)}')
'''
2.. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
'''
def reducerePret(pret_intreg, procent_reducere):
    pret_redus = pret_intreg * procent_reducere / 100
    pret_final = pret_intreg - pret_redus
    if procent_reducere < pret_intreg:
        print(f'Pret final = {pret_final}')
    else:
        print("Reducere invalida")

pret = int(input("Pretul este: "))
reducere = float(input("Reducere de "))
reducerePret(pret, reducere)
'''

3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)
'''
from datetime import datetime
import pytz

def dataSioraCurenta():
    dataCurenta = datetime.now(pytz.timezone('Europe/Athens')) # nu am reusit sa descopar de ce nu merge cu Buckarest
    current_time = datetime.now(pytz.timezone('Asia/Shanghai')) # nu am reusit sa descopar de ce nu merge cu Beijing
    print(f'Data si ora curenta in Romania este: {dataCurenta.strftime("%d/%m/%Y %H:%M:%S")}')
    print(f'Data si ora curenta in China este: {current_time.strftime("%Y-%m-%d %H:%M:%S")}')

dataSioraCurenta()
'''
4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
'''

class Data: # https://www.geeksforgeeks.org/python-program-to-find-number-of-days-between-two-given-dates/?ref=lbp
    def __init__(self, zi, luna, an):
        self.zi = zi
        self.luna = luna
        self.an = an

zileLuna = [31, 28, 31, 30, 31, 30,     # stochez numarul de zile din toate lunile anului
             31, 31, 30, 31, 30, 31]

def countLeapYears(zi):     # in aceasta functie numar anii bisecti inainte de data data
    ani = zi.an
    # Verific dacă anul curent trebuie luat în considerare
    # pentru numărul de ani bisecți sau nu
    if (zi.luna <= 2):
        ani -= 1
    # Un an este un an bisect dacă este multiplu de 4,
    # multiplu de 400 și nu multiplu de 100.
    return int(ani / 4) - int(ani / 100) + int(ani / 400)

def getDifference(dt1, dt2):    # Aceasta funcție returneaza numarul de zile între doua date
    # Numara numarul total de zile inainte de prima data „dt1”
    # initializez numărul folosind ani și zile
    n1 = dt1.an * 365 + dt1.zi

    # Adaugați zile pentru luni la data data
    for i in range(0, dt1.luna - 1):
        n1 += zileLuna[i]
    # Deoarece fiecare an bisect are 366 de zile,adaug o zi pentru fiecare an bisect
    n1 += countLeapYears(dt1)
    # În mod similar, numara numarul total de zile inainte de dt2
    n2 = dt2.an * 365 + dt2.zi
    for i in range(0, dt2.luna - 1):
        n2 += zileLuna[i]
    n2 += countLeapYears(dt2)
    # returneaza diferenta dintre cele doua contoare
    return (n2 - n1)

dt1 = Data(5, 7, 2022)
dt2 = Data(29, 10, 2022)
print(f'Pana la ziua mea de nastere mai sunt: {getDifference(dt1,dt2)} de zile')
'''
'''