def a22():
    try:

        inicial = int(input("Ingrese la cantidad inicial: "))
        vendidos = int(input("Ingrese la cantidad vendida: "))
        recibidos = int(input("Ingrese la cantidad recibida: "))

        inventario_final = inicial - vendidos + recibidos

        print("El inventario final es:", inventario_final)


    except ValueError:
                print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a22()