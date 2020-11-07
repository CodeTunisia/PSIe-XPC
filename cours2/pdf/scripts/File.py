class File:
    def __init__(self) :
        self.liste=[]
    def enfiler (self, v) :
        self.liste.append(v)
    def defiler(self) :
        if self.est_vide() == False:
              return self.liste.pop(0)
    def est_vide(self) :
        return self.liste == []
    def __repr__(self):
        return (str(self.liste))