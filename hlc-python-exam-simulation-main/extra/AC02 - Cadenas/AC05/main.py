# Ángel Muñoz Lozano - DAW2

original = input("Introduce una frase: ")
new = ""

for i in range(len(original) - 1, -1, -1):
    new += original[i]

if __name__ == '__main__':
    print(new)


