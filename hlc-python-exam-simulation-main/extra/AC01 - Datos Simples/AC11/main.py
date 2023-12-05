investment = float(input("Introduce la cantidad con la que comienzas: "))
interest = 0.04

firstYear = investment * (1 + interest)
secondYear = firstYear * (1 + interest)
thirdYear = secondYear * (1 + interest)

if __name__ == '__main__':
    print("Ahorros el primer año: {:.2f}".format(firstYear))
    print("Ahorros el segundo año: {:.2f}".format(secondYear))
    print("Ahorros el tercer año: {:.2f}".format(thirdYear))
