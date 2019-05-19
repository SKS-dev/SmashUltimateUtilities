import tkinter as tk
import time
from tkinter import *
import random
import os 
x = 10
def opengen():
	os.system('RANDOMCHAR.py')


root2 = Tk()
root2.geometry("500x700")
root2.title("Smash Ultimate Utilities Menu")
root2.grid
root2.configure(background='#353332')
Button(root2, text="Random Character Generater", command=opengen) .grid(row=1, column=0,sticky=W)

root2.mainloop()