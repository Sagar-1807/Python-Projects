import random
computer_win=0
sagar_win=0

def sagar_choose():
    sagar_choice=input('Choose Rock,paper or scissor:')
    if sagar_choice in ['ROCK', 'Rock', 'rock', 'R', 'r']:
        sagar_choice = 'r'
    elif sagar_choice in ['PAPER', 'Paper', 'paper', 'P', 'p']:
        sagar_choice = 'p'
    elif sagar_choice in ['scissor', 'SCISSOR', 'S', 's', 'Scissor']:
        sagar_choice = 's'
    else:
        print('plsenter correct word.')
        sagar_choose()
    return sagar_choice

def  computer_choose():
    computer_choice=random.randint(1,3)
    if computer_choice==1:
        computer_choice='r'
    elif computer_choice==2:
        computer_choice='p'
    elif computer_choice==3:
        computer_choice='s'
    return computer_choice

while True:
    print("")
    sagar_choice=sagar_choose()
    computer_choice=computer_choose()
    print("")

    if sagar_choice=='r':
        if computer_choice=='r':
            print('You chose rock  & computer chose rock,hence tie')

        elif computer_choice=='p':
            print('you chose rock & computer chose paper,hence computer win ')
            computer_win +=1

        elif computer_choice=='s':
            print('you chose rock & computer chose scissor,hence you win')
            sagar_win +=1


    elif sagar_choice=='p':
        if computer_choice=='r':
            print('You chose paper & computer  chose rock,hence you win')
            sagar_win += 1

        elif computer_choice=='p':
            print('you chose paper & computer chose paper,hence tie')

        elif computer_choice=='s':
            print('you chose paper & computer chose scissor,hence computer win')
            computer_win +=1


    elif sagar_choice == 's':
        if computer_choice == 'r':
            print('You chose scissor & computer chose rock,hence computer win')
            computer_win += 1

        elif computer_choice == 'p':
            print('you chose scissor & computer chose paper,hence you win')
            sagar_win+=1

        elif computer_choice == 's':
            print('you chose scissor & computer chose scissor,hence tie')


    print("")
    print("--------player win---------",sagar_win)
    print("--------computer win-------- ",computer_win)


    sagar_choice = input('Do you wanna continue (y/n) :')
    if sagar_choice in ['Yes','YES','yes','Y','y']:
        pass
    elif sagar_choice in ['NO','N','No','no','n']:
        break
    else:
        break