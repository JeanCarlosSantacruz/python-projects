𝓣𝓐𝓡𝓔𝓐𝓢 𝓢𝓔𝓜𝓐𝓝𝓐𝓛𝓔𝓢

def herramientas():
    trabajo= "taller1"
    fechaEntreha= "15/junio/11:59pm"

def programacion():
    trabajo= "tarea6"
    fechaEntrega= "11/junio/11:59pm"
    trabajo= "entrega2"
    fechaEntrega= "15/junio/8am"

def fundamentos(): 
    trabajo= "taller"
    fechaEntrega= "hoy"

def introInge():
    trabajo= ""
    fechaEntrega= ""

def modelado():
    trabajo= ""
    fecha= ""

def expresionOral():
    trabajo= ""
    fechaEntrega= ""


def humanidades():
    trabajo= ""   
    fechaEntrega= ""

def experiencia():
    trabajo= ""
    fechaEntrega= ""
    

def constitucion():
    trabajo= ""
    fechaEntrega= ""


def revisar (dicc,letra, s1, s2):
    if letra == "A":
        for clave in dicc:
            if clave== s1:
                dicc[clave].append (s2)
    print (dicc)

def leerImprimir():
    lista= []
    dicc= {}
    repeticiones= int(input("repeticiones: "))
    for i in range(repeticiones):
        cont= 0
        n= int(input("digite el tamaño del diccionario: "))
        claves= input("claves del diccionario:").split()
        while cont < n:
            dicc[claves[cont]]= lista
            cont+=1
        q= int(input("digite el tamaño del diccionario: "))
        for i in range(q):
            cadenas= input("digite la cadena: ").split()
            letra= cadenas[0]
            s1= cadenas[1]
            s2= cadenas[2]
            funcion= revisar(dicc,letra,s1,s2)
            print (funcion)
            

leerImprimir()

def prueba ():
    palabra= input("digite una palabra: ")
    palabra2= input("digite una palabra: ")
    dicc= {"feliz":[],"triste":[],"decepcionado":[]}
    for clave in dicc:
        if clave== palabra:
            dicc[clave].append (palabra2)
            
    
    
    print (dicc)

# prueba ()
lista2= []
            for numero in range (len(lista)):
                if lista[numero]!= 0:
                    pos= numero
                    num= lista[numero]
                    tupla= (pos,num)
                    lista2.append (tupla)       
            disp.append(lista2)


# revisar ({"alegre":[],"triste":[],"decepcionado":[]},"A","alegre","feliz")

def prueba (disp,i,j):
    ans= 0
    i= 6
    j= 4
    disp = [[(0, 1), (5, 4), (7, 5)],
    [(6, 4), (7, 7)],
    [(0, 2), (1, 2), (4, 9), (6, 1)],
    [],
    [(2, 8), (3, 1), (5, 7)],
    [(0, 3), (5, 6), (7, 2)],
    [(0, 4), (1, 4), (2, 7)],
    [(1, 9), (3, 8), (5, 7), (7, 6)]]
    for tupla in disp[i]:
        if tupla[0]==j:
            ans= tupla[1]
        
    return ans
        

# print (prueba())

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
    repeticiones= int(input("repeticiones: "))
    for veces in range (repeticiones):
        m= []
        disp= []
        nColum= input("numero de columnas: ").split()
        for colum in range (int(nColum[0])):
            lista= []
            n= input("numeros: ").split()
            for elemento in n:
                lista.append (int(elemento))
            m.append(lista)
        disp= crearMatrizDispersa(m)
        print (disp)
        i= int(input("i: "))
        j= int(input("j: "))
        obt= obtenerValor(disp,i,j)
        print (obt)
        
        
        

leerImprimir ()
estudiantesEnComun ({"Introducción a la Programación" :
[["Pepito Perez", "892324", 4.0],
["Rivaldo Rodriguez", "434335", 4.3],
["Novita Caicedo", "442565", 3.4]],
"Matemáticas" :
[["Pepito Perez", "892324", 4.0],["Ruperto Gutierrez", "111335", 4.3],
["Lupita Gallego", "789232", 4.8],
["Novita Caicedo", "442565", 3.4]],
"Humanidades" :
[["Eric Cartman", "343422", 2.0],
["Stan Marsh", "22999", 3.3],
["Novita Caicedo", "442565", 3.4]]},"Introducción a la Programación","Matemáticas")