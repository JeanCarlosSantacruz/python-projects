#tarea 5
#Jean Carlos Santacruz
#Id: 8962275

#pregunta 1
def guardarNumeros (l,r):
    f= []
    for i in range(l,r+1):
        if (i%3!=0 and i%4!=0):
            f.append (i)
    return f

def leerImprimir ():
    repeticiones= int(input())
    i= 0
    while i<repeticiones:
        l= int(input())
        r= int(input())
        ans= guardarNumeros(l,r)
        i+=1
        print (ans)
    
#leerImprimir()

#pregunta 2 
def lista_Tupla (l): 
    cont= 0
    tamList= len(l)
    menor= l[cont]
    mayor= l[cont]  
    while cont < tamList:
        n = l[cont]
        if n<menor:
            menor= n
        if n> mayor:
            mayor= n
        cont+=1
    tupla= (menor,mayor)
    return tupla

def leerImprimir():
    repeticiones= int(input())
    i= 0
    while i<repeticiones:
        i+=1
        tamaño= int(input())
        l= []
        cont= 0
        while cont<tamaño:
            numero= int(input())
            l.append (numero)
            cont+=1
        ans= lista_Tupla(l)
        print (ans)

# leerImprimir()

#pregunta 3
def reverse ():
    cont= 0
    i= 0
    lis= []
    repeticiones= int(input())
    while cont < repeticiones: 
        cont+=1
        tamaño= int(input())
        while i<tamaño:
            numero= int(input())
            lis.append (numero)
            i+=1
        lisFinal= []    
        while tamaño!= 0:
            lisFinal.append(lis[tamaño-1])
            tamaño-=1
    return lisFinal
    x= revertir(lis)

# print(reverse())

#pregunta 4
def cuadrantes(lx,ly):
    maximo= len(lx)
    lc= []
    cont= 0
    i= 1   
    while i<=maximo:
        if lx[cont]>0 and ly[cont]>0:
            lc.append (1)
        
        if lx[cont]<0 and ly[cont]>0:
            lc.append (2)
              
        if lx[cont]<0 and ly[cont]<0:
            lc.append (3)
             
        if lx[cont]>0 and ly[cont]<0:
            lc.append (4)
        cont+=1
        i+= 1
    
    return lc

def leerImprimir():
    repeticiones= int(input("repeticiones: "))
    i= 0
    while i<repeticiones:
        cont= 0
        i+=1
        l1= []
        l2= []
        d= int(input("digitos: "))
        while cont<d:
            numero= float(input("numero: "))
            l1.append (numero)
            cont+=1
        cont= 0
        while cont<d:
            numero= float(input("numero: "))
            l2.append (numero)
            cont+=1
        ans= cuadrantes(l1,l2)
        print (ans)

# leerImprimir()


#pregunta 5
def imprimirNumeros():
    n= int(input("digite un numero: "))
    for i in range (1,n+1):
        if i!=n:
            print (i, end= ""+ ", ")
        if i==n:
            print (n)
    r= 1
    t= 2
    cont= 1
    while cont<n:
        for i in range (1+n*r,t*n+1):
            if i != t*n:
                print (i, end= ""+ ", ")
            if i == t*n:
                print (i)
        cont+=1
        r+=1
        t+=1 

# imprimirNumeros()

#pregunta 6
def determinarRegalos (presupuesto):
    l1= ["flores",100000]
    l2= ["chocolates", 40000]
    l3= ["chocolatina Jet", 1000]
    l4= ["concierto", 200000]
    l5= ["viaje", 2000000]
    l6= ["empanadas", 2000]
    l7= ["pony malta con pandebono", 3000]
    l= [l1,l2,l3,l4,l5,l6,l7]
    listaPre= []
    cont= 0
    maximo= len(l)
    while cont<maximo:
        posicion= l [cont]
        if posicion [1]<=presupuesto:
            listaPre.append(posicion [0])
        cont+=1
    print (listaPre)

# determinarRegalos(2000000)
#pregunta 7
def mezclar(list1,list2):
    maximoL1= len(list1)
    maximoL2= len(list2)
    cont1= 0
    cont2= 0
    lista= []
    while cont1<maximoL1 or cont2<maximoL2:
        if cont1<maximoL1:
            lista.append (list1[cont1])
            cont1+=1
        if cont2<maximoL2:
            lista.append (list2[cont2])
            cont2+=1
            if cont2<maximoL2:
                lista.append (list2[cont2])
                cont2+=1
    return lista

