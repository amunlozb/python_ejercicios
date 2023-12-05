
if __name__ == '__main__':

    palabra = (input("Introduce una palabra: ")).lower()

    auxPalindrome = ""

    for i in range (len(palabra) - 1, -1, -1):
        auxPalindrome += palabra[i]

    if palabra == auxPalindrome:
        msg = "Tu palabra es palíndrome"
    else:
        msg = "Tu palabra NO es palíndrome"

    print(msg)



