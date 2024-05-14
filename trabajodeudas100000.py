deudas=100000
estar= True
while estar:
    print("Menu")
    print("1 realizar pago")
    print("2 realizar mulitples compras")
    print("3 para salir")
    opcion=int(input("Ingrese opcion de menu: "))
    match opcion:
        
        case 1:
            
            print("Realize un pago:")
            pago=int(input("Pago: "))
            if pago > 0 and pago <= deudas:
                print("Pago exitoso")
                deudas = deudas-pago
                print("El pago realizado es de:", pago,"| Su nuevo saldo es:", deudas)
            else:
                print("Opcion invalida o Saldo insuficiente.")
        case 2:
            numerodecompras=int(input("Ingrese cantidad de objetos que comprara: "))
            if numerodecompras <= 0:
                print("Opcion Invalida")
            for _ in range(numerodecompras):
                montodecompras=int(input("Ingrese el monto de su compra (0 para salir): "))
                if montodecompras == 0:
                    break
                elif montodecompras > 0 and montodecompras < deudas:
                    deudas = deudas - montodecompras
                    print("Su saldo nuevo es:", deudas)
                elif montodecompras > deudas:
                    print("Saldo insuficiente")
                    break
        case 3:
            print("Gracias por usar el progama, Adios!")
            break
                
        