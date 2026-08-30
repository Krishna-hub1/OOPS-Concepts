class Calculator:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def addition(self):
        return self.x+self.y
obj=Calculator(10,20)
result=obj.addition()
print("The addition of two numbers is:",result)