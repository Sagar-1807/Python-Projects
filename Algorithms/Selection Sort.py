#  MULTIPLE SWAPPING CONSUME MUCH CPU POWER,OR MEMORY POWER
# SORT FROM START TO END
def bubblesort(list):
    for i in range(5):           # UPPER INDEX :7, INITIAL i=0
        min=i
        for j in range(i, 6):
            if list[j] < list[min]:
                min = j

        temp = list[i]
        list[i] = list[min]
        list[min] = temp
        print(list)


list=[12,18,27,36,11,10]
bubblesort(list)
print(" "),print("---Below is final sorted list ---- ")
print(list)