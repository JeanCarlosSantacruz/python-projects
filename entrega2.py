#Jean Carlos Santacruz
#8962275
#Código de Honor
#Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali, los valores éticos y la integri-
#dad son tan importantes como la excelencia académica. En este curso se espera que los estudiantes se comporten ética
#y honestamente, con los más altos niveles de integridad escolar. En particular, se asume que cada estudiante adopta el
#siguiente código de honor:
#Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
#a seguir los más altos estándares de integridad académica.
#Integridad académica se refiere a ser honesto, dar crédito a quien lo merece y respetar el trabajo de los demás. Por eso
#es importante evitar plagiar, engañar, ‘hacer trampa’, etc. En particular, el acto de entregar un programa de computador
#ajeno como propio constituye un acto de plagio; cambiar el nombre de las variables, agregar o eliminar comentarios
#y reorganizar comandos no cambia el hecho de que se está copiando el programa de alguien más. Para más detalles
#consultar el Reglamento de Estudiantes, Sección VI.

#esta funcion se encarga de crear el mapa, recibe una lista con 2 valores (x,y) y con esos valores retorna el mapa
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

#esta funcion se encarga de cambiar de direccion al robot, recibe la letra (L,R) y de ahi define si debe sumar o restar hipoteticamente a la direccion. 
def direccion(listaPosI,comando):
    grados = listaPosI
    
    if (comando == 'L'):
        if(grados == 360):
            grados = 0
        grados += 90
    if (comando =='R'):
        if(grados == 0):
            grados = 360
        grados -= 90
    return grados

#esta funcion se encarga de mover al robot, si esta en 180,360 o 0 se mueve en x, y si esta en 90 o 270 se mueve en y, esa recibe la posicion actual y recibe el tamaño del mapa en y (el numero de sublistas) y el tamaño de cualquier sublista (todas tienen el mismo tamaño) , esto me sirve para ver si el robot se sale o no.
def moverse(listaPosI,lenx,leny):
    cad= ""
    posx = listaPosI[0]
    posy = listaPosI[1]
    grados = listaPosI[2]
    lista2 = [posx,posy,grados,'Lost']
    if (grados == 180):
        posx-= 1
    if (grados == 270):
        posy -=1
    if (grados == 90):
        posy+= 1
    if (grados == 360 or grados == 0):
        posx +=1
    lista = [posx,posy,grados]
    if(posx> leny or posy> lenx):
        lista = lista2
    else:
        lista = [posx,posy,grados]
    return lista

#esta funcion se encarga de ver la direccion en la que inicialmente se encuentra el robot, solo recibe una letra ([x,y,letra]) y lo que hace es comparar la letra y asignarle el valor correspondiente.
def coordenadaInicial(listaI):
    grados = 0

    if( listaI[2] == 'E'):
        grados= 360
    if ( listaI[2] == 'W'):
        grados= 180
    if( listaI[2] == 'N'):
        grados= 90
    if ( listaI[2] == 'S'):
        grados= 270

    return grados

#esta funcion se encarga de convertir la lista en la que tengo la informacion de la posicion final del robot a cadena, solo recibe esta lista y la convierte a cadena, cuenta con una condicion por si el robot se salio del limite.
def convertir( listaInicial):
    grado =''
    if listaInicial[2] == 0 or listaInicial[2] ==360:
        grado = 'E'
    if listaInicial[2] == 270:
        grado = 'S'
    if listaInicial[2] == 180:
        grado = 'W'
    if listaInicial[2] == 90:
        grado = 'N'
    cadena = str(listaInicial[0])+' '+str(listaInicial[1])+' '+grado

    if len(listaInicial) == 4:
        cadena +=' '+'LOST'
    return cadena

#esta funcion se encarga de leer los datos ingresados por el usuario y convertirlos a los que sea necesario (cadenas, listas etc) para posteriormente usarlos en las funciones que se llaman durante la ejecucion, tambien se encarga de la cantidad de veces que se va a ejecutar el codigo
def leerImprimir ():
    valores= input().split()
    tamañoMapa= []
    cont= 0
    while cont < len(valores):
        tamañoMapa.append(int(valores[cont]))
        cont+= 1
    mapa= crearMapa (tamañoMapa)
    valores= input().split()
    bloqueos=[]
    while valores != []:
        posInicial= []
        
        cont2= 0
        tamaño= len(valores)
        while cont2 < tamaño-1:
            posInicial.append(int(valores[cont2]))
            cont2+= 1
        posInicial.append(valores[cont2])
        instrucciones= input()
        posInicial[2]= coordenadaInicial(posInicial)

        for i in instrucciones:
            if ( i == 'R'  or i == 'L'):
                posInicial[2]=  direccion(posInicial[2],i)
            else:
                posInicial = moverse(posInicial,len(mapa)-1,len(mapa[0])-1)
                if len(posInicial) == 4 and not((posInicial[0],posInicial[1]) in bloqueos):
                    bloqueos.append((posInicial[0],posInicial[1]))
                    break
            
            
        print (convertir(posInicial))
    
            
        
        valores= input().split()


leerImprimir ()




