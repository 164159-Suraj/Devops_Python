print('enter a number')
number = int(input())
value=number

def isHarshed(newnum):
    s=0

    while newnum != 0:
        rem=newnum % 10
        s= s + rem
        newnum=newnum // 10

    return s 

x=isHarshed(value)
if(number % x==0):
        print('Harshed number')


else:
        print('Not a Harshed Number')
