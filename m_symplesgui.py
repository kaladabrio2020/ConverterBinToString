import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Txt, Window


def menu():

    sg.theme("DarkBlue2")
    parte_1 = [
        [sg.Checkbox(" Frase ====> Binario ",key='opcaoFB')],
        [sg.Checkbox(" Binario ==> Frase "  ,key='opcaoBF')],
    ]

    layout = [
        [sg.Frame(" Escolha ",layout=parte_1)],
        [sg.Ok(),sg.Cancel()]
    ]
    windows = sg.Window('Menu',layout=layout,resizable=True)
    return windows






def frase_bini():

    sg.theme("DarkBlue2")
    parte =  [ [sg.Multiline(key="Frase",size=(70,20))] ]

    layout = [
        [sg.Frame("  Frase => Binario  ",title_location="n",layout=parte)],
        [sg.Ok(),sg.Button('Voltar')]
    ]

    window = sg.Window("Janela 2",layout=layout,resizable=True)
    return window






def bin_frase():
    sg.theme("DarkBlue2")
    collun =  [  [sg.Image(r'Binario.gif')] ]

    parte_2 = [  [sg.Column(collun),sg.Multiline(key="Binario",size=(50,30))]   ]

    layout = [
        [sg.Frame("Binario => Frase\n Coloque um - entre as palavras.",parte_2,title_location="n")],
        [sg.Ok(),sg.Button('Voltar')]
    ]

    window = sg.Window("Janela 2",layout=layout,resizable=True)
    return window



def num_bin():
    sg.theme("DarkBlue2")
    layout = [
        [sg.Text("Digite um numero : "),sg.Input(key="Numero")],
        [sg.Ok(),sg.Button("Voltar")]
    ]
    window = sg.Window("janela 2",layout=layout,resizable=True)
    return window




def txt(inicio,valor):
    sg.theme("DarkBlue2")
    layout = [
        [sg.Multiline(inicio,size=(70,4))],
        [sg.Multiline(valor,size=(70,15))],
        [sg.Ok(),sg.Button('Voltar')] ]
    windows = sg.Window("Janela 3",layout=layout,resizable=True)
    return windows



def bin(inicio,valor):
    sg.theme("DarkBlue2")
    colun = [sg.MLine(inicio)]
    layout = [
        [sg.MLine(inicio,size=(70,3))],
        [sg.MLine(valor,size=(70,15)) ],
        [sg.Ok(),sg.Button('Voltar')]
    ]
    Windows = sg.Window('Janela 3',layout=layout)
    return Windows
