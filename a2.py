def a2():
    try:

        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))

        area = base * altura

        print("El área del rectángulo es:", area)

    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a2()