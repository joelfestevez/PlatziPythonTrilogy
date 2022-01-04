
# contador = 1
# print(contador)
# while contador < 1000:
#     contador = contador + 1
#     contador += 1
#     print (contador)

# for contador in range (1,101):
#     print (contador)

# for i in range (10):
#     print(11*i)

# a = list(range(100))
# print (a)

def tablas_de_multiplicar():

    print("Tablas de Multiplicar\n")
    num = int(input("Número de tabla que deseas: "))
    lim = int(input("Límite de la tabla (numero x límite): "))
    contador = 0

    for resultado in range (lim+1):
        resultado = num * contador
        print(str(num)+"*"+str(contador)+" = "+str(resultado))
        contador += 1

if __name__ == "__main__":
    tablas_de_multiplicar()