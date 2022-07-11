'''
Tema 6 - OOP _ Clase & Obiecte
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 6 și ia notițe în caz că ți-a scăpat ceva.
Pentru toate clasele, creați cel puțin 2 obiecte cu valori diferite și apelați toate
metodele clasei.
Te rog să scrii pe canalul de comunicare scrisă unde întâmpini dificultăți și te
ajut.
Dacă stai blocat > 30 min, cere indiciu.
Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
'''

import math

class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrierecerc(self):
        print("Culoarea curenta a cercului este:", self.culoare)  # Mov / Verde
        print("Raza cercului este:", self.raza)  # 5 / 32

    def aria(self):
        return math.pi * (self.raza * 2)

    def diametru(self):
        # Diametru d = 2 × r
        d = 2 * self.raza
        return d

    def circumferinta(self):
        # C = π × d = 2 × π × r
        c = 2 * math.pi * self.raza
        return c

# r = int(input("Dati raza cercului: "))
newCerc = Cerc(5, 'Mov')
newCerc.descrierecerc()
print("Aria Cercului:", round(newCerc.aria(), 6))  # 31.415927
print("Diametrul cercului:", (newCerc.diametru()))  # 10
print("Circumferinta cercului:", round(newCerc.circumferinta(), 2))  # 31.42
print('                ')

newCerc1 = Cerc(16, 'Verde')
newCerc1.descrierecerc()
print("Aria Cercului:", round(newCerc1.aria(), 6))
print("Diametrul cercului:", newCerc1.diametru())
print("Circumferinta cercului:", round(newCerc1.circumferinta(), 2))
print('>--------< 2 >-------<')
'''
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
'''
class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self, L, l):
        if L != l:
            return 'Laturi inegale'
        return 'Laturi egale'

    def aria(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


newDreptunchi = Dreptunghi(5, 5, 'Roz')
print("Aria dreptunghiului ", newDreptunchi.aria())  # 25
print('Perimetrul dreptunghi ', newDreptunchi.perimetrul())  # 20
print('Descriere ', newDreptunchi.descriere(5, 4))  # Laturi inegale
print('Are culoarea ', newDreptunchi.culoare)  # Roz
newDreptunchi.culoare = 'Lilo'
print('Culoare curenta ', newDreptunchi.culoare)  # Lilo
print('               ')
newDreptunchi1 = Dreptunghi(10, 11, 'Maro')
print('Aria dreptunghiului ', newDreptunchi1.aria())  # 110
print('Perimetrul dreptunghi ', newDreptunchi1.perimetrul())  # 42
print('Descriere ', newDreptunchi.descriere(12, 12))  # Laturi egale
print('Are culoarea ', newDreptunchi1.culoare)  # Maro
newDreptunchi1.culoare = 'Incolor'
print('Culoare curenta ', newDreptunchi1.culoare)  # Incolor
print('>--------< 3 >-------<')
'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''
class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self,):
        print('Angajatul are numele', self.nume_complet())
        print('Angajatul are salariul lunar de ', self.salariu, ' Lei')
        print('Angajatul are salariul anual de = ', self.salariu * 12)

    def nume_complet(self):
        nume_complet = self.nume + ' ' + self.prenume
        return nume_complet

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        return salariu_anual

    def marire_salariu(self, procent):
        marire_salariu = self.salariu * procent
        return marire_salariu

newAngajat1 = Angajat('Filip', 'Lucian', 3000)
newAngajat1.descriere()
print('Marire salariu lunar = ', newAngajat1.marire_salariu(0.3))
print('Marire salariu anual = ', newAngajat1.marire_salariu(0.3) * 12)
print('                     ')
newAngajat2 = Angajat('David', 'Popovici', 1000)
newAngajat2.descriere()
print('Marire salariu lunar = ', newAngajat2.marire_salariu(0.9))
print('Marire salariu anual = ', newAngajat2.marire_salariu(0.9) * 12)
print('Total salariu anual', newAngajat2.marire_salariu(0.9) * 12 + newAngajat2.salariu_anual())
print('|--------/ 4 \----------|')

'''
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
'''
class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self, suma):
        self.sold = self.sold - suma

    def creditare_cont(self, suma):
        self.sold = self.sold + suma

