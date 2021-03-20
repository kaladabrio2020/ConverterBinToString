
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




def main(texto):#Transformar a palavras em lista de lista com letras
    lista_r = list()
    string  = texto.split("\n")

    for i in range(len(string)):
        new_lis = list()
        palavra = string[i]
        palavra = palavra.split()

        for e in range(len(palavra)):
            letras  = palavra[e] 
            separar = ' '.join(letras)
            separar = separar.split()
            new_lis.append(separar)
        lista_r.append(new_lis)   

    valor    = transformando_numero(lista_r)
    resultado = transformando_binaro(valor)
    return resultado


def transformando_numero(lista):#Transforma cada letra em numero 
    new_values = list()

    for i in range(len(lista)):
        nova = list()
        new_lista = lista[i]

        for e in range(len(new_lista)):
            nov_list = list()
            palavra  = new_lista[e]

            for x in range(len(palavra)):
                string = palavra[x]
                if string == None:
                    nov_list.append([])

                if string in letras_maiu:
                    y = letras_maiu.index(string)
                    nov_list.append(numero_maiu[y])
                
                if string in letras_minu:
                    y = letras_minu.index(string)
                    nov_list.append(numero_minu[y])
                
                if string in caracteres_sinais:
                    y = caracteres_sinais.index(string)
                    nov_list.append(numero_caractere[y])
                
                if string in caracteres_numerica:
                    y = caracteres_numerica.index(string)
                    nov_list.append(numero_carac_num[y])
            
            nova.append(nov_list)
        new_values.append(nova)
    return new_values



def transformando_binaro(lista):#Cria a frase em binario
    new_values = list()

    for i in range(len(lista)):
        new_list = list()
        lista_1  = lista[i]

        for e in range(len(lista_1)):
            dado = lista_1[e]
            if dado == None:
                new_list.append([])
            else:
                binario = transformado_binaro(dado)
                new_list.append(binario)
        new_values.append(new_list)
    
    return new_values

def transformado_binaro(valor):# Transforma em binario

    new_values = list()
    for i in range(len(valor)):
        numero = int(valor[i])
        numero = bin(numero)
        string = str(numero)
        string = string[2::]
        string = string[:3]+ "."+string[3:]
        new_values.append(string)
    return new_values
        