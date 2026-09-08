# adding extra functionality to the existing class using operator overloading

class quantity:
    def __init__(self,weight):
        self.weight=weight
    def info(self):
        print("The weight is:",self.weight)
    def __add__(self,other):
        result=self.weight+other.weight
        return quantity(result)
q1=quantity(10)
q2=quantity(20)
result=q1+q2
result.info()

# Here we have created a class quantity with an attribute weight. We have overloaded the + operator to add the weight of two objects of the class quantity.