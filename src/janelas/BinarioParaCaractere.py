import sys
import tkinter as tk
import tkinter.ttk as ttk
from   PIL import ImageTk, Image  

class BinarioParaCaractere:
    def __init__(self,master):
        master.withdraw()
        self.master = tk.Toplevel()
        
        self.master.title('BinToChar')
        self.master.protocol("WM_DELETE_WINDOW", self.exit)
        self.master.geometry(f'+300+150')
        self.InputConversor()


    def InputConversor(self):
        FrameImage = ttk.Frame(self.master)
        FrameInput = ttk.Frame(self.master)

        image   = Image.open(r"static/img/Binario.png")
        display = ImageTk.PhotoImage(image)
        img     = tk.Label(FrameImage, image=display)
        img.image = display
        img.pack()

        TextInput = tk.Text(FrameInput, width=45, height=28)
        TextInput.pack(padx=10)
        
        FrameImage.grid(row=0,column=0)
        FrameInput.grid(row=0,column=1)

    def exit(self):sys.exit()
