import random #generador de números aleatorios

def main ():
    numero_aleatorio = random.randint(1,100) #Genera un numero aleatorio entero entre un rango específicado
    numero_elegido = int(input("¿En que número entero entre 1 y 100 estoy pensando?\nTienes 10 intentos\n"))
    vidas=10
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Es mas grande")
            vidas -= 1
        elif numero_elegido > numero_aleatorio:
            print("Es mas pequeño")
            vidas -= 1
        if vidas == 0:
            print("El numero era: "+str(numero_aleatorio))
            print("Perdiste")
            break
        else:
            print("Tienes "+str(vidas)+" vidas")
            numero_elegido = int(input("Elige otro número: "))
    if numero_aleatorio == numero_elegido:        
        print ("Si, es ese.\n¡¡¡Felicidades Jonás!!!")

if __name__ == "__main__":
    main()