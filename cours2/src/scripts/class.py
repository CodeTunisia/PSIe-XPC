# Création de la classe CompteBancaire
class CompteBancaire:
    nomBanque = 'BIAT'	#Attributs de classe
    def __init__(self, nom, num_compte, montant_initial):
	# Attributs d'objet
        self.nom = nom
        self.no = num_compte
        self.sold = montant_initial

    # Méthodes
    def depot(self, montant):
        self.sold += montant
        
    def retrait(self, montant):
        if self.sold >= montant:
            self.sold -= montant
        else:
            raise Exception('retrait impossible')
    def decharge(self):
        s = "{}, {}, solde : {}".format(self.nom, self.no, self.sold)
        print(s)
