if __name__ == '__main__':
    altura = int(input("Introduce la altura del triángulo: "))

    for i in range(1, altura + 1):
        for j in range(2 * i - 1, 0, -2):
            print(j, end=' ')
        print()

