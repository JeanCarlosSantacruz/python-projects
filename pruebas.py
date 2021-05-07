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


