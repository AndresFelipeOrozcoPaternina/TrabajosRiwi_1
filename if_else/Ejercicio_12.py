lado1= int(input("Elige lado 1:"))
lado2= int(input("Elige lado 2:"))
lado3= int(input("Elige lado 3"))

if lado1==lado2==lado3 :
    print("El triangulo es equilatero")
elif lado1==lado2!=lado3 or lado1!=lado2==lado3:
    print("El triangulo es Isoceles")
else:
    print("Es escaleno") 
    
       