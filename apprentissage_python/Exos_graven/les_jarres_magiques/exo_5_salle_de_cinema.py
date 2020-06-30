from tkinter import *
from tkinter import messagebox
main = Tk()
main.title('Bienvenue au CInéma ! - Logiciel de Gestion de Cinéma')

# evenement sur la reservation 
def clic_reserver(choix,place):
    nb_place = films[choix-1]['place']
    if nb_place <= 0 :
        messagebox.showinfo(message="Le Film {} est complet ! Désolé".format(films[choix-1]['titre']))
        place.set('Film Complet !')
    else :
        films[choix-1]['place']  -= 1
        messagebox.showinfo(message="Achat Confirmé : Une place pour le film - {} : Bon Film !".format(films[choix-1]['titre']))
        place.set(films[choix-1]['place'])

films = [
{   "titre":"Voyage au centre du html",
    "horaire" : "15h45",   
    "place":14
},
{   "titre":"Les 9 jsons cachés", 
    "horaire" : "17h45",   
    "place":6
},
{   "titre":"Algobox - Le Film", 
    "horaire" : "13h45",   
    "place":3
}
    ]

Label(text="Bienvenue au cinema, voici les films a l'affiche :").grid(row=0, column = 1)
for index, film in enumerate(films,start=1) :
    numero = index
    titre = film['titre']
    heure = film['horaire']
    nbre_place = film['place']
    place_var = StringVar()
    place_var.set(nbre_place)
    titre_label = Label(main,text="{} - {} - {} ".format(numero,titre,heure))
    titre_label.grid(row=index+1, column = 1)
    place_label = Label(main,textvariable= place_var)
    place_label.grid(row=index+1, column = 2)
    reservation = Button(main, text='Reserver', command=lambda num = numero , pos = place_var: clic_reserver(choix = num,place=pos))
    reservation.grid(row=index+1, column=3)

quitter = Button(main, text='Quitter', command=main.quit)
quitter.grid(row=6, column=1)
main.mainloop()