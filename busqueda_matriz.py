# busqueda_matriz.py

def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return (i, j)  # Retorna la posición (fila, columna)
    return None  # Retorna None si el valor no se encuentra


def main():
    # Definimos una matriz de ejemplo
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    valor = int(input("Introduce el valor a buscar: "))
    resultado = buscar_valor(matriz, valor)

    if resultado:
        print(f"Valor encontrado en la posición: {resultado}")
    else:
        print("Valor no encontrado en la matriz")


if __name__ == "__main__":
    main()
