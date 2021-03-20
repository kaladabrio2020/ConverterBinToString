
from typing import BinaryIO
from M_Frase_Binario import transformado_binaro


letras_maiu =[
'A','B','C','D','E','F','G',
"H","I","J","K","L",'M','N',
"O","P","Q","R","S","T","U",
"V","W","X","Y","Z"]
numero_maiu=[
65,66,67,68,69,70,71,
72,73,74,75,76,77,78,
79,80,81,82,83,84,85,
86,87,88,89,90]




letras_minu=[
"a","b","c","d","e","f","g",
"h","i","j","k","l","m","n",
"o","p","q","r","s","t","u",
"v","w","x","y","z"]
numero_minu=[
97,98,99,100,101,102,103,
104,105,106,107,108,109,
110,111,112,113,114,115,
116,117,118,119,120,121,122]




caracteres_sinais=[
" ", "!", "''", "#", "$", "%", "&" , "´",
"(", ")", "*", "+", ",", "-", ".", "/",
":",";","<","=",">","?","@"]

numero_caractere=[
32,33,34,35,36,37,38,39,
40,41,42,43,44,45,46,47,
58,59,60,61,62,63,64]



caracteres_numerica=[
"0","1","2","3","4",
"5","6","7","8","9"]
numero_carac_num=[
48,49,50,51,52,
53,54,55,56,57]


def main(binario):#Transformar a palavras em lista de lista com letras
    lista_r = list()
    string  = binario.split("\n")

    for i in range(len(string)):
        new_lis = list()
        palavra = string[i]
        palavra = palavra.split('-')

        for e in range(len(palavra)):
            letras  = palavra[e]
            new_lis.append(letras)
        lista_r.append(new_lis)  
    
    valor = transformando_numero(lista_r)
    valor_2 = transformando_letra(valor)
    return valor_2




def transformando_numero(lista_r):
    valor = list()
    for i in range(len(lista_r)):
        lista = list()

        try :
            binario_list = lista_r[i]
        except IndexError:
            continue
        binario_list = lista_r[i]

        for e in range(len(binario_list)):
            binario = binario_list[e]
            binario = binario.split()
            lista_valor = numero(binario)
            lista.append(lista_valor)
        valor.append(lista)
    return valor 





def numero(x):
    lista_valor = list()
    for i in range(len(x)):
        dado = x[i]
        resultado = int(dado,2)
        lista_valor.append(resultado)
    return lista_valor


def transformando_letra(numeros):
    lista_letras = list()
    for e in range(len(numeros)):
        lista_n = numeros[e]
        lista = list()
        for i in range(len(lista_n)):
            letras = letrando(lista_n[i])
            lista.append(letras)
        
        lista_letras.append(lista)

    return lista_letras




def letrando(lista):
    letras = list()
    for i in range(len(lista)):
        numeros = lista[i]

        if numeros in numero_maiu:
            x = numero_maiu.index(numeros)
            letras.append(letras_maiu[x])

        elif numeros in numero_minu:
            x = numero_minu.index(numeros)
            letras.append(letras_minu[x])

        elif numeros in numero_caractere:
            x = numero_caractere.index(numeros)
            letras.append(caracteres_sinais[x])

        elif numeros in numero_carac_num:
            x = numero_carac_num.index(numeros)
            letras.append(caracteres_numerica[x])
        else:
            letras.append('0')
    return letras  





