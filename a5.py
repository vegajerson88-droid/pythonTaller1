def a5():
    try:

        horas = float(input("Ingrese las horas trabajadas: "))
        valor_hora = float(input("Ingrese el valor por hora: "))

        if horas > 40:
            horas_normales = 40
            horas_extra = horas - 40
            salario = (horas_normales * valor_hora) + (horas_extra * valor_hora * 1.5)
        else:
            salario = horas * valor_hora

        print("El salario total es:", salario)


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a5()