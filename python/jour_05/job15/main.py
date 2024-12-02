L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]


def manual_round(num):
    integer_part = 0  
    decimal_part = 0  

    
    while num >= 1:
        integer_part += 1
        num -= 1

    decimal_part = num

    
    if decimal_part >= 0.5:
        return integer_part + 1  
    else:
        return integer_part  


def bubble_sort(L):
    n = 0  
    for _ in L:
        n += 1

    for i in range(n - 1):
        for j in range(n - i - 1):
            if L[j] > L[j + 1]:
                
                temp = L[j]
                L[j] = L[j + 1]
                L[j + 1] = temp
    return L


def round_and_sort(L):
    rounded_list = []

    
    for num in L:
        rounded_list.append(manual_round(num))

    
    sorted_list = bubble_sort(rounded_list)

    return sorted_list





result = round_and_sort(L)
print(result)
