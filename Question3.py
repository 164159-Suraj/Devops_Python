def factorial(num):
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        return fact

number= int(input('Enter a number '))
print('the factorial of the number is', factorial(number))