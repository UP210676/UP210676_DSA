# Dada una expresión de parentesis, realizar un método que reciba como parámetro la 
# expresión y retorne TRUE si la expresión está balanceada o FALSE si es incorrecto.

def balanceado(lista):
    pila = []
    for parte in lista:
        for caracter in parte:
            if caracter == "(":
                pila.append(caracter)
            elif caracter == ")":
                if not pila: #si esta vacio
                    return False
                elif pila[-1] == "(":
                    pila.pop()
                else:
                    return False
    return not pila # si al finalizar, esta vacia, esta balanceado

lista1 = ["(())()", "(()",")()(", "(a*+())b()"]
for parte in lista1:
    if balanceado(parte):
        print(f"{parte} está balanceado")
    else:
        print(f"{parte} no está balanceado")
