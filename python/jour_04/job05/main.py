def calcule():

    num1 = int(input("Input a number: "))

    while True:
        operateur = input("Input an operator (+, -, *, /, %): ")
        if operateur in ['+', '-', '*', '/', '%']:
            break

    num2 = int(input("Input a number: "))

    if operateur == '+':
        result = num1 + num2

    elif operateur == '-':
        result = num1 - num2

    elif operateur == '*':
        result = num1 * num2

    elif operateur == '/':        
        if num2 == 0:

            return "Error: Division by zero is not allowed."
        
        result = num1 / num2
    
    elif operateur == '%':
        result = num1 % num2

    return result

result = calcule()

print("The result is: ", result)