class Calculator:
    def addition(self,x,y):
        return x+y
# Creating an object from the Calculator class
obj=Calculator()
# Calling the method using the object and passing two numbers as arguments
result=obj.addition(10,20)
print("The addition of two numbers is:",result)
