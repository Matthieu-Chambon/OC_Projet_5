## Écrivez votre code ici !
def square(number):
    try:
        number_square = float(number) * float(number)
        print(f"{number} au carré = {str(number_square)}")
    except:
        print("Le paramètre doit être un nombre !")
        return None

user_number = input("Entrez un nombre : ")
square(user_number)
