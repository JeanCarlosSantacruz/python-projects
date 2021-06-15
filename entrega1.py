#Jean Carlos Santacruz
#8962275
#Entrega 1

def crearMapa (tamañoMapa):
    mapa= []
    for y in range (tamañoMapa[1]+1):
        cont= 0
        subLista= []
        while cont < (tamañoMapa[0]+1):
            subLista.append(0)
            cont+=1
        mapa.append(subLista)
    return (mapa)

# leerImprimir()

def leerImprimir ():
    repeticiones= int(input())
    valores= input().split()
    tamañoMapa= []
    cont= 0
    while cont < len(valores):
        tamañoMapa.append(int(valores[cont]))
        cont+= 1
    for i in range(repeticiones):
        valores= input().split()
        posInicial= []
        cont2= 0
        tamaño= len(valores)
        while cont2 < tamaño-1:
            posInicial.append(int(valores[cont2]))
            cont2+= 1
        posInicial.append(valores[cont2])
        # print (posInicial)
        instrucciones= input()
        # print (instrucciones)
        mapa= crearMapa (tamañoMapa)
        print (mapa)

# leerImprimir ()

