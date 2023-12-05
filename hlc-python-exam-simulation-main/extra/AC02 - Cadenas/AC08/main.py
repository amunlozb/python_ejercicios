# Ángel Muñoz Lozano - DAW2

price = str(input("Introduce el precio con dos decimales (X.XX): "))

eur = price.split(".")[0]
cents = price.split(".")[1]

if __name__ == '__main__':
    print("Euros: ", eur, "\nCentimos: ", cents)
