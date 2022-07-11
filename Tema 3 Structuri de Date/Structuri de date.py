'''
Tema 3
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 3 și ia notițe în caz că ți-a scăpat ceva.
2. Vizualizează din ‘Primii pași în Programare’ video

- Structuri de date

Astfel, la întâlnirea LIVE deja va fi a 2-a oară când vei auzi conceptele și sigur ți
se vor întipări în minte mai bine.
Link: https://www.itfactory.ro/8174437-intro-in-programare/
Exerciții obligatorii - grad de dificultate: Usor spre Mediu
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.

1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o:
'''
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
'''
● Inversează ordinea folosind slicing și suprascrie această listă.
'''
#invers = slice(-1 , -len(note_muzicale) -1, -1)
invers = note_muzicale[::-1]
note_muzicale = invers
'''
● Printează varianta actuală (inversată).
'''
print(note_muzicale)
'''
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
'''
note_muzicale.reverse()
'''
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
'''
print(note_muzicale)
'''
Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.

2. De câte ori apare ‘do’?
'''
print(f'"do " apare de {note_muzicale.count("do")} ori')
'''
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găseste 2 variante să le unești într-o singură listă.
'''
  # prima varianta cu o variabila ajutatoare
list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
list_3 = list_1 + list_2
print(list_3)
    # a doua varianta fara variabila ajutatoare
'''
list_1 = list_1 + list_2
print(list_1)

    # a treia varianta cu metoda de adaugare append()
list_1.append(list_2)
print(list_1)
'''
    # a patra varianta metoda extend care are scopul de a adauga elemente dintr-o lista in alta
list_1.extend(list_2)
print(list_1)
'''
4.
● Sortează și afișază lista generată la exercițiul anterior.
'''
list_3.sort()
print(list_3)
'''
● Sortează numărul 0 folosind o funcție.
'''
list_3.remove(0)

'''
● Afișaza iar lista.
'''
print(list_3)
'''
5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.
'''
if (not list_3):
    print('Lista este goala')
else:
    print('Lista nu este goala')
'''

6. Folosește o funcție care să șteargă lista de la exercițiul 3.
'''
list_3.clear()
'''
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
'''
if (not list_3):
    print('Lista este goala')
else:
    print('Lista nu este goala')
'''
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())
'''
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
'''

#print(f'Ana a luat nota {dict1["Ana"]}')
#print(f'Gigel a luat nota {dict1["Gigel"]}')
#print(f'Dorel a luat nota {dict1["Dorel"]}')
for key, value in dict1.items():
    print("Key : {} a luat nota  : {}".format(key, value))
'''

10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
'''
dict1["Dorel"] = 6
'''
● Printează nota după modificare
'''
print(f'Dupa contestatie nota lui Dorel este {dict1["Dorel"]}')
'''
11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
'''
dict1.pop("Gigel")
'''
● Vine un coleg nou. Adaugă Ionică, cu nota 9
'''
dict1["Ionica"] = 9
'''
● Printează noii elevi
'''
print(dict1)
'''
12.Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
'''
● Afișeaza zile_sapt
'''
print(zile_sapt)
'''
13.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
'''
if (weekend.issubset(zile_sapt)):
    print('Weekend este un subset al zilelor saptamanii')
'''
● Weekend nu este un subset al zilelor din săptămânii.
'''
if (not weekend.issubset(zile_sapt)):
    print('Weekend nu este un subset al zilelor săptămânii')
'''
14. Afișează diferențele dintre aceste 2 seturi.
'''
print('Diferenta dintre cele doua set-uri este ', zile_sapt.difference(weekend))
'''
15. Afișază intersecția elementelor din aceste 2 seturi.
'''
print('Intersectia celor doua set-uri este ', zile_sapt.intersection(weekend))
'''

Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
'''
jucatori = ['Andrei', 'Rafael', 'Domide', 'Stefan', 'Andone']
schimbari_max = 3
schimbariMaximAdmise = 3
schimbari_efectuate = 2
if (schimbari_efectuate < 0 or schimbari_efectuate >= schimbari_max):
    schimbariMaximAdmise -= 1
    schimbari_efectuate = schimbariMaximAdmise
    print('Nu sunt schimbari disponibile')
else:
    iesire = input("Tastati un jucator")
    intrare = 'Zare'
    if ('Andrei'in iesire or 'Rafael' in iesire or 'Domide' in iesire or 'Stefan' in iesire or 'Andone' in iesire):
        schimbariMaximAdmise -= 1
        schimbari_efectuate = schimbariMaximAdmise
        jucatori.remove(iesire)
        jucatori.append(intrare)
        print(f'a intrat {intrare} a ieșit {iesire} mai ai {schimbari_efectuate} schimbări')
        print(f'Noua lista de jucatori {jucatori}')
    else:
        schimbariMaximAdmise -= 1
        schimbari_efectuate = schimbariMaximAdmise
        print(f'nu se poate efectua schimbarea deoarece jucătorul {iesire} nu e în teren')
        print(f'Mai ai {schimbari_efectuate} schimbari')
'''
Testează codul cu diferite valori
teste:
Google search hint
“how to check if item îs în list python”
'''
