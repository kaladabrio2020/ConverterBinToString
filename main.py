
import sys
import tkinter     as tk
import tkinter.ttk as ttk
import src.janelas.BinarioParaCaractere as BinToChar
#import janelas.BinarioParaCaractere as BinToChar


class Main:
    

    def __init__(self,root):
        self.master = root
        self.master.title('Home')
        self.master.tk.call('source','static/Azure-ttk-theme-main/azure.tcl')
        self.master.tk.call('set_theme','dark')
        self.master.protocol("WM_DELETE_WINDOW", self.exit)
        self.master.geometry(f'+500+280')

        self.Menu()

    def Menu(self):
        FrameMenu = ttk.Frame(self.master )
      
        ttk.Button(
            FrameMenu,text = 'Converter Binario',command = self.ConverterBinario,
            ).grid(row=0,column=0,sticky="nsew",padx=10,pady=5)
        
        ttk.Button(
            FrameMenu,text = 'Converter Caracter'
            ).grid(row=1,column=0,sticky="nsew",padx=10,pady=5)

        FrameMenu.pack()

        ttk.Button( 
            self.master,text='Sair',command = self.exit 
            ).pack(pady=5)

    def ConverterBinario(self) :BinToChar.BinarioParaCaractere(self.master)
    def ConverterCaracter(self):
        pass
    def exit(self):  sys.exit()
    def window(self):return self.master


if __name__=='__main__':  
    (Main(tk.Tk()).window()).mainloop()
    