from typing import BinaryIO
#from src.conversor.CaractereParaBinario import TransformandoBinario


LetrasMaiusculas = [
    'A','B','C','D','E','F','G',
    "H","I","J","K","L",'M','N',
    "O","P","Q","R","S","T","U",
    "V","W","X","Y","Z"
]

NumerosLetrasMaiusculas = [
    65,66,67,68,69,70,71,
    72,73,74,75,76,77,78,
    79,80,81,82,83,84,85,
    86,87,88,89,90
]


LetrasMinusculas=[
    "a","b","c","d","e","f","g",
    "h","i","j","k","l","m","n",
    "o","p","q","r","s","t","u",
    "v","w","x","y","z"
    ]

NumerosLetrasMinusculas = [
    97,98,99,100,101,102,103,
    104,105,106,107,108,109,
    110,111,112,113,114,115,
    116,117,118,119,120,121,122
    ]




caracteres_sinais=[
" ", "!", "''", "#", "$", "%", "&" , "´",
"(", ")", "*", "+", ",", "-", ".", "/",
":",";","<","=",">","?","@"]

NumeroDoCaracter = [
    32,33,34,35,36,37,38,39,
    40,41,42,43,44,45,46,47,
    58,59,60,61,62,63,64
]



CaracteresNumerica = [
    "0","1","2","3","4",
    "5","6","7","8","9"
]
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
    
    valor1 = TransformandoNumero(lista_r)
    valor2 = TransformandoLetra(valor1)
    return valor2



def TransformandoNumero(lista_r):
    valor = list()
    for i in range(len(lista_r)):
        lista = list()
        try :
            binario_list = lista_r[i]
        except IndexError:
            continue

        BinarioLista = lista_r[i]

        for e in range(len(binario_list)):
            binario = BinarioLista[e]
            binario = binario.split()
            lista_valor = numero(binario)
            lista.append(lista_valor)
            
        valor.append(lista)
    return valor 


def numero(x):
    lista_valor = list()

    for i in range(len(x)):
        dado      = x[i]
        resultado = int(dado,2)
        lista_valor.append(resultado)
    return lista_valor


def TransformandoLetra(numeros):
    ListaLetras = list()
    for e in range(len(numeros)):
        ListaNumeros = numeros[e]
        lista        = list()

        for i in range(len(ListaNumeros)):
            letras = Letrando(ListaNumeros[i])
            lista.append(letras)
        
        ListaLetras.append(lista)

    return ListaLetras




def Letrando(lista):
    resultado = None
    letras    = list()
    for numeros in lista:
        if numeros in NumerosLetrasMaiusculas:
            indice    = NumerosLetrasMaiusculas.index(numeros)
            resultado = LetrasMaiusculas[indice]

        elif numeros in NumerosLetrasMinusculas:
            indice    = NumerosLetrasMinusculas.index(numeros)
            resultado = LetrasMinusculas[indice]

        elif numeros in NumeroDoCaracter:
            indice    = NumeroDoCaracter.index(numeros)
            resultado = caracteres_sinais[indice]

        elif numeros in numero_carac_num:
            indice    = numero_carac_num.index(numeros)
            resultado = CaracteresNumerica[indice]

        else:
            resultado = '\0'

        letras.append(resultado)

    return letras
