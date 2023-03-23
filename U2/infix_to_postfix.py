def procedencia_prioridad(c):
    if c in ['+', '-']:
        return 1
    elif c in ['*', '/']:
        return 2
    elif c in ['^']:
        return 3
    elif c in [')']:
        return 0
    else:
        return 0

# Infix
#Q = ['5', '*', '(', '6', '+', '2', ')', '-', '12', '/', '4']
# Postfix = [ 5 6 2 + * 12 4 / - ]
P = []
stack = []
O = ['+', '-', '*', '/', '^', '(', ')']

Q.append(')')
Q.insert(0, '(')

for i in Q:
    if i not in O:       # si es un operando 
        P.append(i)
    elif i == '(':       # si es paréntesis izquierdo
        stack.append(i)
    elif i == ')':       # si es paréntesis derecho
        while stack and stack[-1] != '(':
            P.append(stack.pop())
        if stack and stack[-1] == '(':
            stack.pop()
    else:                # si es operador
        while stack and procedencia_prioridad(stack[-1]) >= procedencia_prioridad(i):
            P.append(stack.pop())
        stack.append(i)

while stack:
    P.append(stack.pop())            
               
print(P)