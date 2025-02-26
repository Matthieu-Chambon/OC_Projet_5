words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

voyelles = "aeiouy"
list = []
for word in words:
    nb_voyelles = 0
    for letter in word:
        if letter in voyelles:
            nb_voyelles += 1
    list.append((word, nb_voyelles))

print(list)