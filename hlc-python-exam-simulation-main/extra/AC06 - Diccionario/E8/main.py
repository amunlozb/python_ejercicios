if __name__ == '__main__':
    esp = input("Introduce una palabra en español: ")
    eng = input("Introduce su traducción en inglés: ")

    # He añadido algunas palabras manualmente al diccionario
    diccionario = {"hola": "hello", "donde": "where", "adios": "bye", esp: eng}

    frase = input("Introduce una frase en español: ")
    palabras = frase.split()

    fraseTraducida = ""

    for palabra in palabras:
        if palabra in diccionario:
            fraseTraducida += diccionario[palabra] + " "
        else:
            fraseTraducida += palabra + " "

    print(fraseTraducida)
