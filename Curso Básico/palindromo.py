# #Programa Palindromo
# def palindromo (palabra):
#     palabra = palabra.replace(" ","") #Eliminamos los espacios
#     palabra = palabra.lower()         #Pasamos la palabra a minusculas
#     palabra_invertida = palabra[::-1] #Genera la palabra al revés
#     if palabra == palabra_invertida:
#         return True
#     else:
#         return False


# def main():     ###Función principal##
#     palabra = input("Escribe una palabra: ")
#     es_palindromo = palindromo(palabra)
#     if es_palindromo == True:
#         print ("Es palindromo ")
#     else:
#         print("No es palindromo ")

# if __name__ == '__main__':
#    main ()



def main():
    palabra = (input("Escribe una palabra: ").replace(" ",""))
    palindromo = palabra.lower() [::-1]
    #print (palindromo)
    if palabra == palindromo:
        print ("En efecto mi estimado, estamos ante un palindromo")
    else:
        print("Me temo que no es palindromo")


if __name__ == "__main__":
    main()