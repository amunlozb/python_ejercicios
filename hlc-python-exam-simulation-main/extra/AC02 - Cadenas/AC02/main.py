# Ángel Muñoz Lozano - DAW2

name = input("Introduce tu nombre completo: ");

name = name.lower()

lowerCase = name
upperCase = name.upper()
caps = name.title()

msg = lowerCase + "\n" + upperCase +"\n" + caps

if __name__ == '__main__':
    print(msg)


