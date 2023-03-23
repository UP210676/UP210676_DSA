# Dada una lista realizar un metodo que reciba como parametros
# la lista y el numero de corrimientos a la derecha

lista = [5,2,1,5,8,9,6,45,4,3,46,8,9]

def recorrerderecha(lista, n):
    for i in range(n):
        lista = [lista[-1]] + lista[:-1]
    return lista

lista = recorrerderecha(lista, 2)

print(lista)

# Otro metodo con pop e insert

lista = [4,3,2,1,8,9,10,11,12,13,14,15,16,17,18,19,20]

def recorrerderecha(lista, n):
    for i in range(n):
        ultimo_elemento = lista.pop()
        lista.insert(0, ultimo_elemento)
    return lista

lista = recorrerderecha(lista, 4)

print(lista)