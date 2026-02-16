def a4():
    try:

        horas = float(input("Ingrese las horas trabajadas en la semana: "))
        valor_hora = float(input("Ingrese el valor por hora: "))

        salario = horas * valor_hora

        print("El salario semanal es:", salario)


    except ValueError:
        print("Debes Ingresar un Número Válido")

if __name__ == "__main__":
    a4()