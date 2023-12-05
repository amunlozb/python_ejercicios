if __name__ == '__main__':

    opcion = int(input("¿Que tipo de pizza quieres? 1 - Vegetariana. 2 - No Vegetariana: "))

    if opcion == 1:
        opcion = "Vegetariana"

        ingrediente = int(input("Elige un ingrediente: 1 - Pimiento. 2 - Tofu: "))

        if ingrediente == 1:
            ingrediente = "Pimiento"
        elif ingrediente == 2:
            ingrediente = "Tofu"

    elif opcion == 2:
        opcion = "No Vegetariana"

        ingrediente = int(input("Elige un ingrediente: 1 - Peperoni. 2 - Jamón. 3 - Salmón: "))

        if ingrediente == 1:
            ingrediente = "Peperoni"
        elif ingrediente == 2:
            ingrediente = "Jamón"
        elif ingrediente == 3:
            ingrediente = "Salmón"

    print("Tu pizza es: " + opcion)
    print("Ingredientes: Tomate, Mozzarella y " + str(ingrediente))
