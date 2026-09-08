# Property Decorator is used to access the private variables like normal variables.

class Student:
    def __init__(self, name, age):
        self.__name = name  # Private variable
        self.__age = age    # Private variable

    def info(self):
        print(self.__name, self.__age)

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, m):
        if m>0 and m<100:
            self.__age = m
s1=Student("BMK", 15)
s1.info()
s1.age = 20  # Using setter to set the age
print("Updated age:", s1.age)  # Using getter to get the age
s1.info()

# Here we have created a class Student with private variables __name and __age. 
# We have used the @property decorator to create a getter method for the age variable and a setter method to set the age variable.