def leerImprimir():
    repeticiones= int(input("repeticiones"))
    cont= 0
    while cont<repeticiones:
        cont+=1
        tamañoLista= int(input("digitos"))
        i= 0
        list1= []
        list2= []
        while i<tamañoLista:
            numero= int(input("numero"))
            list1.append (numero)
            i+=1
        tamañoLista= int(input("digitos"))
        i=0
        while i<tamañoLista:
            numero= int(input("numero"))
            list2.append (numero)
            i+=1
        funcion= mezclar(list1,list2)
        print (funcion)
# leerImprimir()

#pregunta 8
def fracasos (l):
    lFracasados= []
    cont= 0
    maximo= len(l)
    while cont<maximo:
        if (l[cont][4])>(l[cont][5]):
            lFracasados.append (l[cont][0])
        cont+=1

    return lFracasados

# print (fracasos([["Erase una vez en Hollywood", "Quentin Tarantino","Humor Negro", 2016, 90, 374, ["Leonardo Di Caprio", "Brad Pitt", "Margot Robbie"]], ["Avengers Endgame",
#     "Hermanos Russo", "Acción", 2019, 356, 2800, ["Mark Ruffalo", "Robert Downey Jr.", "Chris Evans","Chris Hemsworth", "Scarlett Johansson"]], ["The Ladykillers", 
#     "Alexander Mackendrick", "Humor Negro", 1955, 2, 10, ["Alec Guinness", "Herbert Lom", "Peter Sellers", "Cecil Parker"]],["50 First Dates", "Peter Segal",
#     "Comedia Romántica", 2004, 75, 120, ["Adam Sandler", "Drew Barrymore", "Rob Schneider"]]]))

def imprimirEstadisiticas(l):
    accion= 0
    infantil= 0
    humorNegro= 0
    terror= 0
    comediaRomantica= 0
    total= "total recaudado por genero: "
    f= 0
    cont= 0
    maximo= len(l)
    while f<maximo:
        if l[cont][2]== "Acción":
            accion+=(l[cont][5])

        if l[cont][2]== "Infantil":
            infantil+=(l[cont][5])

        if l[cont][2]== "Humor Negro":
            humorNegro+=(l[cont][5])

        if l[cont][2]== "Terror":
            terror+=(l[cont][5])

        if l[cont][2]== "Comedia Romántica":
            comediaRomantica+=(l[cont][5])
        cont+=1
        f+=1
    print (total)
    print ("Accion"+ " "+ str(accion))
    print ("Infantil"+ " "+ str(infantil))
    print ("Humor Negro"+ " "+ str(humorNegro))
    print ("Terror"+ " "+ str(terror))      
    print ("Comedia Romantica"+ " "+ str(comediaRomantica))

# imprimirEstadisiticas( [["Erase una vez en Hollywood", "Quentin Tarantino","Humor Negro", 2016, 90, 374, ["Leonardo Di Caprio", "Brad Pitt", "Margot Robbie"]], ["Avengers Endgame",
#     "Hermanos Russo", "Acción", 2019, 356, 2800, ["Mark Ruffalo", "Robert Downey Jr.", "Chris Evans","Chris Hemsworth", "Scarlett Johansson"]], ["The Ladykillers", 
#     "Alexander Mackendrick", "Humor Negro", 1955, 2, 10, ["Alec Guinness", "Herbert Lom", "Peter Sellers", "Cecil Parker"]],["50 First Dates", "Peter Segal",
#     "Comedia Romántica", 2004, 75, 120, ["Adam Sandler", "Drew Barrymore", "Rob Schneider"]]])

#pregunta 9     
def problema591 (n,hi):
    sumaDigitos= 0
    cont= 0
    while cont<len(hi):
        sumaDigitos+= hi[cont]
        cont+=1
    tamañoPila= sumaDigitos//len(hi)
    cont= 0
    residuo= 0
    k= 0
    while cont<len(hi):
        if hi[cont]<tamañoPila:
            residuo-=tamañoPila-hi[cont]
            k+=1
        if hi[cont]>tamañoPila:
            residuo+=hi[cont]-tamañoPila
            k+=1
        cont+=1
    return k

def leerImprimir():
    ejecucion= 1
    n= int(input("numero de pilas: "))
    while n!= 0:
        hi= []
        numero= input("numero str: ").split ()
        cont= 0
        cant= len(numero)
        while cont<cant:
            hi.append (int(numero[cont]))
            cont+=1
        x= problema591(n,hi)
        print ("set #"+str(ejecucion))
        ejecucion+=1
        print ("The minimum number of moves is "+ str(x))
        n= int(input("numero de pilas: "))
        

# leerImprimir()  

# pregunta10()
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