newCont1 = Cont('21RNC29RON20XXX', 'Filip Lucian', 20)
newCont1.afisare_sold() # Titularul Filip Lucian are in contul 21RNC29RON20XXX suma de 20 lei
newCont1.debitare_cont(10)
newCont1.afisare_sold() # Titularul Filip Lucian are in contul 21RNC29RON20XXX suma de 10 lei
newCont1.creditare_cont(20)
newCont1.afisare_sold() # Titularul Filip Lucian are in contul 21RNC29RON20XXX suma de 30 lei
print('                ')
newCont2 = Cont('22ROBT201XXX', 'S.C Navrom S.A', 1000)
newCont2.afisare_sold() # Titularul S.C Navrom S.A are in contul 22ROBT201XXX suma de 1000 lei
newCont2.debitare_cont(1000)
newCont2.afisare_sold() # Titularul S.C Navrom S.A are in contul 22ROBT201XXX suma de 0 lei
newCont2.creditare_cont(2000)
newCont2.afisare_sold() # Titularul S.C Navrom S.A are in contul 22ROBT201XXX suma de 2000 lei
print('------Optional 1 -----')

'''
Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
'''
'''
#pip install tabulate
from datetime import date
#from tabulate import tabulate
from pip._internal.utils.misc import tabulate

class Factura:
    seria = 123456

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def calc_total(self):
        return self.pret_buc * self.cantitate

    def genereaza_factura(self):
        print(tabulate([[self.nume_produs, self.cantitate, self.pret_buc, self.calc_total(), date.today()]],
                       headers=['Produs', 'Cantitate', 'Pret Buc', 'Total', 'Data']))

newFactura = Factura(123, 'Heets', 2, 10)
newFactura.genereaza_factura()
    # aici nu stiu cum sa mai repar, am luat codul din tema rezolvata si tot imi da eroare, nu ii convine de headers
    # o las asa nu mai pierd timpul cu ea
'''
'''
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0

'''
class Masina:
    marca = 'Dacia'
    model = None
    viteza_maxima = None
    viteza_actuala = None
    culoare = 'Gri'
    culori_disponibile = {'Alb', 'Mov', 'Galben', 'Verde', 'Indigo'}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descriere(self):
        print(f'Masina {self.marca}, model {self.model}, are o viteza maxima de {self.viteza_maxima} km/h \n'
              f'Aceasta se deplaseaza acum cu viteza de {self.viteza_actuala} km/h \n'
              f'Masina este de culoare {self.culoare}')

    def inmatriculare(self, inmatriculata):
        self.inmatriculata = inmatriculata

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
        else:
            print('Aceasta culoare nu este diponibila')
            pass

    def accelereaza(self, viteza):
        if viteza < self.viteza_maxima:
            self.viteza_actuala = viteza
        elif viteza < 0:
            print('EROARE!')
        else:
            self.viteza_actuala = self.viteza_maxima

    def franeaza(self):
        self.viteza_actuala = 0
        print(f'Viteza actuala este: {self.viteza_actuala}. Am oprit masina.')

newMasina1 = Masina('Logan', 200)
newMasina1.descriere()
'''
3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:

● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
'''
class ToDoList:
    dict = {}

    def adauga_task(self, nume_task, descriere_task):
        self.dict[nume_task] = descriere_task
        print('Am adaugat taskul cu succes')

    def finalizeaza_task(self, nume_task):
        del self.dict[nume_task]

    def afiseaza_todo_list(self):
        print(f'Task-urile din ToDoList sunt: {self.dict.keys()}')

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.dict:
            print(f'Detalii pt taskul {nume_task}: {self.dict[nume_task]}')
        else:
            print('Nu am gasit taskul dorit')
            raspuns = input('Vrei sa adaugi task ul in lista?')
            if raspuns.lower() == 'da':
                descriere_task = input('Introdu descrierea pentru noul task: ')
                self.dict[nume_task] = descriere_task
                print('Am adaugat taskul cu succes')
            elif raspuns.lower() == 'nu':
                print('La revedere!')

newTodoList = ToDoList()
newTodoList.afiseaza_detalii_suplimentare(' ')
