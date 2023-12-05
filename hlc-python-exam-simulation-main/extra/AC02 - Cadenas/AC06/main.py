# Ángel Muñoz Lozano - DAW2

phrase = input("Introduce una frase: ")
vowel = input("Introduce una vocal: ")

msg = phrase.replace(vowel, vowel.upper())

if __name__ == '__main__':
    print(msg)
