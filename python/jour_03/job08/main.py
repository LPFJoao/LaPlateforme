a = float(input("Longueur A : "))
b = float(input("Longueur B : "))
c = float(input("Longueur C : "))

if a + b > c and a + c > b and b + c > a:
    
    if a == b == c:
        print("Le triangle est équilatéral.")
    elif a == b or b == c or a == c:
       
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Le triangle est un triangle rectangle isocèle.")
        else:
            print("Le triangle est isocèle.")

    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Le triangle est rectangle.")

    else:
        print("Le triangle est quelconque.")
        
else:
    print("Les longueurs données ne peuvent pas former un triangle.")