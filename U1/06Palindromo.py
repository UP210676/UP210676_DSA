def palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ","")
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def main():
    palabra = input("Ingrese una palabra: ")
    if palindromo(palabra):
        print("Es palindromo")
    else:
        print("No es palindromo")   

if __name__ == "__main__":
    main()
