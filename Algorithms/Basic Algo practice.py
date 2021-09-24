#FIND SMALLEST NO. IN ARRAY- FOR LOOP
''''
list=[12,15,21,45,9]
num=int(input("Enter the size of array:"))
for n in range(num):
    number=int(input("Enter Numbers:"))

small=list[0]
for n in range(num):
    if (list[n] > small):
        small=list[n]
print('big number is:',small)'''

#-------------------

