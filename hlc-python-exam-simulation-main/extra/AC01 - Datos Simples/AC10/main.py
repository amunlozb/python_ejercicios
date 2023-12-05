# Ángel Muñoz Lozano - DAW2

clownWeight = 0.112
dollWeight = 0.075

clownAmount = int (input("Introduce la cantidad de payasos que se han vendido: "))
dollAmount = int (input("Introduce la cantidad de muñecas que se han vendido: "))

total = (clownWeight * clownAmount) + (dollWeight * dollAmount)

if __name__ == '__main__':
    print("Peso total del paquete a enviar (en kg): ", total)


