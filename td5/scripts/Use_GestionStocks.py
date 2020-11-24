# Q9.
st1 = Stock()
st1.ajouter_article(Article(101, "stylot", 230.5), 120)
st1.ajouter_article(Article(102, "gaumme", 130.5), 260)
st1.ajouter_article(Article(103, "rapporteur", 430.5), 100)

st2 = Stock()
st2.ajouter_article(Article(101, "stylot", 230.5), 200)
st2.ajouter_article(Article(102, "gaumme", 130.5), 390)
st2.ajouter_article(Article(103, "rapporteur", 430.5), 410)
StockE = {1:st1, 2:st2}
print(StockE)

# Q10
while True :
    try:
        ref=int(input("donner la référence de l'article': "))
        break
    except : continue

    
    
qt_T = 0
for m in StockE:
    for i in StockE[m].LS:
        if i[0].ref==ref:
            print(m,':',i[1])
            qt_T += i[1]
print(f"La quantité totale de l'article N° {ref} dans nos magasins est {qt_T}")