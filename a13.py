def a13():
    try:

        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))

        promedio = (nota1 + nota2 + nota3) / 3

        print("El promedio es:", promedio)

        if promedio >= 3.0:
            print("El estudiante aprueba.")
        else:
            print("El estudiante reprueba.")


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a13()