# ordenacion_matriz.py

def ordenar_fila(matriz, fila_index):
    fila = matriz[fila_index]
    # Implementamos el algoritmo Bubble Sort para ordenar la fila
    for i in range(len(fila)):
        for j in range(0, len(fila) - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]


def main():
    # Definimos una matriz de ejemplo
    matriz = [
        [9, 2, 7],
        [3, 8, 5],
        [4, 6, 1]
    ]
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    fila_a_ordenar = int(input("Introduce el índice de la fila a ordenar (0, 1 o 2): "))
    if 0 <= fila_a_ordenar < len(matriz):
        ordenar_fila(matriz, fila_a_ordenar)
        print("Matriz con la fila ordenada:")
        for fila in matriz:
            print(fila)
    else:
        print("Índice de fila no válido")


if __name__ == "__main__":
    main()
