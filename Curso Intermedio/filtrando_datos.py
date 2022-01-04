from data_filtering_db import DATA #Importamos los datos desde otro archivo

def main():
    #Filtramos los trabajadores que usan Python en Platzi por list_comprehensions
    all_python_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]

    all_platzi_workers=[worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    #Filtramos por Filter a mayores de 18, pero arroja todo el diccionario
    adults=list(filter(lambda worker : worker["age"] > 18, DATA))
    #Ahora solo extraemos los nombres
    adults=list(map(lambda worker : worker["name"], DATA))
    #Filtramos a mayores de 70
    old_people=list(map(lambda worker:worker | {"old":worker["age"]>70},DATA))

    #RETO
    all_python_devs_reto=list(filter(lambda worker:worker["language"]=="Python",DATA))
    all_python_devs_reto=list(map(lambda worker : worker["name"], DATA))

    all_platzi_workers_reto=list(filter(lambda worker:worker["organization"]=="Platzi",DATA))
    all_platzi_workers_reto=list(map(lambda worker : worker["name"], DATA))

    adults_reto=[worker["name"] for worker in DATA if worker["age"]>18]
    old_people_reto=[worker["name"] for worker in DATA if worker["age"]>70]
    #FIN DE RETO


    #Imprimimos lo que deseemos visualizar
    for worker in old_people_reto:
        print(worker)


if __name__=='__main__':
    main()