
import string

def compter_mots(phrase):
    # Ajoute la ponctuation propre à la langue française et quelques symboles Unicode courants
    ponctuation_etendue = string.punctuation + "«»—…“”‘’–"
    
    # Met tout en minuscules
    entree_utilisateur = str(phrase).lower()
    
    # Remplace toute la ponctuation par un espace
    table = str.maketrans({c: ' ' for c in ponctuation_etendue})
    texte_nettoye = entree_utilisateur.translate(table)
    
    # Normalise les espaces multiples et compte les mots
    texte_nettoye = " ".join(texte_nettoye.split())
    
    return texte_nettoye.split()


def mots_uniques (listemots):
#Compte le nombre d'occurrences de chaque mot dans une liste de mots.
    
    #Args:
        #listemots (list): Liste de mots à analyser.
        
    #Returns:
        #dict: Dictionnaire où les clés sont les mots et les valeurs
              #sont le nombre d'occurrences."""
    dicomots = {}
    for mots in listemots:
        if  (mots in dicomots):
            dicomots[mots]=dicomots[mots]+1
        else:
            dicomots[mots]=1
    dicomots_tries = dict(sorted(dicomots.items(), key=lambda x: x[1], reverse=True))
    return   dicomots_tries

# Utilisation
phrasebis = input("Entrez une phrase : ")
print(mots_uniques(compter_mots(phrasebis)))


# mots uniques est une version suggéré par chatgpt plus rapide et plus professionnelle du code que j'ai proposée précédemment
def mots_uniques_bis(listemots):
    """
    Compte le nombre d'occurrences de chaque mot et retourne un dictionnaire
    trié avec le mot le plus fréquent en premier.

    Args:
        listemots (list): Liste des mots à analyser.

    Returns:
        dict: Dictionnaire des mots et de leur fréquence, trié par fréquence décroissante.
    """
    # Utilisation de Counter pour compter facilement les occurrences
    compteur = Counter(listemots)

    # Trie le dictionnaire par fréquence décroissante
    dicomots_tries = dict(compteur.most_common())

    return dicomots_tries