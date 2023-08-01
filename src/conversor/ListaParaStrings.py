def string(binario):
    texto = ''
    for i in range(len(binario)):
        x = binario[i]
        if x == []:
            texto = texto +" "
        
        for e in range(len(x)):
            string = x[e]
            string = " ".join(string)

            if not(e == len(x)-1):
                string = string + " "
            texto = texto + string 
        texto += "\n"
    return texto


def bin(binario):
    texto =' '
    for i in range(len(binario)):
        x = binario[i]
        if x == [[]]:
            texto = texto + '\n'
        
        for e in range(len(x)):
            
            string = x[e]
            string = " ".join(string)
            texto += string + ' '
    
    return texto
