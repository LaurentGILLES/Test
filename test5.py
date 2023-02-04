#!/usr/bin/python3
#-*-coding:UTF-8-*

import sys

x = [('Laurent', 20), ('gilles', 40), ('Christine', 15)]

print(sorted(x, key=lambda x: x[1])) #La valeur du paramètre key doit être une fonction
#print(sorted(x, key=x[1])) provoque une erreur
