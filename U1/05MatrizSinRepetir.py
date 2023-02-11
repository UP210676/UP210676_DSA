
import random as sample
def llenarMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]=sample.randint(1,1000)
    return matriz
def imprimirMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

def main():
    n=int(input("Ingrese el tamaño de la matriz: "))
    matriz=[[0 for i in range(n)] for j in range(n)]
    matriz=llenarMatriz(matriz)
    imprimirMatriz(matriz)

if __name__ == "__main__":
    main()

