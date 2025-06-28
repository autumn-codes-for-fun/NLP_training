mois = ['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre']
nbJours = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dico={}
for i in range(0, len(mois)):
    y= nbJours[i]
    x= (mois[i])
    dico={mois[i] : nbJours[i]}
    print("il y a",y, "jour dans", x)
