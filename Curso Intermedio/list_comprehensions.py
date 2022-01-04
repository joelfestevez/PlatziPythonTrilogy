import math

def main():
    
    ####################List comprehensions############################
    #squares = [i**2 for i in range(1,101) if i % 3 != 0] #Todo el código de la lista de abajo en una sola linea :V
    challenge=[i*4 for i in range(1,1000) if (i*4)%6==0 and (i*4)%9==0]
    print(challenge)

    # list_sqr = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         list_sqr.append(i**2)
    # print(list_sqr)

    ##################Dictionary Comprehensions#########################
    my_dict={i:math.sqrt(i) for i in range (1,1001)}
    print(my_dict)

    # my_dict={}
    # for i in range (1,101):
    #     my_dict[i]=i**3
    # print(my_dict)

    

if __name__=='__main__':
    main()