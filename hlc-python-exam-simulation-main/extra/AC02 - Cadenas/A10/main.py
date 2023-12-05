# Ángel Muñoz Lozano - DAW2

input = str(input("Introduce la lista de productos separados por comas: "))
list = input.split(",")
msg = ""

for i in range (len(list)):
    msg += list[i] + "\n"

if __name__ == '__main__':
    print(msg)
