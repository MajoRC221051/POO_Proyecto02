import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import*



fondo_entrar = "#7CBD7D"



ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("1000x600")
ventana.resizable(width=False, height=False)
bg = tk.PhotoImage(file="PI4.png")
bg1 = tk.Label(ventana, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
username = StringVar()
contraseña = StringVar()
entrada_username=Entry(bg1, textvariable=username,width=29,bd=0,font=("League Spartan",15))
entrada_username.place(x=70,y=270)
entrada_contraseña = Entry(bg1,textvariable=contraseña,width=29,bd=0,font=("League Spartan",15),show="*")
entrada_contraseña.place(x=70,y=360)
Button(bg1,text="Ingresar", cursor="hand2",bg= fondo_entrar,  width = 39,pady = 10,  relief = "flat", border = 0, font = ("League Spartan",12)) .place(x=50,y=435)


ventana.mainloop()






