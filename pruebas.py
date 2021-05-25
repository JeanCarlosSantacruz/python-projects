#Tarea 6
#Jean Carlos Santacruz
#8962275


    
def imprimirPotencias ():
    n= int(input("digite un numero: "))
    cont= 0
    while 2**cont <= n:
        print (2**cont)
        cont+=1

imprimirPotencias()

def emoogle ():
    ejecucion= 1
    n= int(input("cantidad de numeros: "))
    caso= 1
    while n!= 0:
        cont1= 0
        cont2= 0
        contt= 0
        numero= input("numeros: ").split ()
        lista= []
        while contt < len(numero):
            lista.append (int(numero[contt]))
            contt+= 1
        for i in range (len(lista)):
            if lista[i] != 0:
                cont1+= 1
            if lista[i] == 0:
                cont2+= 1
        residuo= cont1-cont2
        print ("case "+ str(caso)+ ": "+ str(residuo) )
        n= int(input("cantidad de numeros: "))
        caso+= 1
         
# emoogle()


