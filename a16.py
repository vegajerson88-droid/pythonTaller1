def a16():
    try:

        numero = int(input("Ingrese un número entero: "))

        if numero % 2 == 0:
            print("El número es par.")
        else:
            print("El número es impar.")


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a16()