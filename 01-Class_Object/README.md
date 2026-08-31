A class is a structure that defines the properties and methods related to an object.
For example, in a Student Management System, we need information such as a student's name, age, roll number, and branch. We may also need methods to display or update student information.
So, we create a Student class to define these properties and methods.

**Object**
Object is instance of a class 
It is created when we want to use the properties and methods defined inside a class.
For example, consider a calculator. We create a `Calculator` class that takes two numbers and provides an addition operation.
class Calculator:
    def addition(self,x,y):
        return x+y

Here, Calculator is the class. It contains a method called addition(), which takes two values, x and y, and returns their sum. 
obj = Calculator() creates an object of the Calculator class. 
We can then use this object to call the addition() method by passing 10 and 20 as arguments. 
These values are received by x and y respectively. The method adds x and y and returns the result, which is 30.

Suppose a company wants to manufacture a car. Before manufacturing the car, the engineers first prepare a design or blueprint on paper. The design contains all the details required to build the car, such as the number of wheels, engine, seats, color, and other features.

This blueprint is similar to a class in programming. A class defines what properties and actions the car should have, but the class itself is not an actual car.

Once the company uses this blueprint to manufacture a car, the actual car is similar to an object. 
We can manufacture many cars using the same blueprint, and each car can have different values, such as different colors or models.
