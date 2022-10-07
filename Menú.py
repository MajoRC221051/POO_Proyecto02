class App(Tk):
    def __init__(self):
        super().__init__()

    # Configura la venta Principal
        self.title("Registro")
        self.geometry("950x1000")
        self.resizable(False, False)
        self.bg = PhotoImage(file="Mentally (1000 × 1000 px) (800 × 1000 px) (950 × 1000 px).png")
        self.bg1 = Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
    


    # Creación de botones
        self.foto = PhotoImage(file = "B4.png")
        self.button = tk.Button(self,  image = self.foto, borderwidth=0, highlightthickness=0)
        self.button.place(x=40, y=420)
        self.label1 = Label(self, text = "Alegrate", fg = "black", font = ("League Spartan bold", 16)).place(x=780, y=640)
        
        self.foto2 = PhotoImage(file = "11.png")
        self.button2 = tk.Button(self,  image = self.foto2, borderwidth=0, highlightthickness=0)
        self.button2.place(x=260, y=420)
        self.label2 = Label(self, text = "Regresa", fg = "black", font = ("League Spartan bold", 16)).place(x=550, y=640)
        
        self.foto3 = PhotoImage(file = "B3.png")
        self.button3 = tk.Button(self,  image = self.foto3, borderwidth=0, highlightthickness=0)
        self.button3.place(x=700, y=420)
        self.label3 = Label(self, text = "Relajate", fg = "black", font = ("League Spartan bold", 16)).place(x=303, y=640)
        
        self.foto4 = PhotoImage(file = "B1 (210 × 210 px).png")
        self.button4 = tk.Button(self,  image = self.foto4, borderwidth=0, highlightthickness=0)
        self.button4.place(x=478, y=420)
        self.label4 = Label(self, text = "Duermete", fg = "black", font = ("League Spartan bold", 16)).place(x=100, y=640)
        
        self.button = Button(self,text="Ver estadísticas", bg = "black", fg = "white", width = 25, pady = 7,  relief = "flat", border = 0, font = ("League Spartan",12)) .place(x=500,y=310)
  
app = App()
app.mainloop()
