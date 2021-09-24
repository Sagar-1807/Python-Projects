#INSERTION SORT ALGO-17 aug-21

def insert_sort(list):
    for secnd_no in range(1, len(list)):
        pointer=list[secnd_no]
        first_no=secnd_no-1
        while first_no >=0 and pointer < list[first_no]:
            list[first_no + 1]=list[first_no]
            first_no=first_no-1
        list[first_no + 1]=pointer
if __name__=='__main__':
    list=[45, 12, 23, 7, 15, 9, 5]
    insert_sort(list)
    print(list)