compra=float(input("Ingrese el valor de la compra:"))

if compra >= 200000:
    print("El valor con descuento es:", (compra-(compra*0.20)))
elif compra >= 100000 and compra < 200000:
    print("El valor con descuento es:", (compra-(compra*0.20)))  
else:
    print("No tienes descuento, tu valor es", compra)  