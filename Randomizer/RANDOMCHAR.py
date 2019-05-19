import tkinter as tk
import time
from tkinter import *
import random
x = 10

root = Tk()
root.geometry("500x700")
root.title("Smash Ultimate Character Index")
root.grid
root.configure(background='#353332')
global name
global photo1
photo1 = PhotoImage(file="900.png")
name = ("no character yet")
# CHARACTER FUNTIONS BEGINING
def LUIGI():
    if (ooga == 1):
        print("LUIGI")
        global photo1
        photo1 = PhotoImage(file="LUIGI.png")
        global name
        name = ("LUIGI")
def WARIO():   
    if (ooga == 2):
        print("WARIO")
        global photo1
        photo1 = PhotoImage(file="WARIO.png")
        global name
        name = ("WARIO")
def KROOL():
    if (ooga == 3):
        print("KING K. ROOL")
        global photo1
        photo1 = PhotoImage(file="KROOL.png")
        global name
        name = ("KROOL")
# CHARACTER FUNTIONS END
                               

def gen():
    global ooga
    ooga = 0
    ooga = random.randint(1,3)
    LUIGI()
    WARIO()
    KROOL()
    Label(root, image=photo1, bg="#353332") .grid(row=2, column=2)
    Label (root, text=name, bg='white') .grid (row=1, column=1)
#ooga booga 

Button(root, text="Submit", command=gen) .grid(row=1, column=0,sticky=W)
root.mainloop()

#HAHHSHDSAHDSHDHSAD
#   sadsadadwaWdssadw 
    


