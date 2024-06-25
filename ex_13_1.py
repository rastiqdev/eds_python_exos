from time import sleep
from random import randint
print("Quel est votre nom ?")
name = input()
player = {"nom": name, "niveau": 1337, "attaque": 2, "résistance": 1, "pv": 10}
robot = {"nom": "Bip", "niveau": 420, "attaque": randint(0, 5), "résistance": randint(0, 5), "pv": randint(5, 20)}

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
    diff = attacking["attaque"] - defending["résistance"]
    if diff > 0:
        defending["pv"] -= diff
        print(f"{defending['nom']} a perdu {diff} points de vie.")
    else:
        print(f"{defending['nom']} n'a pas perdu de points de vie.")
    sleep(1)
    turns+=0.5
    player_turn = not player_turn

if match_nul:
    print(f"Après un combat acharné, personne n'a réussi à battre son adversaire.")
    exit()

if player["pv"] <= 0: winner = robot
if robot["pv"] <= 0: winner = player

print(f"Bravo {winner['nom']}, vous avez vaincu votre adversaire.")