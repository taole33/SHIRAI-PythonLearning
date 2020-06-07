import random


N=10000
n_list = []


for i in range (N):
    get_random = random.randint((-N)*10,N*10)
    n_list.append(get_random)


def sort(n_list):
    if len(n_list) <= 1:
        return n_list
    pivot = n_list[0]
    listA = []
    listB = []
    for i in range(1,len(n_list)):
        compared_number = n_list[i]
        if compared_number <= pivot:
            listA.append(compared_number)
        else:
            listB.append(compared_number)
    listA = sort(listA)
    listB = sort(listB)
    listC = [pivot]
    
    return listA + listC +listB





print(sort(n_list))



