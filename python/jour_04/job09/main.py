def moyenne(note1, note2, note3):

    

    return (note1 + note2 + note3) / 3

note1 = float(input("Tell us your 1st Note: "))
note2 = float(input("Tell us your 2nd Note: "))
note3 = float(input("Tell us your 3rd Note: "))

moyenne_note = moyenne(note1, note2, note3)

print(f"The average note is: {moyenne_note:.2f}")

if  15 <= moyenne_note <= 20:
        print("Très bon élève")

elif 11 <= moyenne_note < 15:
        print("Bon élève")

elif 8 <= moyenne_note < 11:
        print("Élève moyen")

elif 0 <= moyenne_note < 8:
        print("Élève devant faire des efforts")

else:
        print("Make sure the notes are correct")


