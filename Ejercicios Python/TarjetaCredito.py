# reciban por consola el valor de una compra
# que puedan ingresar el numero de cuotas a pagar
# calcular el valor de la cuota
# usando While queremos que imprima el plan de pago y le muestre el cupo liberado con cada pago

valorcompra = int(input("Digite el valor de su compra"))
cuotas = int(input("Digite la cantidad de cuotas:"))

valorcuotas = valorcompra / cuotas
cuota_actual = 1