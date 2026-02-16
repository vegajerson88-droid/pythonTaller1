def a20():
    try:

        capital = float(input("Ingrese el capital: "))
        tasa = float(input("Ingrese la tasa de interés (%): "))
        tiempo = float(input("Ingrese el tiempo en meses: "))

        interes = capital * (tasa / 100) * tiempo
        total = capital + interes

        print("El interés simple es:", interes)
        print("El total a pagar es:", total)


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a20()