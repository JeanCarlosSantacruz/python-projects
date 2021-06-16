#Jean Carlos Santacruz
#8962275
#Tarea 6

#pregunta 1
def sinonimos (dicc,cadena):
    final= ""
    if cadena[0] == "A":
        if cadena[1] in dicc:
            dicc[cadena[1]].append(cadena[2])
        else:
            dicc[cadena[1]]= cadena[2] 
    if cadena[0] == "D":
        if cadena[1] in dicc:
            dicc[cadena[1]].remove(cadena[2])
        else:
            print ("invalid word")
    if cadena[0] == "R":
        if cadena[1] in dicc[cadena[2]]:
            print (cadena[1], " is synonym of ", cadena[2])
        elif cadena[2] in dicc[cadena[1]]:
            print (cadena[2], " is synonym of ", cadena[1])
        else:
            print ("not found")


def leerImprimir ():
    repeticiones= int(input())
    for veces in range(repeticiones):
        dicc= {}
        n= int(input())
        claves= input().split()
        for i in range(n):
            elem= claves[i]
            dicc[elem]= []
        nCadenas= int(input())
        for i in range(nCadenas):
            cadena= input().split()
            sinonimos(dicc,cadena)
        
            

# leerImprimir ()

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

# leerImprimir()


#pregunta 3
def obtenerRango (d):
    lista= []
    for clave in d:
        for elemento in d[clave]:
            if elemento not in lista:
                lista.append (elemento)
    
    
    return lista

# print(obtenerRango({ 2 : [3, 4, 1], 4 : [5, 1, 7], 6 : [], 11 : [2, 4, 8, 10, 6] }))


#pregunta 4

def crearMatrizDispersa (m):
    disp= []
    for numero in range (len(m)):
        lista= []
        for elem in range (len(m[numero])):
            if m[numero][elem]!= 0:
                pos= elem
                num= m[numero][elem]
                tupla= (pos,num)
                lista.append (tupla)  
        disp.append (lista)
    return disp

def obtenerValor (disp,i,j):
    ans= 0
    for tupla in disp[i]:
        if tupla[0]==j:
            ans= tupla[1]
    return ans
    

def leerImprimir ():
    repeticiones= int(input())
    for veces in range (repeticiones):
        m= []
        disp= []
        nColum= input().split()
        for colum in range (int(nColum[0])):
            lista= []
            n= input().split()
            for elemento in n:
                lista.append (int(elemento))
            m.append(lista)
        disp= crearMatrizDispersa(m)
        print (disp)
        i= int(input())
        j= int(input())
        obt= obtenerValor(disp,i,j)
        print (obt)
        
# leerImprimir ()


#pregunta 5

def obtenerEstudiantes (cursos):
    estudiantes= []
    for curso in cursos:
        for i in cursos[curso]:
            if i[0] not in estudiantes:
                estudiantes.append(i[0])
    return estudiantes

def estudiantesEnComun (cursos,c1,c2):
    comun= []
    for i in cursos[c1]:
        persona= i[0]
        codigo= i[1]
        for e in cursos[c2]:
            if persona in e:
                tupla= (persona,codigo)
                comun.append (tupla)
    return comun

def leerImprimir():
    repeticiones= int(input())
    for veces in range (repeticiones):
        cursos= {}
        nCursos= int(input())
        for elem in range (nCursos):
            nombreCurso= input()
            nEstudiantes= int(input())
            lista= []
            for estudiante in range (nEstudiantes):
                listaE= []
                listaE.append(input())
                listaE.append(input())
                listaE.append(float(input()))
                lista.append (listaE)
            cursos[nombreCurso]= lista
        estu= obtenerEstudiantes(cursos)
        print (estu)
        c1= input()
        c2= input()
        comun= estudiantesEnComun(cursos,c1,c2)
        print (comun)
        
# leerImprimir ()




