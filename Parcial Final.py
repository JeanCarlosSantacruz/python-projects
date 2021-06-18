#Jean Carlos Santacruz - 8962275
#Alejandro Castañeda - 89644217

def descuentos ():
    condicion = True
    while condicion == True:
        recibo= ""
        cedula= int(input("digite su cedula: "))
        rol= input("¿cual es su rol? (profesor/estudiante)")
        print ("registrar el/los producto/s a comprar")
        productos= int(input("cantidad de productos: "))
        for producto in range(productos):
            codigo= int(input("codigo del producto: "))
            precio= int(input("digite el precio del producto: "))
            cantidad= int(input("cantidad de unidades: "))
            if rol == "profesor":
                total= (precio * cantidad)
                descuento= total * 0.2
                total-= descuento
            if rol == "estudiante": 
                total= (precio * cantidad)
                descuento= total * 0.5
                total-= descuento
            recibo+=  (str(int(total ))+ " por el producto "+ str(codigo)+", ")
            
        print (str("El "+ rol + " con "+ "cedula "+ str(cedula) + " debe pagar "+ recibo))
        continuar= input("¿desea continuar? (si/no) ")
        if continuar== "no":
            condicion = False


descuentos()