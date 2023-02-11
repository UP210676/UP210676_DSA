#cuantos boletos puedcomprar 
dinero = int(input("Dinero: "))
boleto = 1
while dinero > 0:
    dinero = dinero - boleto
    boleto = boleto + 1

print("Boletos: ", boleto - 1)
