#Vamos a hacer un programa que indique si thanos de mata o no cuando chasquea los dedos
import random

def infinityGauntlet(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        fingerSnap=random.randint(0, 1)
        if fingerSnap == 1:
            print('Mueres')
        else:
            print('Vives')
    return wrapper

@infinityGauntlet
def genocide(name = 'Joel'):
    print('Hola '+ name + (', Thanos decide que: '))
    
genocide()