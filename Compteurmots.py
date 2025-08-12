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
    
    return len(texte_nettoye.split())

# Utilisation
phrasebis = input("Entrez une phrase : ")
print("Nombre de mots :", compter_mots(phrasebis))