def main():
    nombre=input("Hola, ¿Cual es tu nombre? \n")
    saludo="Hola "+ nombre
    print(saludo)
    print("La cadena anterior tiene "+ str(len(saludo.replace(" ",""))) + " caracteres")

if __name__ == "__main__":
    main()