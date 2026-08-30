A class is a structure that defines the properties and methods related to an object.
For example, in a Student Management System, we need information such as a student's name, age, roll number, and branch. We may also need methods to display or update student information.
So, we create a Student class to define these properties and methods.

**Object**
Object is instance of a class 
It is created when we want to use the properties and methods defined inside a class.
For example, consider a calculator. We create a `Calculator` class that takes two numbers and provides an addition operation.
class Calculator:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def addition(self):
        return self.x + self.y
Here, Calculator is the class. It defines two properties, x and y, and a method called addition().
obj = Calculator(10, 20)
Here, obj is an object of the Calculator class.

When we create the object, the values 10 and 20 are passed to the constructor. These values are stored in the object's properties:
We can then use the object to call the addition() method:
The method uses the data stored in the object and returns:

Suppose a company wants to manufacture a car. Before manufacturing the car, the engineers first prepare a design or blueprint on paper. The design contains all the details required to build the car, such as the number of wheels, engine, seats, color, and other features.

This blueprint is similar to a class in programming. A class defines what properties and actions the car should have, but the class itself is not an actual car.

Once the company uses this blueprint to manufacture a car, the actual car is similar to an object. 
We can manufacture many cars using the same blueprint, and each car can have different values, such as different colors or models.
