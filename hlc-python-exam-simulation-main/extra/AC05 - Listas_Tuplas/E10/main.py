
if __name__ == '__main__':
    lista = (50, 75, 46, 22, 80, 65, 8)
    valorMinimo = 9999999999
    valorMaximo = 0

    for num in lista:
        if num < valorMinimo:
            valorMinimo = num
        if num > valorMaximo:
            valorMaximo = num

    print("El valor mínimo es: " + str(valorMinimo))
    print("El valor máximo es: " + str(valorMaximo))



