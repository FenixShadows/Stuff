# Importation des modules
from tkinter import *
from tkinter import messagebox,
# Bloc initial
main = Tk()
mainframe = Frame(main, width = 300, height = 200, borderwidth = 1)
# Variables de saisie
identifiant = StringVar()
password = StringVar()
# Evenements des boutons
def recup_identifiant(*args):
    identifiant.get()
# Creation des objets de la fenetre
acceuil = Label(main, text='Identifiez vous !')
main.title('Mon Premier Programme en Python')
id_text = Label(main, text='Identifiant')
pass_text = Label(main, text='Mot de passe')
entree_id = Entry(main, width = 25, exportselection = 0, textvariable = identifiant)
entree_pass = Entry(main, width = 25, show ='*', exportselection=0, textvariable = password)
bouton_con = Button(main, text='Entrer')
bouton_quit = Button(main, text='Fermer', command = main.destroy)
# Disposition des objets
acceuil.grid(row = 1, column = 2)
id_text.grid(row = 2, column = 1)
entree_id.grid(row = 2, column = 2)
pass_text.grid(row = 3, column = 1)
entree_pass.grid(row = 3, column = 2)
bouton_con.grid(row = 4, column = 2)
bouton_quit.grid(row = 4, column = 3)
# Lancement de la fenetre
main.minsize(640,280)
main.mainloop()
