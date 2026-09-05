# Multiple Inheritance allows Multiple base classes Properties and methods inherited to a single derived class.

class King:
    def display(self):
        print("King")
class soldier:
    def show(self):
        print("Soldier")
    def display(self):
        print("Soldier Display")
class C(King,soldier):
    pass
obj=C()
obj.display()
obj.show()

"""
When we are calling method by using the object of class C, 
if that method is coming from both parent classes then which parent method should run that's ambiguity created. 
Then that ambiguity is called diamond problem. 
To solve this problem Python Uses method resolution order. 
In this case the method of class King will run because class King is written first in the inheritance of class C.
as Method resolution order follows c3 linearization algorithm. 
c3 linearization algorithm is used to find the order in which methods should be inherited in case of multiple inheritance.
"""
