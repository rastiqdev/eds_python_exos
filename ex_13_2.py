# Requirements
from time import sleep
from random import randint
from os import path, remove
import json

# Check progress
if path.exists("./ex_13_2_progress.json"):
    # Load existing progress
    progress_file = open("./ex_13_2_progress.json", "r").read()
    player = json.loads(progress_file)
    print(f"Heureux de vous revoir, {player['nom']}")

else:
    # No existing progress, create one
    print("Quel est votre nom ?")
    name = input()
    player = {"nom": name, "niveau": 1337, "attaque": 2, "resistance": 1, "pv": 10}

def do_fight():
    robot = {"nom": "Bip", "niveau": 420, "attaque": randint(0, 5), "resistance": randint(0, 5), "pv": randint(5, 20)}

    print(f"{player['nom']} VS {robot['nom']}")
    sleep(1)
    turns = 0
    player_turn = True
    match_nul = False
    while player["pv"] > 0 and robot["pv"] > 0:
        if turns == 10: 
            match_nul = True
            break
        if player_turn:
            attacking = player
            defending = robot
        else:
            attacking = robot
            defending = player
        diff = attacking["attaque"] - defending["resistance"]
        if diff > 0:
            defending["pv"] -= diff
            print(f"{defending['nom']} a perdu {diff} points de vie.")
        else:
            print(f"{defending['nom']} n'a pas perdu de points de vie.")
        sleep(1)
        turns+=0.5
        player_turn = not player_turn

    if match_nul:
        print(f"Après un combat acharné, persone n'a réussi à battre son adversaire.")
    else:
        if player["pv"] <= 0: winner = robot
        if robot["pv"] <= 0: winner = player
        print(f"Bravo {winner['nom']}, vous avez vaincu votre adversaire.")

    if winner == robot:
        print("Vous avez perdu :(")
        if path.exists("./ex_13_2_progress.json"):
            remove("./ex_13_2_progress.json")
        exit()
    else:
        player["pv"] = 10
        player["resistance"] += randint(1, 3)
    ask_next_step()

def ask_next_step():
    print(f"Voulez vous combattre un autre adversaire (C) ou quitter le jeu et sauvegarder votre profil ? (Q)")
    choice = input()
    if choice == "C":
        do_fight()
    if choice == "Q":
        content_to_write = json.dumps(player)
        progress_file = open("./ex_13_2_progress.json", "w")
        progress_file.write(content_to_write)
        exit()

do_fight()