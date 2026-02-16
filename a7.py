def a7():
    try:

        total_compra = float(input("Ingrese el valor total de la compra: "))

        if total_compra > 200000:
            descuento = total_compra * 0.10
        else:
            descuento = 0

        total_final = total_compra - descuento

        print("Descuento:", descuento)
        print("Total a pagar:", total_final)


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a7()