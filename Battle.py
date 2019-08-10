import random


attackers = input("Enter number of attackers: ")
defenders = input("Enter number of defenders: ")
updates = input("Would you like soldier status after each battle? Y/N: ")

if updates == "Y" or updates == "y":
    updates = True
elif updates == "N" or updates == "n":
    updates = False
else:
    print("Please type Y or N, try again")
    exit()

try:
    attackers = int(attackers)
    defenders = int(defenders)

except ValueError:
    print("non-integer value given, try again.")
    exit()


def battle(attackers, defenders):
    if updates:
        print(str(attackers) + " attackers and " + str(defenders) + " defenders remaining")

    attacker_dice = [0, 0, 0]
    defender_dice = [0, 0]

    for i in range(len(attacker_dice)):
        attacker_dice[i] = random.randint(0, 7)

    for i in range(len(defender_dice)):
        defender_dice[i] = random.randint(0, 7)

    defender_dice = sorted(defender_dice)
    attacker_dice = sorted(attacker_dice)

    if attacker_dice[0] > defender_dice[0]:
        defenders -= 1
    else:
        attackers -= 1

    if defenders > 1 and attackers > 1:
        if attacker_dice[1] > defender_dice[1]:
            defenders -= 1
        else:
            attackers -= 1

    if attackers == 0 and defenders == 0:
        print("Its a tie??")
        return

    if attackers <= 0:
        print("The defending country has won!")
        return

    if defenders <= 0:
        print("The attackers have won!")
        return

    return battle(attackers, defenders)

battle(attackers, defenders)