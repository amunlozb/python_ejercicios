
if __name__ == '__main__':

    edad = int(input("Introduce tu edad: "))
    ingresos = int(input("Introduce tus ingresos mensuales: "))

    if edad > 16 and ingresos >= 1000:
        msg = "Tienes que tributar"
    else:
        msg = "No tienes que tributar"

    print(msg)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
