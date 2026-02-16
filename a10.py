def a10():
    try:

        cantidad = int(input("Ingrese la cantidad de productos: "))
        total = 0

        for i in range(cantidad):
            precio = float(input("Ingrese el precio del producto: "))
            total += precio

        print("El total de la compra es:", total)


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a10()