# Constructor is a special method in python class that is automatically called when an object of classs is created.
# In python constructor is defined using __init__() method.
# These are also called magic methods all magic mathods are start with __ and end with __.

class Calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def addition(self):
        return self.x+self.y
# Creating an object and passing two values to the constructor.
obj=Calculator(10,20)
# Calling the method using the object
result=obj.addition()
print("The addition of two numbers is:",result)
