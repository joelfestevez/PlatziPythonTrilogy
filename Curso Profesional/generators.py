#Fibonacci sequence numbers on a generator
import time

def fibo_gen(max: int)->int:

    n1=0
    n2=1
    counter=0

    while True:
        if counter == 0 :
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            if aux <= max:
                n1, n2 = n2, aux
                counter += 1
                yield aux
            else:
                break

if __name__ == '__main__':
    fibonacci = fibo_gen(25)    #Instancing the iterator until the 25th element
    for idx, element in enumerate(fibonacci): #index for each element
        print(idx, " ", element)
        time.sleep(0.05) 


# A very short way to make it:

# from time import sleep
# def fibonacci_gen():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b

# if __name__ == "__main__":
#     fibonacci = fibonacci_gen()
#     for element in fibonacci:
#         print(element)
#         sleep(1)