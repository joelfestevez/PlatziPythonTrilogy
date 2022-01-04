#This programal eliminates every duplicate element in a list

# def remove_duplicates(some_list):
#     without_duplicates=[]
#     for element in some_list:
#         if element not in without_duplicates:
#             without_duplicates.append(element)
#     return without_duplicates

# def run():
#     random_list = [1,1,2,3,5,5,6,8,8,9,4,5,4,4,10]
#     print(remove_duplicates(random_list))

# if __name__ == '__main__':
#     run()

#---------------Challenge---------------

def remove_duplicates(some_list):
    without_duplicates = set(some_list)
    return without_duplicates

def run():
    random_list = [1,1,2,3,5,5,6,8,8,9,4,5,4,4,10]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()

    