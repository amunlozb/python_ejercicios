# Ángel Muñoz Lozano - DAW2

num1 = int (input("Introduce el dividendo: "))
num2 = int (input("Introduce el divisor: "))
coc = num1 // num2
res = num1 % num2

msg = "{} entre {} da un cociente {} y un resto {}".format(num1, num2, coc, res)

if __name__ == '__main__':
    print(msg)


