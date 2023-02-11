
p = ['5','6','2','+','*','12','4','/','-',')']

def procedencia_prioridad(c):
    if c in ['+', '-']:
        return 4
    elif c in ['*', '/']:
        return 3
    elif c in ['^']:
        return 2
    elif c in ["(",")"]:
        return 1
    else:
        return 0

for i in range(len(p)):
    if p[i] in ['+', '-', '*', '/', '^','(',')']:
        print(p[i]," Es Operador y su prioridad es " + str(procedencia_prioridad(p[i])))
    else:
        print(p[i], " Es Operando") 



