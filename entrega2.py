#Jean Carlos Santacruz
#8962275
#Código de Honor
# Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali, los valores éticos y la integri-
# dad son tan importantes como la excelencia académica. En este curso se espera que los estudiantes se comporten ética
# y honestamente, con los más altos niveles de integridad escolar. En particular, se asume que cada estudiante adopta el
# siguiente código de honor:
# Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
# a seguir los más altos estándares de integridad académica.
# Integridad académica se refiere a ser honesto, dar crédito a quien lo merece y respetar el trabajo de los demás. Por eso
# es importante evitar plagiar, engañar, ‘hacer trampa’, etc. En particular, el acto de entregar un programa de computador
# ajeno como propio constituye un acto de plagio; cambiar el nombre de las variables, agregar o eliminar comentarios
# y reorganizar comandos no cambia el hecho de que se está copiando el programa de alguien más. Para más detalles
# consultar el Reglamento de Estudiantes, Sección VI.


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

# print(crearMapa([5, 3]))

def leerImprimir ():
    valores= input().split()
    tamañoMapa= []
    cont= 0
    while cont < len(valores):
        tamañoMapa.append(int(valores[cont]))
        cont+= 1
    
        valores= input().split()
        posInicial= []
        cont2= 0
        tamaño= len(valores)
        while cont2 < tamaño-1:
            posInicial.append(int(valores[cont2]))
            cont2+= 1
        posInicial.append(valores[cont2])
        print (posInicial)
        instrucciones= input()
        print (instrucciones)
        mapa= crearMapa (tamañoMapa)
        print (mapa)

# leerImprimir ()