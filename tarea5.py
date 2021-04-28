#pregunta 1
def guardarNumeros (l,r):
    f= []
    for i in range(l,r+1):
        if (i%3!=0 and i%4!=0):
            f.append (i)
    return f

def leerImprimir ():
    veces= int(input())
    i= 0
    while i<veces:
        p= int(input())
        q= int(input())
        ans= guardarNumeros(p,q)
        i+=1
        print (ans)
    
# leerImprimir()

#pregunta 2 
def lista_Tupla (l):
    cont= 0
    maximo= len(l)
    menor= l[cont]
    mayor= l[cont]  
    while cont < maximo:
        n = l[cont]
        if n<menor:
            menor= n
        if n> mayor:
            mayor= n
        cont+=1
    tupla= (menor,mayor)
    return tupla

def leerImprimir():
    veces= int(input("veces"))
    cont= 0
    i= 0
    l= []
    while i<veces:
        i+=1
        d= int(input("digitos"))
        while cont<d:
            numero= int(input("numero"))
            l.append (numero)
            cont+=1

    ans= lista_Tupla(l)
    print (ans)
        

# leerImprimir()

#pregunta 3
def revertir (l):
    tope= len(l)
    newL= []    
    while tope!= 0:
        newL.append(l[tope-1])
        tope-=1
    print (newL)

def leerImprimir ():
    cont= 0
    i= 0
    lis= []
    n= int(input("veces: "))
    while cont < n: 
        cont+=1
        digitos= int(input("cantidad de digitos: "))
        while i<digitos:
            d= int(input("numero: "))
            lis.append (d)
            i+=1
    x= revertir(lis)

# leerImprimir()

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
            
        i+= 1
            

    return lc

def leerImprimir():
    veces= int(input())
    cont= 0
    i= 0
    l1= []
    l2= []
    while i<veces:
        i+=1
        d= int(input("digitos"))
        while cont<d:
            numero= float(input("numero"))
            l1.append (numero)

        d= int(input("digitos"))
        cont= 0
        while cont<d:
            numero= float(input("numero"))
            l2.append (numero)

        ans= cuadrantes(l1,l2)
        print (ans)
leerImprimir()


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
        r+=1
        t+=1 



# imprimirNumeros()
#pregunta 6
def determinarRegalos (m):
    l1= ["flores",100000]
    l2= ["chocolates", 40000]
    l3= ["chocolatina Jet", 1000]
    l4= ["concierto", 200000]
    l5= ["viaje", 2000000]
    l6= ["empanadas", 2000]
    l7= ["pony malta con pandebono", 3000]
    l= [l1,l2,l3,l4,l5,l5,l6,l7]
    newL= []
    i= 0
    cont= 0
    maximo= len(l)
    while i<maximo:
        i+=1
        ln= l [cont]
        if ln [1]<=m:
            newL.append(ln [0])
    print (newL)

# determinarRegalos(10000)
#pregunta 7
def mezclar(l1,l2):
    m1= len(l1)
    m2= len(l2)
    cont= 0
    i= 0
    f= m2//2
    newL= []
    dato1= l1[cont]
    dato2= l2[i]
    while cont<m1 or i<m2:
        if cont<m1:
            newL.append (l1[cont])
            cont+=1
        if f<m2:
            newL.append (l2[i])
            i+=1
            f+=1
            if i<m2:
                newL.append (l2[i])
                i+=1
    print (newL)


def leerImprimir():
    veces= int(input("veces"))
    cont= 0
    i= 0
    list1= []
    list2= []
    while cont<veces:
        cont+=1
        d= int(input("digitos"))
        while i<d:
            numero= int(input("numero"))
            list1.append (numero)
            i+=1
        d= int(input("digitos"))
        i=0
        while i<d:
            numero= int(input("numero"))
            list2.append (numero)
            i+=1
    x= mezclar(list1,list2)
    print (x)
# leerImprimir()

#pregunta 8
def fracasos ():
    l = [["Erase una vez en Hollywood", "Quentin Tarantino","Humor Negro", 2016, 10, 374, ["Leonardo Di Caprio", "Brad Pitt", "Margot Robbie"]], ["Avengers Endgame",
    "Hermanos Russo", "Acción", 2019, 356, 2800, ["Mark Ruffalo", "Robert Downey Jr.", "Chris Evans","Chris Hemsworth", "Scarlett Johansson"]], ["The Ladykillers", 
    "Alexander Mackendrick", "Humor Negro", 1955, 15, 10, ["Alec Guinness", "Herbert Lom", "Peter Sellers", "Cecil Parker"]],["50 First Dates", "Peter Segal",
    "Comedia Romántica", 2004, 75, 120, ["Adam Sandler", "Drew Barrymore", "Rob Schneider"]]]
    lFracasados= []
    cont= 0
    maximo= len(l)
    maximo-=1
    f= 0
    while f<maximo:
        f+=1
        if (l[cont][4])>(l[cont][5]):
            lFracasados.append (l[cont][0])
            cont+=1

    print (lFracasados)

# fracasos()

def imprimirEstadisiticas():
    l = [["Erase una vez en Hollywood", "Quentin Tarantino","Humor Negro", 2016, 90, 374, ["Leonardo Di Caprio", "Brad Pitt", "Margot Robbie"]], ["Avengers Endgame",
    "Hermanos Russo", "Acción", 2019, 356, 2800, ["Mark Ruffalo", "Robert Downey Jr.", "Chris Evans","Chris Hemsworth", "Scarlett Johansson"]], ["The Ladykillers", 
    "Alexander Mackendrick", "Humor Negro", 1955, 2, 10, ["Alec Guinness", "Herbert Lom", "Peter Sellers", "Cecil Parker"]],["50 First Dates", "Peter Segal",
    "Comedia Romántica", 2004, 75, 120, ["Adam Sandler", "Drew Barrymore", "Rob Schneider"]]]
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
        f+=1
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
    print (total)
    print ("Accion"+ " "+ str(accion))
    print ("Infantil"+ " "+ str(infantil))
    print ("Terror"+ " "+ str(terror))      
    print ("Comedia Romantica"+ " "+ str(comediaRomantica))

# imprimirEstadisiticas()

#pregunta 9     
def problema591 ():
    n= int(input("numero de pilas: "))
    cont= 0
    i= 0
    k= 0
    l= []
    total= 0
    if n!=0:
        while i<n:
            b= int(input("numero de bloques: "))
            l.append(b)
            total+=b
            i+=1
        alturaMaxima= total//n
        tope= len(l)
        a= 0
    
        while cont<tope:
            cont+=1
            while l[a]>alturaMaxima:
                l[a]-=1
                k+=1
            while l[a]<alturaMaxima:
                l[a]+=1
                k-=1
            a+=1
    
        print (k)

        


                
# problema591()

