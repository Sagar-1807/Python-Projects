import random
import time

roll_again="y"
while roll_again=="y":          # Yes
    print("\nRolling the dice")
    time.sleep(0.5)         #time 0.5 sec

    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print("The values are:")
    print("Dice 1= ",dice1,"\n dice 2=",dice2)

    if dice1==dice2:
        print("Double rolled or Draw")
    else:
        print("try again")

    roll_again=input("\n -----------Roll again ? Y/N  : ")
