def type_of_Dev(langage):

    

    if langage.lower() == "JavaScript":
        print("tu es un développeur web")

    elif langage.lower() == "python":
        print("tu es un développeur IA")

    elif langage.lower() =="java":
        print("tu es un développeur logiciel")
    
    elif langage.lower() == "reactjs":
        print("tu es un développeur mobile")

    else:
        print(" un jour, je serai le meilleur développeur..." )


type_of_Dev(str(input("Tell us your speciality: ")))

