import nltk
nltk.download('punkt') 
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression

#données d'entrainement:
corpus = ["bonjour", "salut", "combien de pages pour le mémoire", "je ne sais pas rédiger une bibliographie", "je ne comprends pas", "à bientôt"]
intention = ["salutation", "salutation", "longueur mémoires", "données mémoires", "enseignant", "au_revoir"]
# fonction preprocessing qui nettoie le texte avant son traitement retire la ponctuation, les stopwords et met tout en minuscule
# fonction qui prend en argument un texte ou phrase et qui retourne un texte nettoyé sous la forme de str
def  preprocessing(phrase):
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
    # restranforme la liste de mots nettoyée en phrase
    return " ".join(reductiontexte)  

# fonction creer_vectorizer qui prend en argument une phrase et retourne une liste de vocabulaire appelée vectoizer contenant n features et un tuple x avec la forme sample, feautures
def creer_vectorizer(corpus, methode='tfidf'):
    """
    Crée un vectorizer (BoW ou TF-IDF) et retourne l'objet + la matrice de features.
    
    Args:
        corpus (list[str]): Liste de phrases à analyser.
        methode (str): 'bow' pour Bag of Words, 'tfidf' pour TF-IDF (par défaut).
    
    Returns:
        vectorizer: l'objet scikit-learn (CountVectorizer ou TfidfVectorizer)
        X (sparse matrix): Matrice des phrases vectorisées
    """
    if methode == 'bow':
        vectorizer = CountVectorizer()
    else:  # tfidf par défaut
        vectorizer = TfidfVectorizer()
    
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X
#la fonction transformer_phrase retourne une matrice qui compare les mots contenu dans le vocabulaire vectorizer aux mots de la phrase
# la matrice contient un tuple (nombre de sample testé ou nombre de documents ou liste, nbre de mots dans le vocabulaire ou features) ainsi que la correspondance des valeurs 0 ou 1
def transformer_phrase(vectorizer, phrase):
    """
    Transforme une nouvelle phrase en vecteur numérique à l'aide d'un vectorizer déjà entraîné.
    
    Args:
        vectorizer: Objet CountVectorizer ou TfidfVectorizer entraîné
        phrase (str): Phrase utilisateur à analyser
    
    Returns:
        vecteur (sparse matrix): Représentation vectorisée de la phrase
    """
    return vectorizer.transform([phrase])


#e fonction prediction_chat qui entraine le model et crée en argument un corpus d'entrainement sous forme de liste
#+ intention associées sous forme de liste+ phrases à predire et retourne la bonne intention
def prediction_chat(corpus, phrase, intention ):
    vec_corp,vx_corp= creer_vectorizer(corpus, methode='tfidf')
    X_new = transformer_phrase(vec_corp, phrase)
    model = LogisticRegression() # crée un modèle vide
    model.fit(vx_corp, intention)#associe phrases à une intention selon les données d'entrainement fournies
    return model.predict(X_new)

#fonction chatbot_response prend en argumenet une prédiction et retourne une str sous forme de réponse préécrite
def chatbot_response(prediction):



#tests
nouvelle_phrase = "aide moi à écire 10 pages pour mon mémoire"
print(prediction_chat(corpus, nouvelle_phrase, intention ))