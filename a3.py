def a3():
    try:

        celsius = float(input("Ingrese la temperatura en grados Celsius: "))

        fahrenheit = (celsius * 9/5) + 32

        print("La temperatura en Fahrenheit es:", fahrenheit)


    except ValueError:
            print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a3()