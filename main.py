from os import popen
import sys
import time
import PySimpleGUI as sg
import m_symplesgui as p1
import Arquivo_txt  as atx
import M_Frase_Binario as fra_bin
import M_Binario_Frase as bin_fra


def main():

    jan_1 = p1.menu()
    evento_1,valor_1 = jan_1.read()

    while True:
        jan_1.hide()
        if evento_1 == "Cancel" or evento_1 ==sg.WIN_CLOSED:
            jan_1.close()
            break

        if evento_1 == "Ok":
            if valor_1.count(False) > 2:
                return main()
            if valor_1.count(True) > 1:
                return main()
            
            if valor_1[0] == True:
                frase()
            
            if valor_1[1] == True:
                binario()
    sys.exit()

    



def frase():

    jan_2 = p1.frase_bini()
    evento_2 , valor_2 = jan_2.read()

    while True:
        if evento_2 == "Ok":
            jan_2.close()
            texto = valor_2["Frase"]
            tex_lis = texto.replace('\n','   (,)   ')
            lista_b = fra_bin.main(texto)
            valores = atx.string(lista_b)

            jan_3 = p1.txt(tex_lis,valores)
            evento_3,valor_3 = jan_3.read()
            if evento_3 == "Ok":
                jan_2.hide()
                return main()
            
            if evento_3 =='Voltar':
                jan_3.hide()
                return frase()
            
            if evento_3 == sg.WIN_CLOSED:
                jan_3.close()
                sys.exit()


        if evento_2 == "Voltar":
            jan_2.hide()
            return main()
        
        if evento_2 == sg.WIN_CLOSED:
            jan_2.close()
            sys.exit()











def binario():
    jan_2 = p1.bin_frase()
    evento_3 , valor_3 = jan_2.read()

    while True:
        if evento_3 == "Ok":
            jan_2.hide()
            binario = valor_3['Binario']
            lista_letras = bin_fra.main(binario)
            print(lista_letras)
            string_palara = atx.bin(lista_letras)

            jan_3 = p1.bin(binario,string_palara)
            evento_4,valor_4 = jan_3.read()
            if evento_4 == 'Ok':
                jan_3.hide()
                return main()
            
            if evento_4 == 'Voltar':
                jan_3.hide()
                return binario()
            
            if evento_4 == sg.WIN_CLOSED:
                jan_3.hide()
                sys.exit()
    

        if evento_3 == "Voltar":
            jan_2.hide()
            return main()
        
        if evento_3 == sg.WIN_CLOSED:
            jan_2.close()
            sys.exit()


 









if __name__=='__main__':
    main()