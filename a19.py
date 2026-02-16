def a19():
    try:

        pesos = float(input("Ingrese el valor en pesos colombianos: "))
        tasa = float(input("Ingrese la tasa de cambio (COP a USD): "))

        dolares = pesos / tasa

        print("El valor en dólares es:", dolares)


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a19()