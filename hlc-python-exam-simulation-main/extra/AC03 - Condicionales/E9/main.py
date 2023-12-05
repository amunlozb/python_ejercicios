
if __name__ == '__main__':

    edad = int(input("Escribe tu edad: "))

    if edad < 4:
        precio = "Gratis"
    elif edad >= 4 and edad <= 18:
        precio = "5€"
    elif edad > 18:
        precio = "10€"

    print(precio)
