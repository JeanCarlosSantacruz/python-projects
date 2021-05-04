# pregunta10()
def soundex ():
    lista= [["B","F","P","V"],["C", "G", "J", "K", "Q", "S", "X", "Z"],["D", "T"],["L"],["M", "N"],["R"]]
    palabra= input("digite la palabra: ")
    respuesta= ""
    tope= len(palabra)
    posicion= -1
    for letra in (palabra):
        posicion+=1
        cont= 1
        for subLista in lista:
            if letra in subLista:
                if posicion+1==tope:
                    respuesta+= str(cont)
                    break                                       
                elif not(palabra[posicion+1] in subLista):
                    respuesta+= str(cont)
                    break
                    
                                
            cont+=1        
    print (respuesta)
        
# soundex()

def soundex ():
    bloque1= [["B", "F", "P","V"],"1"]
    bloque2= [["C", "G", "J", "K", "Q", "S", "X", "Z"],"2"]
    bloque3= [["D", "T"],"3"]
    bloque4= [["L"],"4"]
    bloque5= [["M", "N"],"5"]
    bloque6= [["R"],"6"]
    palabra= input("digite la palabra: ")
    cont= 1
    respuesta= ""
    tope= len(palabra)
    j= 0
    for letra in palabra:
        if letra in bloque1[0]:
            if j+1==tope:
                respuesta+= bloque1[1]
            elif not(palabra[j+1] in bloque1[0]):
                respuesta+= bloque1[1]
        if letra in bloque2[0]:
            if j+1==tope:
                respuesta+= bloque2[1]
            elif not(palabra[j+1] in bloque2[0]):
                respuesta+= bloque2[1]
        if letra in bloque3[0]:
            if j+1==tope:
                respuesta+= bloque3[1]
            elif not(palabra[j+1] in bloque3[0]):
                respuesta+= bloque3[1]
        if letra in bloque4[0]:
            if j+1==tope:
                respuesta+= bloque4[1]
            elif not(palabra[j+1] in bloque4[0]):
                respuesta+= bloque4[1]
        if letra in bloque5[0] :
            if j+1==tope:
                respuesta+= bloque5[1]
            elif not(palabra[j+1] in bloque5[0]):
                respuesta+= bloque5[1]
        if letra in bloque6[0]:
            if j+1==tope:
                respuesta+= bloque6[1]
            elif not(palabra[j+1] in bloque6[0]):
                respuesta+= bloque6[1]
        if j<len(palabra)-1:
            j+=1
    print (respuesta)

soundex()