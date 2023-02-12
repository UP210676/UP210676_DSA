def doble(x):
    y = x * 2
    return y

numeros = [5, 2, 7, 9, 3]

# Imprimir cada elemento de la lista "numeros"
for numero in numeros:
    print(numero)

# Ordenar la lista "numeros" utilizando el algoritmo Bubble Sort
for i in range(len(numeros) - 1):
    for j in range(len(numeros) - 1 - i):
        if numeros[j] > numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

print(numeros)

valor = 10
if valor > 10:
    print("Mayor a 10")
else:
    print("Menor o igual a 10") 

print(doble(10))

print(". . . Hecho")