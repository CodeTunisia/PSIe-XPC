class Personne:
 
    # constructeur de la classe
    def __init__(self, nom, prenom):      
        self.nom = nom
        self.prenom = prenom
 
    def __del__(self): 
        print("je suis le destructeur")