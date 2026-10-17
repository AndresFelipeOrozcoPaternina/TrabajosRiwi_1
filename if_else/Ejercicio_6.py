numero1= float(input("Ingrese el numero 1:"))
numero2= float(input("ingrese el numero 2:"))

print("--------- Calculadora -----------------")
print("opcion 1 si es suma")
print("opcion 2 si es resta")
print("opcion 3 si es multiplicacion")
print("opcion 4 si es division")

sw= int(input("Ingresa opcion: "))

if sw==1:
    print("la suma de los numeros es :", (numero1+numero2))
elif sw==2:
    print("la resta de los numeros es :", (numero1-numero2))
elif sw==3:
    print("La multiplicacion de los numeros es :", (numero1*numero2))
elif sw==4 and (numero2==0 or numero1 == 0):
    print("El resultado es infinito")
elif sw==4 and (numero1 != 0 or numero2 != 0):
    print("La division de los numeros es:", (numero1/numero2))    