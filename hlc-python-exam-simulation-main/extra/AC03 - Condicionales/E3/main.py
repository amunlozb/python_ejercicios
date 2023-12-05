

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num1 = int(input("Introduce el primer número (dividendo): "))
    num2 = int(input("Introduce el segundo número (divisor): "))

    if num2 == 0:
        msg = "Error: El divisor no puede ser 0"
    else :
        msg = "Resultado de la división: " + str(num1 / num2)

    print(msg)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
