L = [1,2,3,4,5]

print("List: ",L)

print("Dernière valeur de la liste: ", L[1])

def remplacer_case(L):
   
        L[3] = L[2] + L[4]


remplacer_case(L)


print("Liste après modification :", L)


print("Dernière valeur de la liste :", L[-1])