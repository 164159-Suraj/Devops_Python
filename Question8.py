class Calculation:

    "This is class for calculating roots of the given values of an equation"

    def __init__(self,c_value,h_value,d_value):
     self.c_value = c_value
     self.h_value = h_value
     self.d_value = d_value
    def square_root(self):
     result=round(((2* self.c_value * self.d_value)/self.h_value) ** 0.5)
     return result
      

d = list(map(int,input('Enter the D values:  ').split(',')))
squareRoot_values = []

for i in d:
    ob=Calculation(50,30,i)
    x=ob.square_root()
    squareRoot_values.append(x)

print(squareRoot_values)

