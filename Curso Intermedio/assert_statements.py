#Este programa nos da los divisores de un número ingresado en forma de lista
def divisors(num):
    divisors=[i for i in range(1,num+1) if num%i==0]
    return divisors

#Control de excepciones con try - except

def main():
        num = input("\nIngresa un número: ")
        assert num.isnumeric() and int(num)>0,"Debes ingresar un entero positivo"
        print(divisors(num))
        print("Termina programa")

            

if __name__=="__main__":
    main()