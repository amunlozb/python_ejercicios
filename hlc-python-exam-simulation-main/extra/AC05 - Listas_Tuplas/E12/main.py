import numpy as np

if __name__ == '__main__':

    # He tenido que investigar sobre el paquete "numpy" para ahorrarme codificar la multiplicación de matrices a mano

    matriz1 = np.array([[1, 2, 3], [4, 5, 6]])
    matriz2 = np.array([[-1, 0], [0, 1], [1, 1]])

    matrizResultado = matriz1@matriz2

    print(matrizResultado)
