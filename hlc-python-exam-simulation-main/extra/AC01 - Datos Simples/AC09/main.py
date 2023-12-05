# Ángel Muñoz Lozano - DAW2

investment = float (input("Introduce la cantidad a invertir: "))
interest = float (input("Introduce el interés anual a aplicar (en decimal): "))
years = int (input("Introduce la cantidad de años: "))

n = 12 # asumo que aunque el interes sea anual, se aplica cada mes

total = investment * (1 + (interest/ n)) ** (years * n)

if __name__ == '__main__':
    print("Capital obtenido en la inversión: ", total)


