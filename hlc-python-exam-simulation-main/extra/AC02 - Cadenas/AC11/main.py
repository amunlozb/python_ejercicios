# Ángel Muñoz Lozano - DAW2

# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre
# del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total
# con 8 dígitos enteros y 2 decimales.

name = input("Introduce el nombre del producto: ")
price = float(input("Introduce el precio por unidad: "))
amount = int(input("Introduce la cantidad de unidades: "))

total = price * amount  # Calcula el costo total

msgPrice = "{:09.2f}".format(price)
msgAmount = "{:03d}".format(amount)
msgTotal = "{:011.2f}".format(total)

if __name__ == '__main__':
    print(name, "\nPrecio unitario: ", msgPrice, "\nCantidad de unidades: ", msgAmount, "\nCoste total: ", msgTotal)


