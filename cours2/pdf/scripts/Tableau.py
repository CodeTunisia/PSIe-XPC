class Tableau:
    donnee=[]
    # constructeur de la classe
    def __init__(self):
        #initialiser le tableau avec 100 éléments
        self.donnee=[0]*100

    def __del__(self):
        print("je suis le destructeur")
        # vider le tableau
        self.donnee.clear()