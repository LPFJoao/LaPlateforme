def verifier_pair_ou_impair():
    
    
    nombre_user = input("Entrez un nombre entier positif : ")
        
        
    if nombre_user.isdigit() and int(nombre_user) >= 0:

        nombre = int(nombre_user)

        if nombre % 2 == 0:
                print(f"{nombre} est pair.")
        else:
                print(f"{nombre} est impair.")
   
    else:
        print("Veuillez entrer un nombre entier positif valide.")
    
   


verifier_pair_ou_impair()