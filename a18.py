def a18():
    try:

        edad = int(input("Ingrese la edad: "))

        if edad < 18:
            print("Es menor de edad.")
        elif edad < 60:
            print("Es adulto.")
        else:
            print("Es adulto mayor.")


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a18()