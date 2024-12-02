L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]


def remove_dublons(L):

    
    unique_list = []

    
    for n in L:
        
        f = False
        for unique_n in unique_list:
            if n == unique_n:
                f = True
                break
        
        if not f:
            unique_list.append(n)

    return unique_list



resultat = remove_dublons(L)


print(resultat)