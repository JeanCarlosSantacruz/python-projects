#pruebas
#pregunta 2
def traducir(d,frase):
    f= ""
    for palabra in frase:
        if palabra in d:
            f+= (d[palabra])
            f+= " "
        else:
            f= "impossible"
            return f
    return f

def leerImprimir ():
    repeticiones= int(input())
    for veces in range (repeticiones):
        d= {}
        nPalabras= int(input())
        for i in range (nPalabras):
            pEsp= input()
            pIng= input()
            d[pEsp]=pIng
        frase= input().split()
        funcion= traducir(d,frase)
        print (funcion)

leerImprimir()


