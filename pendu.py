from random import *

def choisir_mot():
    liste_mots = ["Clavier", "Levier", "Poirier", "Fabian", "Sablier","Sudoku","Pizza","Petit","Eliott","Lilian","Agathe","Kelyan","Trousse"]
    mot = choice(liste_mots)
    return mot.lower()

def pendu(mot):

    #Cette fonction permet de jouer au jeu du pendu

    lettre_donne = set()
    print(lettre_donne)
    essaie = 6
    long=len(mot)

    while essaie > 0:
        # Afficher l'état actuel du mot caché
        mot_cache = ""
        for lettre in mot:
            if lettre in lettre_donne:
                mot_cache += lettre
            else:
                mot_cache += "_"
        print(mot_cache)

        # Demander une lettre
        tentative = input("Entrez une lettre : ").lower()

        # Vérifier si la lettre a déjà été devinée
        if len(tentative)>=2:
            if mot==tentative:
                print("Bravo! Vous avez deviné le mot!")
                return
        print(len(tentative))
        if tentative in lettre_donne:
            print("Vous avez déjà deviné cette lettre.")
            continue

        # Ajouter la lettre devinée à l'ensemble des lettres devinées
        lettre_donne.add(tentative)

        # Vérifier si la lettre est dans le mot à deviner
        if tentative in mot:
            print("Bonne devinette!")
             # Afficher l'état actuel du mot caché
            mot_cache = ""
            for lettre in mot:
                if lettre in lettre_donne:
                    mot_cache += lettre
                else:
                    mot_cache += "_"
            print(mot_cache)

            print(mot_cache)



        else:
            print("Mauvaise devinette.")
            essaie -= 1

        # Vérifier si tous les caractères ont été devinés
        if mot==mot_cache:
            print("Bravo! Vous avez deviné le mot!")
            return

        # Afficher le nombre de tentatives restantes
        print("Il vous reste {} tentatives.".format(essaie))

    # Si le joueur n'a plus de tentatives, afficher le mot à deviner
    print("Dommage! Le mot était {}.".format(mot))

# Programme principal
mot = choisir_mot()
pendu(mot)
