# Ángel Muñoz Lozano - DAW2

date = str(input("Introduce una fecha (dd/mm/aaaa): "))

day = date.split("/")[0]
month = date.split("/")[1]
yr = date.split("/")[2]

if __name__ == '__main__':
    print("Día: ", day, "\nMes: ", month, "\nAño: ", yr)
