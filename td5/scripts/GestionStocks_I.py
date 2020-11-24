# Partie I
## Q1
class Article:
    def __init__(self,ref,dsg,prix_a):
        self.ref=ref
        self.dsg=dsg
        self.prix_a=prix_a
    ##Q2.
    def __repr__(self):
        return f'({self.ref}, {self.dsg}, {self.prix_a})'
    ##Q3
    def set_article(self,type_modif,modif):
        if type_modif == 1:
            if type(modif) != int:
                raise ValueError('erreur de type')
            self.ref = modif
        elif type_modif == 2:
            if type(modif) != str:
                raise ValueError('erreur de type')
            self.dsg = modif
        elif type_modif == 3:
            if type(modif) != float:
                raise ValueError('erreur de type')
            self.prix_a = modif
    ##Q4
    def prix_vente(self,pourcentage=20):
        return self.prix_a*(1 + pourcentage/100)