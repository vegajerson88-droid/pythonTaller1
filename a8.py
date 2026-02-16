def a8():
    try:

        precio = float(input("Ingrese el precio del producto: "))
        porcentaje = float(input("Ingrese el porcentaje de descuento: "))

        descuento = precio * (porcentaje / 100)
        precio_final = precio - descuento

        print("Valor del descuento:", descuento)
        print("Precio final:", precio_final)


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a8()