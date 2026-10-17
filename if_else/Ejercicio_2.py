numero1=int(input("Ingrese el numero:"))
numero2=int(input("Ingrese el numero 2:"))
Resultado=0

print("-----------Menu------------")
print("1. Si es suma")
print("2. Si es resta")

sw=int(input("Ingrese la opcion que necesiste: "))

if sw == 1 :
  Resultado= numero1 + numero2
  print("El resultado es",Resultado)

elif sw==2 : 
  Resultado= numero1 + numero2
  print("El resultado es",Resultado)

if Resultado > 10:
    print("El resultado es mayor a 10")
elif Resultado < 10:
   print("El resultado es menor a 10")    