#!/usr/bin/python3
#-*-coding:UTF-8-*

import pickle
class stockObjet:
    def __init__(self, dico):
        self.dico = dico

    def montre(self):
        return self.dico

monDico = {"un":"one", "deux":"two", "trois":"three", "quatre":"four", "cinq":"five", "six":"six", "sept": "seven"}

#monStockObjet = stockObjet(monDico)

#print(monStockObjet.montre())
print(monDico)

r = input("r ou w ? ")

"""
if r == "r":
    with open("stock5.bin", "rb") as monFichier:
        monDePickler = pickle.Unpickler(monFichier)
        monStockObjet = monDePickler.load()
"""

if r == "r":
    with open("stockDico.bin", "rb") as monFichier:
        monDePickler = pickle.Unpickler(monFichier)
        monDico = monDePickler.load()

"""
if r == "w":
    with open("stock6.bin", "wb") as monFichier:
        monPickler = pickle.Pickler(monFichier)
        monPickler.dump(monStockObjet)
"""

if r == "w":
    with open("stockDico.bin", "wb") as monFichier:
        monPickler = pickle.Pickler(monFichier)
        monPickler.dump(monDico)

#print(monStockObjet.montre())
print(monDico)