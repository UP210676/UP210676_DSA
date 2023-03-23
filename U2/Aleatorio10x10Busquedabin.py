def mi_random(inicial, a, b, n):
    numeros = []
    # n números aleatorios
    for i in range(n):
        # bucle para generar un número aleatorio
        while True:
            # aplicar algoritmo hash a la semilla
            inicial = hash(str(inicial))
            
            # generar aleatorio en el rango a b
            num_aleatorio = a + (inicial % (b - a))
            
            if num_aleatorio not in numeros:
                numeros.append(num_aleatorio)
                break

    return numeros

def bubble_sort(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ordenarmatriz(matriz, lista):
    matriz = [[0 for j in range(10)] for i in range(10)]
    indice = 0
    for i in range(10):
        for j in range(10):
            matriz[i][j] = lista[indice]
            indice += 1
    return matriz  

def binarySearch(list1, valor):
    prin = 0; final = len(list1) - 1;  mit = (prin + final) // 2; contador = 0;
    while prin <= final and list1[mit] != valor:
        contador += 1
        if valor < list1[mit]:
            final = mit -1
        else:
            prin = mit + 1
        mit = (prin+final)//2
    if list1[mit] == valor:
        return (mit, contador)
    else:
        return (-1, contador) 

def main():

    matriz = []; valor = 404

    # crear lista
    lista_desordenada = mi_random(inicial='Carito :3', a=101, b=500, n=100)

    # ordenar la lista
    lista_ordenada = bubble_sort(lista_desordenada)

    # crear la matriz
    for i in ordenarmatriz(matriz, lista_ordenada):
        print(i)
    
    # buscar un valor
    indice, contador = binarySearch(lista_ordenada, valor)
    if indice == -1:
        print (f"El valor {valor} no se encontró en la matriz")
    else:
        print(f"El valor {valor} esta en la posicion {indice}, con {contador} iteraciones del ciclo while.")

if __name__ == "__main__":
    main()