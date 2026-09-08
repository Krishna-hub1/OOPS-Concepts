#when we want to create an object instead of creating object manually we can use factory method to generate the object automatically.
class Calculator:
    def __init__(self,a,b):
        self.val1=a
        self.val2=b
    def addition(self):
        return self.val1+self.val2
    def multiplication(self):
        return self.val1*self.val2
    def division(self):
        return self.val1//self.val2
    @classmethod
    def generateobject(cls,p):
        return cls(*p)
pairs=[(10,20),(30,40),(50,60)]
list_of_objects=[Calculator.generateobject(p) for p in pairs]
for obj in list_of_objects:
    result=obj.addition()
    print("The addition of two numbers is:",result)
    
# Here we are using factory method to generate the object of class Calculator automatically. We are passing the tuple of values to the factory method and it is returning the object of class Calculator.