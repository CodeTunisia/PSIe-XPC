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
# Partie II
## Q1.
class ArticleEnPromo(Article):
    def __init__(self,ref, dsg, prix_a, remise):
        super().__init__(ref, dsg, prix_a)
        self.remise = remise
    ##Q2.
    def prix_ventePromo(self):
        return self.prix_vente() * (1-self.remise/100)
# Partie III
## Q1.
class Stock:
    def __init__(self):
        self.LS=[]
    ## Q2.
    def __repr__(self):
        ch=''
        for i in self.LS:
            ch += str(i[0])+':'+str(i[1])+'\n'
        return ch
    ## Q3. 
    def recherche_article(self, ref):
        for i in self.LS:
            if i[0].ref == ref:
                return i[0].dsg, i[0].prix_vente(), i[1]
            else:
                return None
    ## Q4.  
    def ajouter_article(self, article, qt):
        self.LS.append([article, qt])
    ## Q5.
    def maj_qtstock(self, ref, qt, type_maj):
        for i in self.LS:
            if i[0].ref == ref:
                if type_maj == 1:
                    i[1] += qt
                else:
                    i[1] -= qt
                break
    ## Q6.
    def supprimer_Articles(self, ref):
        for i in range(len(self.LS)):
            if self.LS[i][0].ref == ref:
                self.LS.pop(i)
    ## Q7.
    def articles_prix(self, p1, p2):
        L=[]
        for i in self.LS:
            pv = i[0].prix_vente()
            if pv >= p1 and pv <= p2:
                L.append(i[0])
        return L
    ## Q8.
    def articles_promo_qt(self,qt_min,remise):
        L=[]
        for i in self.LS:
            if i[1] < qt_min:
                x = ArticleEnPromo(i[0],remise)
                L.append((x, x.prix_vente(), x.prix_ventePromo()))
        return L
