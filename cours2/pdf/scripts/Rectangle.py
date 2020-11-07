class Rectangle:
    def __init__(self, longueur=30, largeur=15):
        self.L, self.l = longueur, largeur
        self.nom = "rectangle"
    def __str__(self):
        return "nom : {}".format(self.nom)

class Carre(Rectangle): # héritage simple
    """
    Sous-classe spécialisée de la super-classe Rectangle.
    """
    def __init__(self, cote=20):
        # appel au constructeur de la super-classe de Carre :
        super().__init__(cote, cote)
        self.nom = "carré" # surcharge d'attribut