import random
flag=True
while flag:
    upper_num=input(("Enter the upper number: "))
    if upper_num.isdigit():
        print('lets play')
        number=int(upper_num)
        flag=False  # means it stop iteration of upper_num line.
    else:
        print('Invalid input')
secret=random.randint(1,number)
guess=None
count=1
while guess!= secret:
    guess=input('please type number between 1 to ' +str(number)+":")
    if guess.isdigit():
        guess=int(guess)
    if guess==secret:
        print('correct')
    else:
        print('try again')
        count+=1
print('It took you',count,'guess')


