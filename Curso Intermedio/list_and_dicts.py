#####Listas y diccionarios anidados########
#####Los diccionarios pueden almacenar listas y las listas pueden almacenar diccionarios.######

def run():
    my_list = [1,"Hello",True,4.5]
    my_dict = {"firstname":"Joel","lastname":"Flores"}

    #Super lista hecha de diccionarios

    super_list = [
        {"firstname":"Joel","lastname":"Flores"},
        {"firstname":"Jonás","lastname":"Flores"},
        {"firstname":"Juan","lastname":"Flores"},
        {"firstname":"Joel","lastname":"Castañeda"},
        {"firstname":"Raul","lastname":"Flores"},
    ]

    #Super diccionarion hecho de listas

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_num': [-1, -2, 0, 1, 2],
        'float_nums': [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for item in super_list:
        print(item["firstname"], "-", item["lastname"])

if __name__=='__main__':
    run()