#Programa para determinar un número primo con depuración static typing en Python
#Depurador: $ mypy primo.py --check-untyped-defs

def prime(number: int)->bool:
    if number % 2 != 1:
        return False
    else:
        return True

def run():
    print(prime(3))

if __name__ == '__main__':
    run()