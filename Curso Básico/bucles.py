##Potencias de x hasta n

def main():
    numero=float(input("Digita el número que quieres elevar a potencias: "))
    limite = float(input("Digita el límite al que llegarán las potencias: "))
    contador = 0
    resultado = numero**contador

    while resultado < limite :
        print(str(round(numero,1))+"^"+str(contador)+ " = " +str(resultado))
        contador=contador+1
        resultado=numero**contador

if __name__ == "__main__":
    main()

# def main ():
#     LIMITE = 1000000 #Constante

#     contador = 0
#     potencia_2 = 2**contador

#     while potencia_2 < LIMITE:
#         print("2^"+str(contador)+"= "+ str(potencia_2))
#         contador=contador+1
#         potencia_2=2**contador


# #PUNTO DE ENTRADA
# if __name__ == "__main__":
#     main()
