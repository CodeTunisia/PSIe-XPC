def creer_pile():
    '''
    créer une pile (vide)
    '''
    return []

def empile(a,p):
    '''
    ajouter un élément au sommet de la pile
    '''
    p.append(a)
    
def depile(p):
    '''
    retirer le dernier élément ajouté
    '''
    return p.pop()
def sommet(p):
    '''
    donne le sommet de la pile
    '''
    return p[-1]

def hauteur(p):
    '''
    donne la hauteur de la pile
    '''
    return len(p)

def est_vide(p):
    '''
    vérifier si la pile est vide ou non
    '''
    return hauteur(p) == 0
