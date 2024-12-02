
n = int(input("number of repeats: "))
chaine = "abcdefghijklmnopqrstuvwxyz"*n

rows = len(chaine)

for i in range (1, rows + 1,2):
    print(chaine[:i])