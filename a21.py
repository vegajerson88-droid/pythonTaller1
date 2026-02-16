def a21():
    try:

        capital = float(input("Ingrese el capital inicial: "))
        tasa = float(input("Ingrese la tasa de interés (%): "))
        periodos = int(input("Ingrese el número de períodos: "))

        monto_final = capital * (1 + tasa / 100) ** periodos

        print("El monto final es:", monto_final)


    except ValueError:
                print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a21()