import tkinter as tk
import tkinter.ttk as ttk


import sys
import tkinter as tk
import tkinter.ttk as ttk
from   PIL import ImageTk, Image 

import src.conversor.CaractereParaBinario as CharToBin
import src.conversor.ListaParaStrings     as Con
texto = '\
binario : 01101111 01101001 - 00100000 - 00101100 00100000 01101111 01101100 01100001\n\
convertido : oi , ola'

class CaractereParaBinario:
    Caracteres = None
    Back       = None
    convertido =  None


    def __init__(self,master):
        self.Back = master
        self.Back.withdraw()
        self.master = tk.Toplevel()
        self.master.title('Caracteres para Binario')
        self.master.protocol("WM_DELETE_WINDOW", self.exit)
        self.master.geometry(f'+500+150')
        self.InputConversor()


    def InputConversor(self):
        FrameInput = ttk.Frame(self.master)
        FrameButto = ttk.Frame(FrameInput)

        self.Caracteres = tk.Text(FrameInput, width=45, height=28)
        self.Caracteres.pack(padx=10)
        
        ttk.Button(
            FrameButto,text = 'Converter',
            command = self.Convertendo,
            style   = "Accent.TButton"
        ).grid(row=0,column=0,padx=5)

        ttk.Button(
            FrameButto,text = 'Voltar',
            command = self.back,
            style   = "Accent.TButton"
        ).grid(row=0,column=1,padx=5)

        FrameButto.pack()
        FrameInput.grid(row=0,column=1)

    def exit(self):
        sys.exit()

    def back(self):
        try:
            self.convertido.withdraw()
            self.master.withdraw()
            self.Back.deiconify()

        except Exception:
            self.master.withdraw()
            self.Back.deiconify()

    
    def Convertendo(self):
        ListaPalavras = CharToBin.main(self.Caracteres.get('1.0',tk.END))
        TextoResult   = Con.bin(ListaPalavras)

        self.convertido = tk.Toplevel()
        self.convertido.title('Resultado')
        Texto = tk.Text(self.convertido,width=40,height=10)
        Texto.insert('0.1',chars=TextoResult)
        Texto.pack()  
        