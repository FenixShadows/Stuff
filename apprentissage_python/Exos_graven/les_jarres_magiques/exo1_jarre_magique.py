import random
print("Bienvenue dans le jeu ! ")
print("Vous disposez de 5 jarres, Choisissez entre 1 et 5")

# Demander au joueur de mettre une valeur
while True :
    niveau = int(input('Choix du niveau du jeu : '))
    choix = int(input("Choix : "))
    choix -= 1
    jarre = ["clé","clé","clé","clé","serpent"]
    random.shuffle(jarre)
    print("Le joueur a mit la jarrre dans le numéro ",choix+1)
    resultat = jarre[choix]
    def decision(resultat):
        return "Victoire" if "clé" else "Défaite" 
    print("Résultat de la manche : ", decision(resultat))

