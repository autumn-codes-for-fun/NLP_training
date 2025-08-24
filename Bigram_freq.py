import nltk
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
# ce code ne prend pas en compte les mots composées comem sous-branche ou les chiffres
def Bigram_Freq (phrase):
    #séparer les mots+ tout mettre en minuscule
    phraseminuscule= str(phrase).lower()
    listemots= word_tokenize(phraseminuscule) 
    # retirer les mots inutiles de la liste stopwords
    listeepuree=[]
    stopwords_list= stopwords.words('french')
    for token in listemots:
        if token not in stopwords_list:
              listeepuree.append(token)
    #verifier que les mots sont des mots nom des chiffres ou ponctuation
        mots_utiles = []
        for t in listeepuree:
            if t.isalpha():
                mots_utiles.append(t)
    # trouve les Bigrammes et les classes dans une liste
    listebigram=[]
    # attention ne prend pas en charge le cas ou 0 ou moins de 2 mots utiles entrée
    length= len(mots_utiles)
    if len(mots_utiles) < 2:
        return "veuillez reformuler votre question avec plus de mots"
    for i in range (length-1):
        tulpe= mots_utiles[i],mots_utiles[i+1]
        listebigram.append(tulpe)        
    # utilisation de freq pour compter les plus communs
    fdist = nltk.FreqDist(listebigram)
    return(fdist.most_common(5))
    
phrasetest = input("Entrez une phrase : ")
print(Bigram_Freq (phrasetest))

