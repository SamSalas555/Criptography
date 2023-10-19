from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

root.geometry("400x400")
# Length and width window :D

cmb = ttk.Combobox(root, width="10", values=("prova","ciao","come","stai"))
# to create checkbox
# cmb = Combobox

#now we create simple function to check what user select value from checkbox

def checkcmbo():
     if cmb.get() == "prova":
        messagebox.showinfo("What user choose", "you choose prova")
    # if user select prova show this message 
    elif cmb.get() == "ciao":
        messagebox.showinfo("What user choose", "you choose ciao")

     # if user select ciao show this message 
    elif cmb.get() == "come":
        messagebox.showinfo("What user choose", "you choose come")

    elif cmb.get() == "stai":
        messagebox.showinfo("What user choose", "you choose stai")

    elif cmb.get() == "":
        messagebox.showinfo("nothing to show!", "you have to be choose something")


cmb.place(relx="0.1",rely="0.1")

btn = ttk.Button(root, text="Get Value",command=checkcmbo)
btn.place(relx="0.5",rely="0.1")

root.mainloop()