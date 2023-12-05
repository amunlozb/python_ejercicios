# Ángel Muñoz Lozano - DAW2

freshCost = 3.49
discount = 0.6

amount = int (input("Introduce la cantidad de barras que no son del día: "))

total = (freshCost * discount) * amount


if __name__ == '__main__':
    print("Precio de las barras que no son del día: ", total)


