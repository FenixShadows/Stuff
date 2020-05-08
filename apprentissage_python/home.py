from tkinter import *
home = Tk()
home.title(' Bienvenue dans l application')
# Menu
# Configuration des onglets
menu = Menu(home)
# Premier onglet
menu1 = Menu(menu, tearoff=0)
menu1.add_command(label='option 1')
menu1.add_command(label='option 2')
menu1.add_command(label='option 3')
# Deuxième onglet
menu2 = Menu(menu,tearoff=0)
menu2.add_command(label='option 1')
menu2.add_command(label='option 2')
menu2.add_command(label='option 3')
# Insertion des onglets dans le menu
menu.add_cascade(label='Premier', menu=menu1)
menu.add_cascade(label='second', menu=menu2)
# Lancement de la fenêtre
home.config(menu = menu)
home.mainloop()
