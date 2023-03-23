def quicksort (a, primero, ultimo):
    central = (primero + ultimo) // 2
    pivote = a[central]
    i = primero
    j = ultimo
    while i <= j:
        while a[i] < pivote: 
            i += 1
        while a[j] > pivote: 
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if primero <= j:
        quicksort(a, primero, j)
    if i < ultimo:
        quicksort(a, i, ultimo)

list = [23, 34, 45, 12, 45]
quicksort(list, 0, len(list) -1)
print(list)




