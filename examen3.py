#parcial 3
#Jean Carlos Santacruz
#Id: 8962275 

#pregunta 1
def restriccionRango (lista,conjunto):
    listaParejas= []
    for pareja in lista:
        if pareja[1] not in conjunto:
            listaParejas.append(pareja)
    return listaParejas

# print(restriccionRango([("a", 4), ("b", 3), ("c", 1), ("a", 5),("d", 6), ("b", 5)], {5, 3}))

#pregunta 2
def crearMatrizDispersa ():
    m= []
    nColum= input().split()
    for colum in range (int(nColum[0])):
        lista= []
        n= input().split()
        for elemento in n:
            lista.append (int(elemento))
        m.append(lista)
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

# crearMatrizDispersa ()

def reconstruirMatriz (disp):
    matriz= []
    for colum in range (len(disp)):
        lista= []
        for filas in range (len(disp)):
            lista.append (0)
        matriz.append (lista)
    print (matriz)




#pregunta 3
def obtenerCostoTexto (cad,d):
    valorCad= 0
    cad= cad.split()
    for palabra in cad:
        for clave in d:
            if palabra== clave:
                valorCad+= d[clave]
    return valorCad


# print(obtenerCostoTexto("mientras siga viendo tu cara en la cara de la luna",
# {"mientras" : 11, "siga" : 2, "viendo" : 6,"cara" : 3, "la" : 5}))

#pregunta 4
def obtenerRango (d):
    lista= []
    for clave in d:
        for elemento in d[clave]:
            if elemento not in lista:
                lista.append (elemento)
    
    
    return lista

# print(obtenerRango({ 2 : [3, 4, 1], 4 : [5, 1, 7], 6 : [], 11 : [2, 4, 8, 10, 6] }))


#pregunta 5
def organizarPalabras(a):
    respuesta={}
    listaC = list(a)
    for i in range(len(listaC)):
        if listaC[i] in respuesta:
            respuesta[listaC[i]].append(i)
        else:
            respuesta[listaC[i]] =[i]


    return respuesta

# print(organizarPalabras("el cielo resplandece a mi alrededor"))




