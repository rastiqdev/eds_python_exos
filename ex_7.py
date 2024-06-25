for i in range(10):
    print("Je teste la boucle.")

liste = ["premier élément", "deuxième élément", "troisième élément", "quatrième élément", "cinquième élément"]
for i in range(len(liste)):
    print(liste[i])

dico = {"nom": "Dupont", "prénom": "Baptiste", "âge": "1337", "ville": "Evry-Courcouronnes"}
for key, value in dico.items():
    print(f"{key} : {value}")