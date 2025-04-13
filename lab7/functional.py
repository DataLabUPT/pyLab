"""Acest modul contine cod legat de programare functionala pentru

Limbaje de programare 3, Laborator 7, versiunea 1
de Bogdan Dragulescu, Razvan Vilceanu
https://datalab.upt.ro/cursuri/limbaje-de-programare-3/

Copyright 2025 Bogdan Dragulescu

Licenta: http://creativecommons.org/licenses/by/4.0/
"""

from utilfunc import p

# TODO 1: construiti un iterator din nrPrime si afisati elementele
nrPrime = (1, 3, 5, 7, 11, 13, 17, 19)


# TODO 2: sortati elementele dupa an utilizand o functie lambda
date = [(13, 12, 2015), (23, 5, 2016), (5, 7, 2017), (5, 3, 2015)]


# map
# TODO 3: calculati lungimea tuturor elementelor utilizand map
studenti = ['Birtalan Zsolt', 'Bujancă Ana-Maria', 'Drăgoescu Florentina',
           'Gaşpar Nicoleta-Larisa', 'Lovasz Evelyn-Astrid',
           'Mănescu Ionela-Claudia', 'Milici Alina-Simona',
           'Nicoară Octavian-Radu', 'Nicoraş Robert-Teofil',
           'Palfi Andreea-Sorina', 'Roman Camelia-Valentina',
           'Suditu Raul-Răzvan', 'Vălean  Ana-Maria', 'Vidoni Dan']


# TODO 4: din range(2, 6) obtineti [(2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]


# TODO 5: adunati vectorii range(2, 5), range(3, 9, 2)


# filter
# TODO 6: din studenti eliminati studenti transferati utilizand filter
transfer = ['Mănescu Ionela-Claudia', 'Palfi Andreea-Sorina', 'Vălean  Ana-Maria']


# reduce
# TODO 7: calculati factorial de 5 folosind reduce


# TODO 8: pentru un credit calculati restul de plata la final de an
# daca avem un credit de 1000, cu 4 plati trimestriale de 100 si o dobanda de 10% per an
credit = [1000, -100, -100, -100, -100]

