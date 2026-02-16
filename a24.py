def a24():
    try:

        consumo = float(input("Ingrese el consumo de agua (m3): "))
        valor_m3 = float(input("Ingrese el valor por metro cúbico: "))

        total = consumo * valor_m3

        print("El valor total de la factura es:", total)


    except ValueError:
                print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a24()