def ordre_crois(L):
    
    length = 0
    for item in L:
        length += 1

    
    for i in range(length):
        
        min_index = i
        
        for j in range(i + 1, length):
            
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]

L = [ 11, 42, 39, 2, 8, 24, 27, 48 ,16, 9, 102, 7, 84, 91]

ordre_crois(L)

print(L)