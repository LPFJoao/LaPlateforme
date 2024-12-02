def produit(type, saison):

    if type.lower() == 'fruits' and saison.lower() == 'hiver':
        print("orange, mandarine et kiwi")
    
    elif type.lower() == 'fruits' and saison.lower() == 'été':
        print("Poire, fraise, cassis")
    
    elif type.lower() == 'légume' and saison.lower() == 'hiver':
        print("carotte, topinambour, endive")

    elif type.lower() == 'légume' and saison.lower() == 'été':
        print("artichaut, aubergine, navet")

    else:
        print("Type ou saison non valide. Veuillez réessayer.")





produit(input("Tell us your Product type: "), input("Tell us which season: "))