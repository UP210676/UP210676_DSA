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

list1 = [-3,0,1,5,7,9]
valor = 5
indice, contador = binarySearch(list1, valor)
print(f"El valor {valor} esta en la posicion {indice}, con {contador} iteraciones del ciclo while.")