class Pile:
    def __init__(self) :
        self.liste=[]
    def empiler (self, v) :
        self.liste.append(v)
    def depiler(self) :
        if self.est_vide() == False:
            return self.liste.pop()
    def est_vide(self) :
        return self.liste == []
    def __repr__(self):
        return (str(self.liste))
