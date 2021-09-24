'''
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizz _ buzz"
    if input % 3==0:
        return "Fizz"
    if input % 5 == 0:
        return  "Buzz"
    if input % 2==0:
        return 'Divided by 2'
    return input
print(fizz_buzz(9))'''
'''
savings=250
curr_value=[175,133,109,210,97]
futu_value=[200,125,128,228,133]

def selectstock():
    i=0
    for i in curr_value:
        buy1 = i
        if buy1 < savings:
            return 'stocks are:',curr_value[i],curr_value[i+1]
print(selectstock())'''