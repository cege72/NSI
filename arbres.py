class Arbre:
    def __init__(self,valeur):
        self.v=valeur
        self.fg=None
        self.fd=None
    def ajout_gauche(self,val):
        self.fg=Arbre(val)

    def ajout_droit(self,val):
        self.fd=Arbre(val)

    def affiche(self):
        """permet d'afficher un arbre"""
        if self==None:
            return None
        else :
            return [self.v,Arbre.affiche(self.fg),Arbre.affiche(self.fd)]
    def taille(self):
        if self==None:
            return 0
        else :
            return 1+Arbre.taille(self.fg)+Arbre.taille(self.fd)
    def hauteur(self):
        if self==None:
            return 0
        elif self.fg==None and self.fd==None:
            return 0
        else :
            return 1+max(Arbre.hauteur(self.fg),Arbre.hauteur(self.fd))
    def get_valeur(self):
        if self==None:
            return None
        else:
            return print(self.v)
