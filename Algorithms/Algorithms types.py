#VIDEO:Data Structures and Algorithms in Python  Python Programming Tutorial  720 x 1280
# CREATING TREE TRAVERSAL ALGO.
# CREATE NODE CLASS
class node():
    def __init__(self,val):
        self.childleft=None
        self.childright=None
        self.nodedata=val
#CREATE THE INSTANCE NOD CLASS TO CREATE THE TREE
root=node(1)
root.childleft=node(2)
root.childright=node(3)
root.childleft.childleft=node(4)
root.childleft.childright=node(5)

#INORDR-CREATE THE FUN TO TRAVEL IN ABOVE NODE
'''
def Inorder(root):
    if root:
        Inorder(root.childleft)
        print(root.nodedata)
        Inorder(root.childright)
Inorder(root)'''
#PREORDER TREE
'''
def Preorder(root):
    if root:
        print(root.nodedata)
        Preorder(root.childleft)
        Preorder(root.childright)
Preorder(root)'''
#POSTORDER TREE
'''
def Inorder(root):
    if root:
        Inorder(root.childleft)
        Inorder(root.childright)
        print(root.nodedata)
Inorder(root)'''
#---------------------------END-------------------------
# CREATING SORTING ALGO.
# ----1.MERGE SORT ALGO
#PENDING
# ----2. BUBBULE SORT ALGO
'''
def bubblesort(a):      # a is list
    b=len(a)-1
    for x in range(b):
        for y in range(b-x):
            if a[y]>a[y+1]:
                a[y],a[y+1]=a[y+1],a[y]     # swaping the elem.
    return a
a=[12,654,98,2,51,25,75,250,455]
print(bubblesort(a))'''
# ----3. INSERTION SORT ALGO
'''
def insrtsort(a):
    for x in range(1,len(a)):
        k=a[x]  # elem at 1st index
        j=x-1
        while j >=0 and k < a[j]:
            a[j+1]=a[j]
            j -= 1
        a[j+1]=k
a=[200,350,500,12,75,56]
insrtsort(a)
print(a)'''
# ----4. SELECTION SORT ALGO
'''
def selsort(myarray,r):
    for x in range(r):
        minimum=x       # 1st min value assumed
        for y in range(x+1,r):
            if myarray[y]<myarray[minimum]:
                minimum=y
        (myarray[x],myarray[minimum])=(myarray[minimum],myarray[x])
list=[1,21,15,51,84,67]
r=len(list)
selsort(list,r)
print(list)'''
# ----5. SHELL SORT ALGO
'''
def shellsort(myarray,n):
    gap=n//2                 # n: total no.s in list
    while gap>0:
        for x in range(gap,n):
            y=myarray[x]
            z=x
            while z>=gap and myarray[z-gap]>y:
                myarray[z]=myarray[z-gap]
                z-=gap
            myarray[z]=y
        gap//=2
list=[79,11,0,86,14,646]
l=len(list)
shellsort(list,l)
print(list)'''
#----------LINEAR SEARCH ALGORITHM
'''
def linalgo(list, n, key): # n=length of list,key = find the no.
    for x in range(0,n):
        if (list[x]==key):
            return x
    return -1
list=[6,79,4,0,87,64,46]
key=0   # to find in list
n=len(list)
matched=linalgo(list, n, key)
if (matched==-1):
    print("key is not present")
else:
    print("key is present at index",matched)'''
#for example for linear search algo
'''
def linalgo(list, n, key): # n=length of list,key = find the no.
    for x in range(0,n):
        if (list[x]==key):
            return x
    return -1
list=["Mango","apple","peru","grapes","banana"]
key=input("Ener to find")   # to find in list
n=len(list)
matched=linalgo(list, n, key)
if (matched==-1):
    print("key is not present")
else:
    print("key is present at index",matched)'''
#--------BINARY SEARCH ALGO
'''
def bin_search(list,key):
    l=0                         #left list value
    r=len(list)-1               #right list value
    matched=False
    while l<=r and not matched:
        middle=(l+r)//2
        if list[middle]==key:
            matched=True
        else:
            if key< list[middle]:
                r=middle-1
            else:
                    l=middle+1
    return matched
print(bin_search([12,27,35,99,101],56))
print(bin_search([12,27,35,99,101],35))'''

#------------------------------VIDEO END-----------------------------













































































