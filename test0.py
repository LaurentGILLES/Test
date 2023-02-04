#-*-coding:utf-8 -*

class ZDict:
    """Classe enveloppe d'un dictionnaire"""

    def __init__(self):
        """Notre classe n'accepte aucun paramètre"""
        self._dictionnaire = {}

    def __getitem__(self, index):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""
        print("__getitem__ pour la donnée d'index : {}".format(index))
        return self._dictionnaire[index]
        
    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
		On redirige vers self._dictionnaire[index] = valeur"""
        print("__setitem__ pour la donnée : {}".format(valeur))
        self._dictionnaire[index] = valeur

    def __delitem__(self, index):
        """Cette méthode permet de supprimer une donnée"""
        print("__delitem__ pour la donnée dont l'index est : {}".format(index))
        if index == "one":
            print("Impossible de supprimer one")
        else:
            del self._dictionnaire[index]

    def __contains__(self, item):
        """Cette méthode permet d'utiliser le mot clé in"""
        return self._dictionnaire.__contains__(item)

monDico = ZDict()
monDico["one"] = "un"
monDico["two"] = "deux"
monDico["three"] = "trois"

for cle, valeur in monDico._dictionnaire.items():
    print(cle, valeur)
print("Vous rechercher : {}".format(monDico["two"]))
del monDico["one"]
for cle, valeur in monDico._dictionnaire.items():
    print(cle, valeur)

print("one" in monDico)



# *****************************************************************
"""
dict = {"un":"one",
    "deux":"two",
    "trois":"three",
    "quatre":"four"}

dict["cinq"] = "five"
dict.pop("deux")

print(dict["un"])
for key in dict.keys():
    print(key)

try:
    print(dict["sept"])
except:
    pass

dico = {}
dico[1, 2] = "liste 1"
dico[3, 4] = "liste 2"
print(dico)
"""
# *****************************************************************
"""
def add(*param):
    param = list(param)
    nbr = 0
    for i, elem in enumerate(param):
        param[i] = int(elem)
        nbr = nbr + param[i]
    return nbr
    
print(add(1, 3, 6, 10) + 1)
"""
# *****************************************************************
"""
with open("loadlin.txt", "r") as fichier:
    texte = fichier.read()

liste = ["Laurent", "Christine", "Pierre-Aymeric", "Héloïse"]

newListe = [elem.upper() for elem in liste]

print("".join(newListe))

liste = texte.split(" ")
texte = "".join(liste)
liste = texte.split("\n")
texte = "".join(liste)
liste = texte.split("-")
texte = "".join(liste)
liste = texte.split(".")
texte = "".join(liste)
liste = texte.split("=")
texte = "".join(liste)
liste = texte.split(",")
texte = "".join(liste)

with open("loadlin.txt", "w") as fichier:
    fichier.write(texte)

print(texte)

fichier.close()
"""
# *****************************************************************
"""
List_Planetes = ["terre", "mars", "venus", "saturne", "jupiter"]
print(List_Planetes)
Text_Planetes = "\n".join(List_Planetes)
print(Text_Planetes)
Text_Planetes = "{}\nUranus".format(Text_Planetes)
# Text_Planetes = Text_Planetes + "\nUranus"
List_Planetes = Text_Planetes.split("\n")
print(List_Planetes)
for ele in List_Planetes:
    print(ele)
for ele in enumerate(List_Planetes):
    print(ele)
for i, ele in enumerate(List_Planetes):
    print(i)
    print(ele)
"""
# *****************************************************************
"""
def plusUn(a, b, c):
    a, b, c = a + 1, b + 1, c + 1
    return a, b, c

a, b, c = 5, 6, 7
print(a , b, c) # Affiche 5 6 7
plusUn (a, b, c)# Le passage de paramètres s'effectue toujours par copies
print(a , b, c) # Affiche 5 6 7
# En cas de besoin de mofifier les contenus des paramètres, on réaffecte
a, b, c = plusUn (a, b, c) # ces derniers avec le contenu du tuple résultat
print(a , b, c) # Affiche 6 7 8
"""
# *****************************************************************
