#tarea 5
#Jean Carlos Santacruz
#Id: 8962275 

#pregunta 1

def imprimirNumeros():
    cont= 1
    while (cont<=100):
        if (cont%3!=0 and cont%4!=0):
            print (cont)
        cont += 1

# imprimirNumeros()

#pregunta 2
def revertir (lista):
    tope= len(lista)
    nuevaL= []
    while tope!= 0:
        nuevaL.append(lista[tope-1])
        tope-=1
    return nuevaL

# print (revertir([2,1,3,4]))

#pregunta 3

def obtenerOcurrencias (l,e):
    lista= []
    tamaño= len(l)
    cont= 0
    while cont < tamaño:
        if l[cont]== e:
            lista.append (cont)
        cont+= 1

    return lista

def leerImprimir ():
    repeticiones= int(input())
    cont= 0
    while cont < repeticiones:
        e= int(input())
        i= 0
        l= []
        cantidad= int(input())     #cantidad de numeros"
        while i < cantidad:
            n= int(input())        #numero a agregar
            l.append (n)
            i+= 1
        x= obtenerOcurrencias(l,e)
        print (x)
        cont+= 1

# leerImprimir()

#pregunta 4


def obtenerPuntosTorneo(torneo, equipoBusqueda):
    tamaño= len(torneo)
    puntosTotal = 0
    for partido in range (len(torneo)):
        partido= torneo[partido]
        if partido[0] == equipoBusqueda:
            if partido[1]>partido[3]:
                puntosTotal+= 3
            if partido[1]==partido[3]:
                puntosTotal+= 1
            if partido[1]<partido[3]:
                puntosTotal+= 0
        if partido[2] == equipoBusqueda:
            if partido[3]>partido[1]:
                puntosTotal+= 3
            if partido[3]==partido[1]:
                puntosTotal+= 1
            if partido[3]<partido[1]:
                puntosTotal+= 0
    
    return puntosTotal


# print(obtenerPuntosTorneo([["America", 3, "Cali", 0],
# ["Junior", 2, "America", 3],
# ["Santafe", 2, "Junior", 1],
# ["Cali", 2, "Junior", 2],
# ["America", 1, "Santafe", 1]],"Cali"))

#pregunta 5
def imprimir (lista):
    cont= 0
    cont1= 0
    while cont < len(lista):
        numero= lista[cont]
        if numero%2==0:
            while cont1 < lista[cont]:
                print ("*", end= " ")
                cont1+= 1
        elif numero%2!=0:
            while cont1 < lista[cont]:
                print ("+", end= " ")
                cont1+=1
        print ("")
        cont+= 1
        cont1= 0


def leerImprimir ():
    repeticiones= int(input())
    cont= 0
    while cont < repeticiones:
        i= 0
        lista= []
        cantidad= int(input())   #cantidad de numeros"
        while i < cantidad:
            n= int(input())      #numero a agregar
            lista.append (n)
            i+= 1
        cont+= 1
        x= imprimir(lista)

leerImprimir()



#pregunta 6
def obtenerMatriz (n):
    matriz= []
    cont= 0
    while cont < n:
        inicio= cont+1
        lista= []
        i= 0
        while i < n:
            lista.append (inicio)
            inicio+= n
            i+= 1
        matriz.append (lista)
        cont+=1
    return matriz

# print(obtenerMatriz(5))