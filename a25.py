def a24():
    try:

        ventas = int(input("Ingrese el número de ventas realizadas en el día: "))
        valor_venta = float(input("Ingrese el valor de cada venta: "))

        total = ventas * valor_venta
        promedio = total / ventas

        print("El total vendido es:", total)
        print("El promedio por venta es:", promedio)


    except ValueError:
                print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a25()