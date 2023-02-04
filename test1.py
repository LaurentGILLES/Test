#-*-coding:utf-8 -*

from tkinter import *
fenetre = Tk()
# Les cadres
cadre = Frame(fenetre, width=768, height=576, borderwidth=10)
cadre.pack(fill=BOTH)
# Les labels
champ_label = Label(cadre, text="Laurent GILLES")
champ_label.pack() # La méthode pack positionne un objet dans une fenêtre ou un cadre
# Les boutons
bouton_quitter = Button(cadre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack()
# Une ligne de saisie
var_texte = StringVar() # Création d’une variable texte Tkinter
ligne_texte = Entry(cadre, textvariable=var_texte, width=30)
ligne_texte.pack(side="top", fill=X)
# Les champs de texte
memo_texte = Text(cadre, width=60)
memo_texte.pack()
# Les cadres labellisés
cadre_lab = LabelFrame(cadre, text="Laurent GILLES")
cadre_lab.pack(fill=BOTH)
# Les cases à cocher
var_case = IntVar() # La variable integer Tkinter interrogeable par var_case.get()
case = Checkbutton(cadre_lab, text="Ne plus poser cette question", variable=var_case)
case.pack()
# Les boutons radio
var_choix = StringVar()
choix_rouge = Radiobutton(cadre_lab, text="Rouge", variable=var_choix, value="rouge")
choix_vert = Radiobutton(cadre_lab, text="Vert", variable=var_choix, value="vert")
choix_bleu = Radiobutton(cadre_lab, text="Bleu", variable=var_choix, value="bleu")
choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()

# Les listes déroulantes
liste = Listbox(cadre_lab)
liste.pack()
liste.insert(END, "Pierre")
liste.insert(END, "Feuille")
liste.insert(END, "Ciseau")
# si liste.curselection() renvoie ('2',), c'est Ciseau qui est sélectionné
fenetre.mainloop()