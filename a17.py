def a17():
    try:

        nacimiento = int(input("Ingrese el año de nacimiento: "))
        actual = int(input("Ingrese el año actual: "))

        edad = actual - nacimiento

        print("La edad es:", edad)


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a17()