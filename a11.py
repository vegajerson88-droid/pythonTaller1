def a11():
    try:

        ventas = float(input("Ingrese el total de ventas: "))

        comision = ventas * 0.05
        total_recibir = ventas + comision

        print("La comisión es:", comision)
        print("Total a recibir:", total_recibir)


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a11()