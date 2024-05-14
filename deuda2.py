saldo=100000
disponiblidad=True
def mostrar_opciones():
    print("Menu de opciones:")
    print(" 1 Pago de tarjeta de credito")
    print(" 2 Simulacion de compras")
    print(" 3 Ver saldo disponible")
    print(" 4 Salir")


def pagar_tarjeta():
    global saldo
    montoapagar=int(input("Ingrese un monto a pagar: "))
    if montoapagar >= 0 and montoapagar <= saldo:
        saldo =-montoapagar
        print("Pago realizado exitosamente!")
    else:
        print("Opcion invalida o saldo insuficiente")

def simulacion_compras(num_compras):
        global saldo
        for _ in range  (num_compras):
            compras=int(input("Ingrese la cantidad de compras que ha hecho (0 para salir): "))
            if compras >= 0 and  compras < saldo :
                saldo=- compras
                print("Compras realizadas exitosamente")
            elif compras == 0:
                print("Chau")
            

