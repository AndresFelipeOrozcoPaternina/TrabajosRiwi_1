sw = 1
saldo = 500000.0

while sw != 4:
    print("============= CAJERO =============")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")
    
    
    try:
        sw = int(input("Ingresa una opción: "))
    except ValueError:
        print("Opción inválida. Ingresa un número del 1 al 4.")
        continue

    if sw == 1:
        print("Tu saldo actual es:",(saldo))

    elif sw == 2:
        while True:
            try:
                retirar = float(input("Valor a retirar: $"))
                if retirar <= 0:
                    print("El monto a retirar debe ser mayor a cero.")
                elif retirar > saldo:
                    print("Fondos insuficientes tu saldo actual es:", (saldo))
                    break
                else:
                    saldo -= retirar
                    print("Retiro exitoso, nuevo saldo: ",(saldo))
                    break
            except ValueError:
                print("Por favor ingresa solo numeros.")

    elif sw == 3:
        while True:
            try:
                deposito = float(input("\nValor a depositar: $"))
                if deposito <= 0:
                    print("El monto a depositar debe ser mayor a cero.")
                else:
                    saldo += deposito
                    print("Depósito exitoso. Nuevo saldo:",(saldo))
                    break
            except ValueError:
                print("Entrada inválida. Por favor ingresa solo números.")

    elif sw == 4:
        print("Gracias por usar el cajero.")

    else:
        print("Opción no válida. Selecciona entre 1 y 4.")