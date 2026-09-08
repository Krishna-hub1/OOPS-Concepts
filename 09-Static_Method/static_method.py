# Static Method is a method that belongs to the class rather than an instance of the class.
class Student:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def get_school_name():
        return Student.school_name
Student1 = Student("BMK", 15)
print(Student.get_school_name())
"""
Here we have created a class Student and a static method get_school_name() which returns the school name. 
We can call this method using the class name without creating an instance of the class.
instance of a class means an object of that class.

"""