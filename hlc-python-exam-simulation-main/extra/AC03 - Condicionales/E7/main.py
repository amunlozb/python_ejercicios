
if __name__ == '__main__':

    renta = int(input("Introduce tu renta: "))

    if renta < 10000:
        res = 5
    elif renta >= 10000 and renta < 20000:
        res = 15
    elif renta >= 20000 and renta < 35000:
        res = 20
    elif renta >= 35000 and renta < 60000:
        res = 30
    elif renta >= 60000:
        res = 45

    print("Tipo impositivo: " + str(res) + "%")

