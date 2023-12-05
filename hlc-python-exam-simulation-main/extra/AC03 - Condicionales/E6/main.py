
if __name__ == '__main__':

    nombre = input("Escribe tu nombre: ")
    sexo = input("Escribe tu sexo: ")

    if (sexo == "Mujer" and nombre[0] < 'M') or (sexo == "Hombre" and nombre[0] > 'N'):
        msg = "Te corresponde el grupo 1"
    else:
        msg = "Te corresponde el grupo 2"

    print(msg)


