class Rectangle:
    # définir le constructeur avec des attributs : longueur et largeur 
    def __init__(self, longueur , largeur):
        self.longueur = longueur
        self.largeur = largeur
        
    # Créer une méthode perimetre
    def perimetre(self):
        return 2*(self.longueur + self.largeur)
    
    # Créer la méthode aire
    def aire(self):
        return self.longueur*self.largeur   
    
    # créer la méthode affiche
    def affiche(self):
        print("La longueur du rectangle est : ", self.longueur)
        print("La largeur du rectangle est : ", self.largeur)
        print("Le périmètre du rectangle est : ", self.perimetre())
        print("L'aire du rectangle est : ", self.aire())
        
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur , hauteur):
        # appel au constructeur de la super-classe de Parallelepipede :
        super().__init__(longueur, largeur)
        self.hauteur = hauteur
        
    # créer la méthode volume
    def volume(self):
        return self.longueur*self.largeur*self.hauteur
        
myRectangle = Rectangle(7 , 5)
myRectangle.affiche()
print("----------------------------------")
myParallelepipede = Parallelepipede(7 , 5 , 2)
print("Le volume de myParallelepipede es: " , myParallelepipede.volume())
