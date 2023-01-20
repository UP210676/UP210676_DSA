import random 

numerosecreto = random.randint(1,100)
print("Adivina el número secreto")

numero = int(input("Introduce un número: "))

while True:
    
    if numero == numerosecreto:
        print ("Has acertado")
        break
    elif (numero > numerosecreto):
        numero = int(input("Ingresa un número más pequeño: "))
    else:
        numero = int(input("Ingresa un número más grande: "))

