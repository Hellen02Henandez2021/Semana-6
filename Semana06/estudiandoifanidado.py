#Si gasto hasta $100, pago con dinero en efectivo. Si no, si gasto más de $100 pero menos de $300, pago con tarjeta de débito. Si no, pago con
#tarjeta de crédito

#obtencion de datos
compra=int(input("coloque el dato de su compra"))
#En el primer if estamos comparando todos aquellos datos 
#Que sean menores o igual a 100
if compra<=100:
     print("pago en efectivo")
#Elif significa que vamos a evaluar otra condicion
#And significa vamos a evaluar 2 condiciones a 2 resultados
#Que se cumplen las condiciones de la izquierda y la derecha
elif compra  > 100 and compra < 300: 
    print("Pago con targeta de debito")
