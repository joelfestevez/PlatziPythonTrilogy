#Este programa nos da los divisores de un número ingresado en forma de lista
def divisors(num):
    divisors=[i for i in range(1,num+1) if num%i==0]
    return divisors

#Control de excepciones con try - except

def main():
    while True:
        try:
            num = int(input("\nIngresa un número: "))
            if num<0 or num==0:
                raise ValueError
            print(divisors(num))
            print("Termina programa")
            break
        except ValueError:
            print("Debes ingresar un entero positivo")
            

if __name__=="__main__":
    main()