def a23():
    try:

        peso = float(input("Ingrese el peso del paquete (kg): "))

        if peso <= 5:
            costo = 10000
        else:
            costo = 20000

        print("El costo de envío es:", costo)


    except ValueError:
                print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a23()