import sys
import tkinter as tk
import tkinter.ttk as ttk
from   PIL import ImageTk, Image 

import src.conversor.BinarioParaCaractere as BinToChar
import src.conversor.ListaParaStrings     as Con
texto = '\
binario : 01101111 01101001 - 00100000 - 00101100 00100000 01101111 01101100 01100001\n\
convertido : oi , ola'

class BinarioParaCaractere:
    Binario    = None
    Back       = None
    convertido = None

    def __init__(self,master):
        self.Back = master
        self.Back.withdraw()
        self.master = tk.Toplevel()
        self.master.title('Binario para Caracteres')
        self.master.protocol("WM_DELETE_WINDOW", self.exit)
        self.master.geometry(f'+300+150')
        self.InputConversor()


    def InputConversor(self):
        FrameImage = ttk.Frame(self.master)
        FrameInput = ttk.Frame(self.master)
        FrameButto = ttk.Frame(FrameInput)

        image   = Image.open(r"static/img/Binario.png")
        display = ImageTk.PhotoImage(image)
        img     = tk.Label(FrameImage, image=display)
        img.image = display
        img.pack()

        ttk.Button(
            FrameImage,text = 'Exemplo',command=self.Exemplo,style="Accent.TButton"
        ).pack()

        self.Binario = tk.Text(FrameInput, width=45, height=28)
        self.Binario.pack(padx=10)
        
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
        FrameImage.grid(row=0,column=0)
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


    def Exemplo(self):
        exemplo = tk.Toplevel()
        exemplo.title('Exemplo')
        Texto = tk.Text(exemplo,width=40,height=10)
        Texto.insert('0.1',chars=texto)
        Texto.pack()

    
    def Convertendo(self):    
        ListaPalavras = BinToChar.main(self.Binario.get('1.0','end-1c'))
        TextoResult   = Con.string(ListaPalavras)
        self.convertido = tk.Toplevel()

        self.convertido.title('Resultado')
        Texto = tk.Text(self.convertido,width=40,height=10)
        Texto.insert('0.1',chars=TextoResult)
        Texto.pack()  
        