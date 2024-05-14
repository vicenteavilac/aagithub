# Saldo inicial de la tarjeta
saldo_tarjeta = 100000

# Menú de opciones
def mostrar_menu():
    print("Menú de opciones:")
    print("1. Pago de Tarjeta de Crédito")
    print("2. Simulación de Compras")
    print("3. Salir")

# Función para pagar la tarjeta de crédito
def pagar_tarjeta():
    global saldo_tarjeta
    monto_pago = float(input("Ingrese el monto a pagar: "))
    if monto_pago >= 0 and monto_pago <= saldo_tarjeta:
        saldo_tarjeta -= monto_pago
        print("Pago realizado correctamente.")
    else:
        print("Monto inválido o excede el saldo de la tarjeta.")

# Función para simular compras
def simular_compras():
    global saldo_tarjeta
    total_compras = 0
    while True:
        monto_compra = float(input("Ingrese el monto de la compra (0 para salir): "))
        if monto_compra == 0:
            break
        elif monto_compra < 0:
            print("Monto inválido.")
        else:
            total_compras += monto_compra
    if total_compras > 0:
        saldo_tarjeta -= total_compras
        print("Total de compras realizadas: $", total_compras)

# Ciclo principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        pagar_tarjeta()
    elif opcion == '2':
        simular_compras()
    elif opcion == '3':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")