list1 = [-5, 2, 3, 6, 1, 9, 14]
list2 = [-3, 0, 5, 7, 9, 10, 14]
a = 9

'''
def LinealNoSort(list1, a):
    pos = 0 
    for i in list1:
        pos += 1
        if i == a:
            a = pos
            break
        elif a not in list1:
            print ("El valor no se encuentra en la lista")
            break
    return (a)
print("El valor se encuentra en la posición: ", LinealNoSort(list1,a) -1)
'''
def LinealSort(list2, a): 
    for i in range(len(list2)):
        if list2[i]==a:
            return i
        elif list2[i] > a:
            break
    return None
print("El valor se encuentra en la posición: ", LinealSort(list2,a))


