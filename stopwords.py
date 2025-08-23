import nltk
nltk.download('punkt') 
nltk.download('stopwords')
from nltk.corpus import stopwords
import string

def retrait_stopword(phrase):
    # Ajoute la ponctuation propre à la langue française et quelques symboles Unicode courants
    ponctuation_etendue = string.punctuation + "«»—…“”‘’–"
    
    # Met tout en minuscules
    entree_utilisateur = str(phrase).lower()
    
    # Remplace toute la ponctuation par un espace
    table = str.maketrans({c: ' ' for c in ponctuation_etendue})
    texte_nettoye = entree_utilisateur.translate(table)
        
    # Normalise les espaces multiples et compte les mots
    texte_nettoye = " ".join(texte_nettoye.split())
    texte_nettoye= texte_nettoye.split()
    
    #retire les stopwords
    reductiontexte=[]
    for word in  texte_nettoye:
        if word not in stopwords.words('french'):
            reductiontexte.append(word)

    return reductiontexte

phrasetest = input("Entrez une phrase : ")
print(retrait_stopword(phrasetest))