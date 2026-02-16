def a6():
    try:

        producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio unitario: "))
        cantidad = int(input("Ingrese la cantidad comprada: "))

        total = precio * cantidad

        print("El total a pagar por", producto, "es:", total)


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a6()