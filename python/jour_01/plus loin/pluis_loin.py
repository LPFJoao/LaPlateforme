texte = "Que vous aillez fini vos jobs ou pas, rendre sur le projet sur votre intranet etremplir le"

compteur = int(0)

i = 0

while i < len(texte):

    if "e" in texte[i]:

        compteur += 1

    i +=1

print(f"Il as {compteur} 'e' dans le texte")
