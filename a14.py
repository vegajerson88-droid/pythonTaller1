def a14():
    try:

        talleres = float(input("Ingrese la nota de talleres: "))
        parcial = float(input("Ingrese la nota del examen parcial: "))
        final = float(input("Ingrese la nota del examen final: "))

        nota_definitiva = (talleres * 0.30) + (parcial * 0.30) + (final * 0.40)

        print("La nota definitiva es:", nota_definitiva)


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a14()