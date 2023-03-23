P = [5, 6, 2, '+', '*', 12, 4, '/', '-']
stack = []
r = 0
i = 0
P.append(')')
while P[i] != ')':
    if type(P[i]) == int:
        stack.append(P[i])
    else:
        b = stack.pop()
        a = stack.pop()    
        if  P[i] == '*':
                r = a * b
        elif P[i] == '/':
                r = a / b
        elif P[i] == '+':
                r = a + b
        elif P[i] == '-':
                r = a - b
        stack.append(r)
    i = i + 1        
print(stack)       
