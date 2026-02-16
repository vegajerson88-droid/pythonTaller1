def a9():
    try:

        venta = float(input("Ingrese el valor de la venta sin IVA: "))

        iva = venta * 0.19
        total = venta + iva

        print("Valor del IVA:", iva)
        print("Total con IVA:", total)


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a9()