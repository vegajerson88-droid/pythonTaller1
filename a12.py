def a12():
    try:

        ventas = float(input("Ingrese el valor de ventas mensuales: "))

        if ventas > 1000000:
            comision = ventas * 0.10
        else:
            comision = ventas * 0.05

        print("La comisión es:", comision)


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a12()