#USING FUN & FOR LOOP

choice_position=0
def search(list,choice):
    i=0
    while i < len(list):
        if list[i]==choice:
            global choice_position
            choice_position=i
            return True
        i=i+1
    return False

list=[12,5,6,7,8,9]
choice=int(input("Enter:"))

if search(list,choice):
    print("Choice number found at",choice_position)
else:
    print("This number not present in list")

#----------Example




