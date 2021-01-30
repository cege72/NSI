# coding: utf-8
from tkinter import *
fenetre = Tk()
label = Label(fenetre, text="Hello World")
label.pack()
Bouton_sortie = Button(fenetre, text="Quitter", command=fenetre.quit) Bouton_sortie.pack()
fenetre.mainloop()
