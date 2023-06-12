import tkinter as tk


class Aplication(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #Datos programa
        self.PrecioSinIVA = tk.DoubleVar()
        self.IVA = tk.DoubleVar()
        self.PrecioIVA = tk.DoubleVar()
        self.valorI = tk.DoubleVar()
        self.valorI.set(0.21)
        self.band = tk.IntVar()
        
        #Atributos ventana
        self.geometry("300x500")
        self.title("Cálculo de IVA")
        
        #Atributos generales
        opts = {"padx": 5, "pady": 5,"ipadx":10, "ipady": 10}
        
        #Labels
        
        precioSI = tk.Label(self, text = "Precio sin IVA")
        precioSI.grid(row = 1, column = 0, **opts)
        
        IVA = tk.Label(self, text = "Valor IVA")
        IVA.grid(row = 6, column = 0, **opts)
        
        precioCI = tk.Label(self, text = "Precio con IVA")
        precioCI.grid(row = 7, column = 0, **opts)
        
        
        #RadioButtons
        
        IVA21 = tk.Radiobutton(text = "IVA 21 %", value = 0, variable = self.band, command = self.cambiaValorI)
        IVA21.grid(row = 4, column = 0)
        
        IVA10 = tk.Radiobutton(text = "IVA 10 %", value = 1, variable = self.band, command = self.cambiaValorI)
        IVA10.grid(row = 5, column = 0)

        #Entrys
        
        entry_precioSin_IVA = tk.Entry(textvariable = self.PrecioSinIVA)
        entry_precioSin_IVA.grid(row = 1, column = 1, **opts)
        
        entry_IVA = tk.Entry(textvariable = self.IVA)
        entry_IVA.grid(row = 6, column = 1, **opts)
        
        entry_precioCon_IVA = tk.Entry(textvariable = self.PrecioIVA)
        entry_precioCon_IVA.grid(row = 7, column = 1, **opts)        
        
        
        
        
        
        
        
        
        
        #Botones
        
        
        calcula = tk.Button(self, text="Calcular", command = self.calcula)
        salir = tk.Button(self, text = "Salir", command = self.salir)
        
        calcula.grid(row = 8, column = 0, **opts)
        salir.grid(row = 8, column = 1, **opts)
        
        self.mainloop()
        
    def cambiaValorI(self):
        if self.band.get()==0:
            self.valorI.set(0.21)

        elif self.band.get() == 1:
            self.valorI.set(0.105)

        
    def salir(self):
        self.destroy()
        
    def calcula(self):
        self.PrecioIVA.set(self.PrecioSinIVA.get() * self.valorI.get() + self.PrecioSinIVA.get())
        self.IVA.set(self.PrecioSinIVA.get() * self.valorI.get())
