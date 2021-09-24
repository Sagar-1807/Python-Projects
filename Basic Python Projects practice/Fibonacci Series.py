
def fibo(n):
    a=0
    b=1

    if n==1:
        print(a)
    else:
        for i in range(2,n):
            c=int(a+b)           #=3
            a=b             #then a=2
            b=c             #b=c i.e 3
            print(c)        # o/p=3
fibo(8)
#then in next iter.= 2+3=5,
#in next iter a=3,b=5,hence.= 3+5=8 and so on


























