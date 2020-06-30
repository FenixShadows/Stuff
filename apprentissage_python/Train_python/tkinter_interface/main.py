from _ast import Lambda
from tkinter import *

main = Tk()
main.title("Ma calculation")


def execution(number):
    champ.insert(0, str(champ.get())+str(number))


def clear():
    champ.delete(0, 'end')

champ = Entry(main, borderwidth=5)
champ.grid(row=0, column=0, columnspan=3, pady=20)


button1 = Button(main, text="1", padx=20, pady=20, command= lambda : execution(1))
button1.grid(row=1, column=0)
button2 = Button(main, text="2", padx=20, pady=20, command=lambda: execution(2))
button2.grid(row=1, column=1)
button3 = Button(main, text="3", padx=20, pady=20, command=lambda: execution(3))
button3.grid(row=1, column=2)
button4 = Button(main, text="4", padx=20, pady=20, command=lambda: execution(4))
button4.grid(row=2, column=0)
button5 = Button(main, text="5", padx=20, pady=20, command=lambda: execution(5))
button5.grid(row=2, column=1)
button6 = Button(main, text="6", padx=20, pady=20, command=lambda: execution(6))
button6.grid(row=2, column=2)
button7 = Button(main, text="7", padx=20, pady=20, command=lambda: execution(7))
button7.grid(row=3, column=0)
button8 = Button(main, text="8", padx=20, pady=20, command=lambda: execution(8))
button8.grid(row=3, column=1)
button9 = Button(main, text="9", padx=20, pady=20, command=lambda: execution(9))
button9.grid(row=3, column=2)
button0 = Button(main, text="0", padx=20, pady=20, command=lambda: execution(0))
button0.grid(row=4, column=1)
button_plus = Button(main, text="+", padx=20, pady=20, command=execution)
button_plus.grid(row=4, column=0)
button_solve = Button(main, text="=", padx=20, pady=20, command=execution)
button_solve.grid(row=4, column=2)
button_reset = Button(main, text="Reset", padx=20, pady=20, command=clear())
button_reset.grid(row=5,  columnspan=3)
main.mainloop()
