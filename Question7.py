class MycClass:
    "This is my first class for getting  and printing values"
    def __init__(self,string_value):
        self.string_value = string_value
        
    
    def getvalue (self):
        return self.string_value
    
    def printvalue(self):
        print(self.string_value.upper())
    
ob=MycClass("Suraj")
print(MycClass.__doc__)
s=ob.getvalue()
ob.printvalue()
