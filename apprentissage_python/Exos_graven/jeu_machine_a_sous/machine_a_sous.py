
import random 

print('Bienvenue sur la machine à sous ')
fruits = ['ananas','cerise','orange','pasteque','pomme_doree']
# choix aleatoire de plusieurs fruits - méthode 1
""" print(' Choix aléatoire - Méthode 1')
i = 0
while i < 3 :
    # choix aléatoire d'un fruit
    fruit_choisi = random.choice(fruits)

    print("Le fruit choisi est : ",fruit_choisi)

    i += 1 """

# choix aleatoire de plusieurs frutis - methode 2 
""" print(' Choix aléatoire - Méthode 2')
fruit_choisi = random.choices(fruits,k=3)
for i in fruit_choisi :
    print('Le fruit choisi est : ',i)
"""

# choix aleatoire des fruits avec une probabilité de choix 
import numpy as np
# Définir la probabilité de chaque outils
proba_fruits = [0.2,0.25,0.4,0.1,0.05] 
# Choix aléatoires de 3 fruits selon les probabilités choisies
selection = np.random.choice(fruits,3,p=proba_fruits)
gain = [50,15,5,150,10000]
fruit_gain = dict(zip(fruits,gain))
if selection[0] == selection[1] == selection[2] :
    jetons = fruit_gain[selection[0]]
    print(f' Des {selection[0]} ! Vous gagnez {jetons} jetons')
else :
    print(selection)
