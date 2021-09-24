
#using temp var
'''
def bubblesort(a):
    for i in range(0,len(a)-1):      #This loop for iterate the complete list.
        for j in range(len(a)-1):   #this loop iterate list & comppare no.s
          if a[j]>a[j+1]:
              temp=a[j]
              a[j]=a[j+1]
              a[j+1]=temp
    return a
a = [18,12,27,45,78,8,19,25]
print('unsorted list is:',a)
print('sorted list is:',bubblesort(a))'''
#-------------------------------------------------------------------
#without using temp var

def bubblesort(b):
    total_itern=0

    for i in range(0,len(b)-1):
        for j in range(len(b)-1):
            if b[j]>b[j+1]:
                b[j],b[j+ 1]=b[j+1],b[j]    #swap
                print(b)
    total_itern+=1
    print('- - - - Total iteration done:',total_itern)
    return b

b=[12,2,47,89,16,7,1]
print('1] unsorted list is:',b)
print('sorted list is:',bubblesort(b)),print("")


#-------------------------------------------------------------------

'''
def bubblesort(b):
    is_swapped=True
    total_itern=0
    while is_swapped:
        is_swapped=False
    for i in range(0,len(b)-1):
        for j in range(len(b)-1):
            if b[j]>b[j+1]:
                b[j],b[j+ 1]=b[j+1],b[j]    #swap
                is_swapped=True
        total_itern+=1
    print('- - - - Total iteration done:',total_itern)
    return b
b=[12,2,47,89,16,7]
print('2] unsorted list is:',b)
print('sorted list is:',bubblesort(b))'''

#-------------------------------------------SOURCE:VIDEO
#  multiple SWAPPING METHOD IS USED
'''
def bubblesort(list):
    for i in range(len(list)-1,0,-1):           # INDEX STARTS FROM :-1,ITERATION IS: -1
            for j in range(i):
                if list[j]>list[j+1]:
                    temp=list[j]
                    list[j]=list[j+1]
                    list[j+1]=temp
                    print(list)

list=[12,8,7,6,11,10]
bubblesort(list)
print(" "),print("--- final sorted list ---- ")
print(list)'''