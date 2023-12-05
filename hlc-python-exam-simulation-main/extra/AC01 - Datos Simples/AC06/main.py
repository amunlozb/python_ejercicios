# Ángel Muñoz Lozano - DAW2

number = int(input("Introduce un número entero positivo: "))

# Sum of first n positive integers = n(n + 1)/2

total = (number * (number + 1)) / 2

if __name__ == '__main__':
    print("La suma de todos los enteros desde 1 hasta ", number, " es: ", total)


