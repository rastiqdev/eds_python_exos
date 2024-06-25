from time import sleep
from random import randint
print("Quel est votre nom ?")
surname = input()
print("Et votre prénom ?")
name = input()

def game():
    chosen_number = randint(1, 50)
    print("J'ai choisi un nombre aléatoire entre 1 et 50.")
    guesses = 0
    while guesses < 10:
        print("Choisissez un nombre entre 1 et 50.")
        guessed_number = int(input())
        print(f"Vous avez choisi {guessed_number}.")
        sleep(1)
        if guessed_number == chosen_number: 
            print(f"Vous avez gagné {surname} {name} Bravo!!!")
            sleep(2)
            game()
        elif guessed_number > chosen_number:
            print("C'est moins")
        else: print("C'est plus")
        guesses+=1
    print(f"Vous avez perdu {surname} {name} dommage")
    sleep(1)
    game()

game()