import nltk
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


def Stemmer (phrase):
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
    # créer le stemmer
    stemmer= SnowballStemmer('french')
    # crée une liste de vocabulaire
    vocabulaire=[]
    for m in mots_utiles:
        vocabulaire.append(stemmer.stem(m))
    return vocabulaire
