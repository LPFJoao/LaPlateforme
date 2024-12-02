def nombre():
    n = int(input("Input your desired number: "))

    if n > 0:
        output = "Positive"
    
    elif n < 0:
        output = "Negative"

    elif n == 0:
        output = "THATs the same as 0 dumbdumb"
    
    return output

output = nombre()

print(output)
