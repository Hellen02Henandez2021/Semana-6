#1) Una farmacia desea un programa para ingresar el valor de
#Cpmpra y calcular lo siguiente si el pago se efectua al
#"contado",calcular un descuento del 
#5%; pero si el pago es con "targeta" se incrementa un recargo 
#del 3% al valor de compra.
#calcular y visualizar el descuento o recargo segun
#sea el caso y el total a pagar de la compra.
##

Compra = float(input("ingrese el valor de la compra"))
print("seleccione metodo de pago contado o targeta")
capturardatos =str(input("Metodo de pago"))

if capturardatos == "contado":
      Compra = Compra * 0.05
      compra= Compra - descuento 
      print("Se aplico el descuento", compra)
elif capturardatos == "targeta": 
     aumento = Compra *0.03
     compra = Compra + aumento
     print("No se aplico el descuento",compra)
else:
    print("Error no seleccionaste correctamete los cambios")