import math

def fnEcuacion(valor): 
    return math.pow(valor, 2) - 2

x1 = 1
x2 = 2
xm = 0
Es = 0.001
Er = abs(x2-x1)
i = 1
it = round((math.log(x2 - x1) - math.log(Es)) / math.log(2))
print("Número de iteraciones: ", it)

print("i   |     x1    |     x2    |      Er   |     xm    |" \
       "   f(x1)   |   f(xm)   | f(x1) * f(xm) |")

while Er >= Es:
    xm = (x1 + x2) / 2
    print("%3d |%10.4f |%10.4f |%10.4f |%10.4f |%10.4f |%10.4f \n" % 
          (i, x1, x2, Er, xm,  fnEcuacion(x1), fnEcuacion(xm)))
    if fnEcuacion(x1) * fnEcuacion(xm) < 0:
        x2 = xm
    else:
        x1 = xm
    Er = abs(x2 - x1)
    i = i + 1
    
print("La raíz es: ", xm)
