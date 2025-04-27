"""Acest modul contine cod legat de exceptii, fisiere si serializarea datelor

Limbaje de programare 3, Laborator 8, versiunea 1
de Bogdan Dragulescu, Razvan Vilceanu
https://datalab.upt.ro/cursuri/limbaje-de-programare-3/

Copyright 2025 Bogdan Dragulescu

Licenta: http://creativecommons.org/licenses/by/4.0/
"""

from utilfunc import p
from itertools import groupby
import traceback

# TODO 1: trateaza exceptiile ce pot sa apara in program

# Deschide fisier pentru citire
# sursa fisier https://mail.python.org/pipermail/
fhand = open('2018-March.txt')

# extrage liniile ce incep cu FROM
liniiFrom = filter(lambda x: x.startswith('From '), fhand)

# extrage email
adrese = map(lambda x: x.split()[1], liniiFrom)

# agregare
adreseS = sorted(adresele)
adreseC = map(lambda x: (x[0], len(list(x[1]))), groupby(adreseS))

# ordonare dupa aparitii
adreseOrd = sorted(adreseC, key=lambda x: x[2], reverse=True)
p('Adrese ordonate dupa aparitii', adreseOrd)


# TODO 2: exporta adresele ordonate intr-un fisier JSON


# TODO 3: exporta adresele ordonate intr-un fisier csv


# TODO 4: exporta adresele ordonate intr-un fisier pickle

