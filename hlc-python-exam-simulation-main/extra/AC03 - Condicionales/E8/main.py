
if __name__ == '__main__':
    score = float(input("Escribe tu puntuación: "))

    if score == 0.0:
        nivel = "Nivel Inaceptable."
    elif score == 0.4:
        nivel = "Nivel Aceptable."
    elif score >= 0.6:
        nivel = "Nivel Meritorio."

    dinero = 2400 * score

    print(str(nivel) + " Te corresponden " + str(dinero) + "€")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
