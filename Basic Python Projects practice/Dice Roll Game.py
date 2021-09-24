import random
def main():
    player1=0
    player1wins=0
    player2=0
    player2wins = 0
    rounds=1

    while rounds!=5:        # rounds of game or repitation
        print("Round No:" + str(rounds))
        player1=dice_roll()
        player2= dice_roll()
        print("player-1 dice rolled:" + str(player1))
        print("player-2 dice rolled:" + str(player2))

        if player1==player2:
            print("-------------Draw\n")
        elif player1 > player2:
            player1wins = player1wins + 1
            print("-------------winner=Player-1\n")
        else:
            player2wins = player2wins + 1
            print("-------------winner=Player-2\n")

        rounds=rounds+1

    if player1wins == player2wins:
        print("-------Draw game---------")
    elif player1wins>player2wins:
        print("Hey.......winner is Player-1 ,Total won="+str(player1wins))
    else:
        print("Hey.......winner is Player-2 ,Total won ="+str(player2wins))

def dice_roll():
    diceroll=random.randint(1,6)
    return diceroll
main()