# Entradas
def a1():
    try:
        x = int(input("Ingrese el primer número entero: "))
        y = int(input("Ingrese el segundo número entero: "))
        z = int(input("Ingrese el tercer número entero: "))

        # Proceso
        sum = x + y + z
        average = sum / 3

        # Salidas
        print("La suma total es:", sum)
        print("El promedio es:", int(average))
        
    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a1()