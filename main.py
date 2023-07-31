from os import popen
import sys
import time
import PySimpleGUI as sg
import m_symplesgui as p1
import Arquivo_txt  as atx
import M_Frase_Binario as fra_bin
import M_Binario_Frase as bin_fra


def main():

    janela = p1.menu()
    evento ,valor = janela.read()

    while True:
        janela.hide()

        if evento == "Cancel" or evento ==sg.WIN_CLOSED: break

        ListaOpcao = list(valor.values())

        if evento == "Ok":
            if   ListaOpcao.count(False) > 2:return main()
            elif ListaOpcao.count(True)  > 1:return main()

            if ListaOpcao[0] == True: frase()
            else:                     binario()
    sys.exit()

    



def frase():

    janela = p1.frase_bini()
    evento , valor = janela.read()

    while True:
        if evento == "Ok":
            janela.close()
            texto = valor["Frase"]
            tex_lis = texto.replace('\n','   (,)   ')
            lista_b = fra_bin.main(texto)
            valores = atx.string(lista_b)

            janela_3 = p1.txt(tex_lis,valores)
            evento_3,valor_3 = janela_3.read()
            if evento_3 == "Ok":
                janela.hide()
                return main()
            
            if evento_3 =='Voltar':
                janela_3.hide()
                return frase()
            
            if evento_3 == sg.WIN_CLOSED:
                janela_3.close()
                sys.exit()


        if evento == "Voltar":
            janela.hide()
            return main()
        
        if evento == sg.WIN_CLOSED:
            janela.close()
            sys.exit()











def binario():
    janela = p1.bin_frase()
    evento_3 , valor_3 = janela.read()

    while True:
        if evento_3 == "Ok":
            janela.hide()
            binario = valor_3['Binario']
            lista_letras = bin_fra.main(binario)
         
            string_palara = atx.bin(lista_letras)

            janela_3 = p1.bin(binario,string_palara)
            evento_4,valor_4 = janela_3.read()
            if evento_4 == 'Ok':
                janela_3.hide()
                return main()
            
            if evento_4 == 'Voltar':
                janela_3.hide()
                return binario()
            
            if evento_4 == sg.WIN_CLOSED:
                janela_3.hide()
                sys.exit()
    

        if evento_3 == "Voltar":
            janela.hide()
            return main()
        
        if evento_3 == sg.WIN_CLOSED:
            janela.close()
            sys.exit()


 









if __name__=='__main__':
    main()