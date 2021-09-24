#IN BINARY SEARCH LIST IS BIG
#LOGIC: DIVIDING THE LIST IN UPPERBOUND & LOWER BOUND.

choice_position=-1
def search(list,choice):
    lower=0
    upper=len(list)-1

    while lower <= upper:
        mid=(lower+upper)//2

        if list[mid]== choice:
            global choice_position
            choice_position= mid
            return True
        else:
            if list[mid]< choice:
                lower=mid+1
            else:
                upper=mid-1
    return False

list=[1,2,3,4,5,6,7,8,9]
choice=int(input("Enter:"))

if search(list,choice):
    print("Choice number found at",choice_position)
else:
    print("Choice number not found")





