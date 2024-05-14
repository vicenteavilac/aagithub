def simulacion_compras(num_compras):
    saldo_tarjeta = 0
    
    for _ in range(num_compras):
        while True:
            try:
                monto_compra = float(input("Ingrese el monto de la compra: "))
                if monto_compra >= 0:
                    saldo_tarjeta += monto_compra
                    print(f"Compra realizada por ${monto_compra}. Saldo actual de la tarjeta: ${saldo_tarjeta}")
                    break  # Salir del bucle while si el monto es válido
                else:
                    print("Error: El monto de la compra debe ser mayor o igual a cero.")
            except ValueError:
                print("Error: Ingrese un monto válido.")

    print("Simulación de compras finalizada.")