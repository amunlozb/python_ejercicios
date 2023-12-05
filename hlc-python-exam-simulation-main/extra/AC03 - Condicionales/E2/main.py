

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    correcta = "contraseña"

    introducida = input("Introduce la contraseña: ").lower()

    if introducida == correcta:
        msg = "Correcto!"
    else:
        msg = "Erróneo!"

    print(msg)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
